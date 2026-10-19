"""Infusão contínua: valores de referência independentes, ida e volta, extremos e entradas inválidas."""

import math
import random

import pytest

from medicore import calculos as calc
from medicore.calculos import EntradaInvalida


def conc(qtd, unidade, volume):
    return calc.concentracao_por_diluicao(qtd, unidade, volume)


class TestValoresDeReferencia:
    def test_exemplo_da_versao_original(self):
        # 0,1 mcg/kg/min × 70 kg × 60 min/h ÷ 16 mcg/mL = 26,25 mL/h (conta feita à mão)
        r = calc.vazao_ml_h(0.1, "mcg/kg/min", conc(4, "mg", 250), 70)
        assert r.valor == pytest.approx(26.25)
        assert r.unidade == "mL/h"

    def test_concentracao_dobrada_reduz_vazao_pela_metade(self):
        # Erro da versão original: com 8 mg/250 mL a vazão correta é a metade (13,125), não 26,25
        r = calc.vazao_ml_h(0.1, "mcg/kg/min", conc(8, "mg", 250), 70)
        assert r.valor == pytest.approx(13.125)

    def test_noradrenalina_bula_2_a_3_ml_por_minuto(self):
        # Bula/rótulo: 4 mg em 1.000 mL = 4 mcg/mL; 8 a 12 mcg/min = 2 a 3 mL/min = 120 a 180 mL/h
        c = conc(4, "mg", 1000)
        assert c.valor_base_por_ml == pytest.approx(4.0)
        assert calc.vazao_ml_h(8, "mcg/min", c).valor == pytest.approx(120.0)
        assert calc.vazao_ml_h(12, "mcg/min", c).valor == pytest.approx(180.0)

    def test_amiodarona_tabela_do_rotulo_norte_americano(self):
        # Rótulo Nexterone: 360 mg/200 mL (1,8 mg/mL) a 0,556 mL/min ≈ 1 mg/min; a 0,278 mL/min ≈ 0,5 mg/min
        c = conc(360, "mg", 200)
        assert c.valor_base_por_ml == pytest.approx(1800.0)  # mcg/mL
        assert calc.vazao_ml_h(1, "mg/min", c).valor == pytest.approx(0.556 * 60, rel=1e-3)
        assert calc.vazao_ml_h(0.5, "mg/min", c).valor == pytest.approx(0.278 * 60, rel=1e-3)
        # 150 mg/100 mL a 10 mL/min = 15 mg/min
        c2 = conc(150, "mg", 100)
        assert calc.dose_pela_vazao(600, "mg/min", c2).valor == pytest.approx(15.0)

    def test_adrenalina_anafilaxia_refrataria_rcuk(self):
        # RCUK 2021: 1 mg em 100 mL (10 mcg/mL) a 0,5–1,0 mL/kg/h → 5–10 mcg/kg/h
        c = conc(1, "mg", 100)
        assert c.valor_base_por_ml == pytest.approx(10.0)
        assert calc.dose_pela_vazao(0.5 * 70, "mcg/kg/h", c, 70).valor == pytest.approx(5.0)
        assert calc.dose_pela_vazao(1.0 * 70, "mcg/kg/h", c, 70).valor == pytest.approx(10.0)

    def test_vasopressina_em_ui(self):
        # Rótulo: 50 UI em 500 mL = 0,1 UI/mL; 0,01 UI/min = 0,6 UI/h → 6 mL/h
        c = conc(50, "UI", 500)
        assert calc.vazao_ml_h(0.01, "UI/min", c).valor == pytest.approx(6.0)
        assert calc.vazao_ml_h(0.07, "UI/min", c).valor == pytest.approx(42.0)

    def test_mg_kg_h_com_concentracao_direta(self):
        # 0,05 mg/kg/h × 80 kg = 4 mg/h ÷ 1 mg/mL = 4 mL/h
        c = calc.concentracao_direta(1, "mg/mL")
        assert calc.vazao_ml_h(0.05, "mg/kg/h", c, 80).valor == pytest.approx(4.0)

    def test_gramas(self):
        c = conc(1, "g", 100)  # 10 mg/mL
        assert c.valor_base_por_ml == pytest.approx(10_000.0)
        assert calc.vazao_ml_h(10, "mg/h", c).valor == pytest.approx(1.0)

    def test_passos_documentam_as_conversoes(self):
        r = calc.vazao_ml_h(0.1, "mcg/kg/min", conc(4, "mg", 250), 70)
        texto = " ".join(r.passos)
        assert "4.000 mcg" in texto and "16 mcg/mL" in texto and "× 60 min/h" in texto and "26,25 mL/h" in texto


class TestIdaEVolta:
    def test_aleatorio_com_semente_fixa(self):
        rnd = random.Random(20261019)
        for _ in range(500):
            unidade = rnd.choice(list(calc.UNIDADES_DOSE))
            grandeza = calc.UNIDADES_DOSE[unidade].grandeza
            un_qtd = "UI" if grandeza == "UI" else rnd.choice(["mg", "mcg", "g"])
            qtd = rnd.uniform(0.5, 500) if un_qtd != "g" else rnd.uniform(0.01, 5)
            c = conc(qtd, un_qtd, rnd.uniform(10, 1000))
            peso = rnd.uniform(1, 200)
            dose = rnd.uniform(0.001, 50)
            try:
                v = calc.vazao_ml_h(dose, unidade, c, peso)
            except EntradaInvalida:
                continue  # combinações que excedem o limite de vazão são rejeitadas de propósito
            volta = calc.dose_pela_vazao(v.valor, unidade, c, peso)
            assert volta.valor == pytest.approx(dose, rel=1e-9)


class TestAlertasEExtremos:
    def test_vazao_muito_baixa_gera_alerta(self):
        r = calc.vazao_ml_h(0.001, "mcg/kg/min", conc(16, "mg", 50), 3)
        assert r.valor < 0.1
        assert r.alertas

    def test_vazao_muito_alta_gera_alerta(self):
        r = calc.vazao_ml_h(100, "mcg/min", conc(1, "mg", 1000), None)  # 6000 mcg/h ÷ 1 = 6000 mL/h
        assert r.valor > 1000
        assert r.alertas

    def test_vazao_absurda_e_rejeitada(self):
        with pytest.raises(EntradaInvalida):
            calc.vazao_ml_h(100, "mg/min", conc(1, "mg", 1000))  # 6.000.000 mL/h

    def test_peso_nos_limites(self):
        c = conc(4, "mg", 250)
        assert calc.vazao_ml_h(0.1, "mcg/kg/min", c, 0.3).valor > 0
        assert calc.vazao_ml_h(0.1, "mcg/kg/min", c, 350).valor > 0
        for peso in (0.29, 350.1, 0, -70):
            with pytest.raises(EntradaInvalida):
                calc.vazao_ml_h(0.1, "mcg/kg/min", c, peso)

    def test_unidade_sem_peso_ignora_peso(self):
        c = conc(4, "mg", 250)
        assert calc.vazao_ml_h(10, "mcg/min", c, None).valor == pytest.approx(37.5)
        assert calc.vazao_ml_h(10, "mcg/min", c, 999).valor == pytest.approx(37.5)


class TestEntradasInvalidas:
    @pytest.mark.parametrize("dose", [0, -0.1, math.nan, math.inf, None, True, "0,1", [0.1]])
    def test_dose_invalida(self, dose):
        with pytest.raises(EntradaInvalida):
            calc.vazao_ml_h(dose, "mcg/kg/min", conc(4, "mg", 250), 70)

    def test_unidade_de_dose_desconhecida(self):
        with pytest.raises(EntradaInvalida):
            calc.vazao_ml_h(1, "mcg/kg/s", conc(4, "mg", 250), 70)

    def test_peso_obrigatorio_para_unidade_por_kg(self):
        with pytest.raises(EntradaInvalida, match="peso"):
            calc.vazao_ml_h(0.1, "mcg/kg/min", conc(4, "mg", 250), None)

    def test_ui_com_concentracao_em_massa(self):
        with pytest.raises(EntradaInvalida, match="incompatíveis"):
            calc.vazao_ml_h(0.03, "UI/min", conc(4, "mg", 250))

    def test_massa_com_concentracao_em_ui(self):
        with pytest.raises(EntradaInvalida, match="incompatíveis"):
            calc.vazao_ml_h(1, "mcg/min", conc(20, "UI", 100))

    def test_concentracao_ausente(self):
        with pytest.raises(EntradaInvalida):
            calc.vazao_ml_h(1, "mcg/min", None)

    @pytest.mark.parametrize("qtd, unidade, volume", [(0, "mg", 250), (4, "mg", 0), (4, "mg", 0.5), (4, "mg", 5001), (4, "kg", 250), (100_001, "mg", 250), (-4, "mg", 250)])
    def test_diluicao_invalida(self, qtd, unidade, volume):
        with pytest.raises(EntradaInvalida):
            conc(qtd, unidade, volume)

    @pytest.mark.parametrize("valor, unidade", [(0, "mcg/mL"), (-1, "mg/mL"), (1, "mcg/L"), (math.nan, "mcg/mL")])
    def test_concentracao_direta_invalida(self, valor, unidade):
        with pytest.raises(EntradaInvalida):
            calc.concentracao_direta(valor, unidade)

    @pytest.mark.parametrize("vazao", [0, -1, 10_001, math.nan, None])
    def test_vazao_invalida_no_calculo_inverso(self, vazao):
        with pytest.raises(EntradaInvalida):
            calc.dose_pela_vazao(vazao, "mcg/kg/min", conc(4, "mg", 250), 70)


class TestNoradrenalinaSalBase:
    @pytest.mark.parametrize("sal, base", [(8, 4), (16, 8), (2, 1)])
    def test_conversao_da_bula(self, sal, base):
        r = calc.norepinefrina_hemitartarato_para_base(sal)
        assert r.valor == pytest.approx(base)
        assert "bula_hyponor" in r.referencias

    @pytest.mark.parametrize("sal", [0, -8, None, math.inf])
    def test_entrada_invalida(self, sal):
        with pytest.raises(EntradaInvalida):
            calc.norepinefrina_hemitartarato_para_base(sal)
