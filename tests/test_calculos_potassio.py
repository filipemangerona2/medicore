"""Potássio: classificação, conferência de infusão e volume de concentrado."""

import math

import pytest

from medicore import calculos as calc
from medicore.calculos import EntradaInvalida


class TestClassificacao:
    @pytest.mark.parametrize(
        "k, inicio_categoria, nivel",
        [
            (1.6, "Hipocalemia grave", "critico"),
            (2.49, "Hipocalemia grave", "critico"),
            (2.5, "Hipocalemia moderada", "alerta"),
            (2.99, "Hipocalemia moderada", "alerta"),
            (3.0, "Hipocalemia leve", "alerta"),
            (3.4, "Hipocalemia leve", "alerta"),
            (3.49, "Hipocalemia leve", "alerta"),
            (3.5, "Fora das faixas", "neutro"),
            (4.2, "Fora das faixas", "neutro"),
            (5.49, "Fora das faixas", "neutro"),
            (5.5, "Hipercalemia leve", "alerta"),
            (5.99, "Hipercalemia leve", "alerta"),
            (6.0, "Hipercalemia moderada", "critico"),
            (6.49, "Hipercalemia moderada", "critico"),
            (6.5, "Hipercalemia grave", "critico"),
            (8.0, "Hipercalemia grave", "critico"),
        ],
    )
    def test_faixas(self, k, inicio_categoria, nivel):
        resultado = calc.classificar_potassio(k)
        assert resultado.categoria.startswith(inicio_categoria)
        assert resultado.nivel == nivel

    @pytest.mark.parametrize("k", [5.5, 6.0, 6.5, 7.0])
    def test_regressao_hipercalemia_nunca_e_segura(self, k):
        # Erro da versão original: qualquer K ≥ 3,5 aparecia como "faixa segura", inclusive 7,0
        resultado = calc.classificar_potassio(k)
        texto = (resultado.categoria + " ".join(resultado.mensagens)).lower()
        assert "segura" not in texto
        assert resultado.nivel != "neutro"

    def test_3_4_nao_e_mais_rotulado_critico(self):
        assert calc.classificar_potassio(3.4).nivel == "alerta"

    def test_faixa_intermediaria_nao_promete_seguranca(self):
        mensagens = " ".join(calc.classificar_potassio(4.0).mensagens)
        assert "não é, por si só, garantia de segurança" in mensagens

    def test_ecg_na_hipercalemia_moderada(self):
        assert any("ECG de 12 derivações" in m for m in calc.classificar_potassio(6.1).mensagens)

    def test_referencias(self):
        assert "ukka_hipercalemia" in calc.classificar_potassio(7).referencias
        assert "sps2024_hipocalemia" in calc.classificar_potassio(2).referencias

    @pytest.mark.parametrize("k", [1.0, 1.49, 10.5, 14.9])
    def test_alerta_de_valor_extremo(self, k):
        assert any("Valor extremo" in m for m in calc.classificar_potassio(k).mensagens)

    @pytest.mark.parametrize("k", [0.4, 15.1, -1, math.nan, None, "4"])
    def test_entrada_invalida(self, k):
        with pytest.raises(EntradaInvalida):
            calc.classificar_potassio(k)


class TestConferenciaDeInfusao:
    def test_dentro_dos_limites(self):
        # 40 mmol em 1000 mL = 40 mmol/L; a 250 mL/h = 10 mmol/h
        v = calc.verificar_infusao_potassio(40, 1000, 250)
        assert v.concentracao_mmol_l == pytest.approx(40)
        assert v.taxa_mmol_h == pytest.approx(10)
        assert v.dentro_dos_limites

    def test_concentracao_acima_de_40_em_acesso_periferico(self):
        v = calc.verificar_infusao_potassio(40, 500, 100)  # 80 mmol/L
        assert any("acesso periférico" in a for a in v.alertas)

    def test_concentracao_acima_de_40_em_acesso_central_exige_k_menor_que_2(self):
        v = calc.verificar_infusao_potassio(40, 500, 100, acesso_central=True, potassio_serico_mmol_l=2.4)
        assert any("K sérico < 2" in a for a in v.alertas)
        v2 = calc.verificar_infusao_potassio(40, 500, 100, acesso_central=True, potassio_serico_mmol_l=1.8)
        assert not any("K sérico < 2" in a for a in v2.alertas)

    def test_concentracao_acima_de_80(self):
        v = calc.verificar_infusao_potassio(20, 100, 50, acesso_central=True, potassio_serico_mmol_l=1.5)  # 200 mmol/L
        assert any(a.startswith("Concentração acima de 80 mmol/L") for a in v.alertas)
        # 80 mmol/L exatos, acesso central e K < 2: admitido pelo SmPC (só o lembrete de > 40)
        v2 = calc.verificar_infusao_potassio(40, 500, 50, acesso_central=True, potassio_serico_mmol_l=1.5)
        assert not any(a.startswith("Concentração acima de 80 mmol/L") for a in v2.alertas)
        assert any(a.startswith("Concentração acima de 40 mmol/L") for a in v2.alertas)

    def test_velocidade_entre_10_e_20_sem_hipocalemia_grave(self):
        v = calc.verificar_infusao_potassio(40, 1000, 400)  # 16 mmol/h
        assert any("acima de 10 mmol/h" in a for a in v.alertas)
        v2 = calc.verificar_infusao_potassio(40, 1000, 400, potassio_serico_mmol_l=2.3)
        assert v2.dentro_dos_limites

    def test_velocidade_acima_de_20(self):
        v = calc.verificar_infusao_potassio(40, 1000, 600)  # 24 mmol/h, sem ECG e sem K
        assert len(v.alertas) == 3
        v2 = calc.verificar_infusao_potassio(40, 1000, 600, ecg_continuo=True, potassio_serico_mmol_l=1.8)
        assert len(v2.alertas) == 1  # só o lembrete de monitorização

    def test_velocidade_acima_de_40(self):
        v = calc.verificar_infusao_potassio(40, 1000, 1100, ecg_continuo=True, potassio_serico_mmol_l=1.5)  # 44 mmol/h
        assert any("40 mmol/h" in a for a in v.alertas)

    def test_passos(self):
        passos = " ".join(calc.verificar_infusao_potassio(40, 1000, 250).passos)
        assert "40,0 mmol/L" in passos and "10,0 mmol/h" in passos

    @pytest.mark.parametrize(
        "args",
        [
            (0, 1000, 250),
            (40, 0, 250),
            (40, 1000, 0),
            (501, 1000, 250),
            (40, 6000, 250),
            (40, 1000, 2001),
            (math.nan, 1000, 250),
            (None, 1000, 250),
        ],
    )
    def test_entradas_invalidas(self, args):
        with pytest.raises(EntradaInvalida):
            calc.verificar_infusao_potassio(*args)

    def test_flags_nao_booleanas(self):
        with pytest.raises(EntradaInvalida):
            calc.verificar_infusao_potassio(40, 1000, 250, acesso_central="sim")
        with pytest.raises(EntradaInvalida):
            calc.verificar_infusao_potassio(40, 1000, 250, ecg_continuo=1)


class TestVolumeDeConcentrado:
    def test_kcl_19_1(self):
        r = calc.volume_concentrado_potassio(20, 2.562)
        assert r.valor == pytest.approx(7.806, abs=1e-3)
        assert any("diluir" in a.lower() for a in r.alertas)

    @pytest.mark.parametrize("mmol, conc", [(0, 2.56), (20, 0), (20, 5.1), (501, 2.56), (None, 2.56)])
    def test_invalido(self, mmol, conc):
        with pytest.raises(EntradaInvalida):
            calc.volume_concentrado_potassio(mmol, conc)
