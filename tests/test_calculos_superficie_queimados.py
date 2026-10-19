"""Superfície corporal (Mosteller e DuBois) e reposição no grande queimado."""

import math

import pytest

from medicore import calculos as calc
from medicore.calculos import EntradaInvalida


class TestSuperficieCorporal:
    def test_mosteller_referencia(self):
        # √(170 × 70 ÷ 3600) = √3,30556 = 1,8181
        assert calc.superficie_corporal(70, 170).mosteller_m2 == pytest.approx(1.81812, abs=1e-4)

    def test_mosteller_produto_3600_resulta_1_m2(self):
        assert calc.superficie_corporal(60, 60).mosteller_m2 == pytest.approx(1.0)

    def test_dubois_pela_forma_logaritmica(self):
        # Caminho de cálculo independente: log10(SC) = log10(0,007184) + 0,425·log10(P) + 0,725·log10(A)
        for peso, altura in [(70, 170), (120, 160), (3.5, 50), (150, 190)]:
            esperado = 10 ** (math.log10(0.007184) + 0.425 * math.log10(peso) + 0.725 * math.log10(altura))
            assert calc.superficie_corporal(peso, altura).dubois_m2 == pytest.approx(esperado, rel=1e-12)

    def test_dubois_valor_conhecido(self):
        # 0,007184 × 100^1,15 = 0,007184 × 199,526 = 1,4334
        assert calc.superficie_corporal(100, 100).dubois_m2 == pytest.approx(1.4334, abs=1e-3)

    def test_diferenca_entre_formulas_em_obesidade(self):
        sc = calc.superficie_corporal(120, 160)
        diferenca = (sc.dubois_m2 - sc.mosteller_m2) / sc.mosteller_m2
        assert diferenca == pytest.approx(-0.057, abs=0.002)  # ≈ −5,7%: motivo de nomear cada fórmula

    def test_passos_identificam_as_formulas(self):
        passos = " ".join(calc.superficie_corporal(70, 170).passos)
        assert "Mosteller" in passos and "DuBois" in passos

    @pytest.mark.parametrize("peso, altura", [(0.4, 170), (351, 170), (70, 29), (70, 251), (None, 170), (70, math.nan)])
    def test_entradas_invalidas(self, peso, altura):
        with pytest.raises(EntradaInvalida):
            calc.superficie_corporal(peso, altura)


class TestReposicaoQueimado:
    def test_parkland_referencia(self):
        # 4 × 70 × 15 = 4200 mL; 1ª metade em 8 h = 262,5 mL/h; 2ª metade em 16 h = 131,25 mL/h
        r = calc.reposicao_queimado(70, 15, 4.0)
        assert r.total_24h_ml == pytest.approx(4200)
        assert r.taxa_primeiras_8h_ml_h == pytest.approx(262.5)
        assert r.taxa_16h_seguintes_ml_h == pytest.approx(131.25)

    def test_equacoes_da_calculadora_msd(self):
        # MSD: taxa 8 h = total ÷ 16; taxa 16 h = total ÷ 32
        r = calc.reposicao_queimado(82.5, 37.5, 4.0)
        assert r.taxa_primeiras_8h_ml_h == pytest.approx(r.total_24h_ml / 16)
        assert r.taxa_16h_seguintes_ml_h == pytest.approx(r.total_24h_ml / 32)

    def test_volumes_somam_o_total(self):
        r = calc.reposicao_queimado(63, 42, 2.0)
        assert r.volume_primeiras_8h_ml + r.volume_16h_seguintes_ml == pytest.approx(r.total_24h_ml)
        assert r.taxa_primeiras_8h_ml_h * 8 == pytest.approx(r.volume_primeiras_8h_ml)
        assert r.taxa_16h_seguintes_ml_h * 16 == pytest.approx(r.volume_16h_seguintes_ml)

    def test_aba_2_ml(self):
        r = calc.reposicao_queimado(70, 30, 2.0, adulto=True)
        assert r.total_24h_ml == pytest.approx(4200)
        assert r.referencias[0] == "aba2023_queimados"
        assert not any("fora dessa população" in a for a in r.alertas)

    def test_aba_fora_da_populacao(self):
        assert any("fora dessa população" in a for a in calc.reposicao_queimado(70, 15, 2.0, adulto=True).alertas)
        assert any("fora dessa população" in a for a in calc.reposicao_queimado(20, 30, 2.0, adulto=False).alertas)

    def test_parkland_avisa_recomendacao_da_aba(self):
        assert any("2 mL/kg/%SCQ" in a for a in calc.reposicao_queimado(70, 30, 4.0).alertas)

    def test_avisos_permanentes(self):
        alertas = " ".join(calc.reposicao_queimado(70, 30, 4.0).alertas)
        assert "superficiais" in alertas
        assert "8 h" in alertas  # momento zero não verificado

    def test_100_porcento(self):
        assert calc.reposicao_queimado(70, 100, 4.0).total_24h_ml == pytest.approx(28_000)

    @pytest.mark.parametrize("pct", [0, -5, 100.1, math.nan, None])
    def test_percentual_invalido(self, pct):
        with pytest.raises(EntradaInvalida):
            calc.reposicao_queimado(70, pct, 4.0)

    @pytest.mark.parametrize("fator", [3.0, 0, True, "4", None])
    def test_fator_invalido(self, fator):
        with pytest.raises(EntradaInvalida):
            calc.reposicao_queimado(70, 20, fator)

    @pytest.mark.parametrize("peso", [0.9, 351, None])
    def test_peso_invalido(self, peso):
        with pytest.raises(EntradaInvalida):
            calc.reposicao_queimado(peso, 20, 4.0)
