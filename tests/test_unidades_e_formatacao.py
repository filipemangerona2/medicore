import math

import pytest

from medicore.formatacao import fmt, fmt_auto
from medicore.unidades import (
    FATOR_CREATININA_MGDL_PARA_UMOLL,
    FATOR_GLICOSE_MMOLL_PARA_MGDL,
    creatinina_para_mg_dl,
    glicose_mmol_l_para_mg_dl,
    massa_para_mcg,
    mcg_para,
    mmol_por_ml_kcl,
)


class TestConstantes:
    def test_fator_creatinina_derivado_da_massa_molar(self):
        # 1 mg/dL = 10 mg/L; 10 / 113,12 mmol/L = 0,08840 mmol/L = 88,40 µmol/L
        assert pytest.approx(88.40, abs=0.01) == FATOR_CREATININA_MGDL_PARA_UMOLL

    def test_fator_glicose(self):
        assert pytest.approx(18.016, abs=0.001) == FATOR_GLICOSE_MMOLL_PARA_MGDL
        # Limiar do ABCDE (4,0 mmol/L) exibido como ≈ 72 mg/dL
        assert round(glicose_mmol_l_para_mg_dl(4.0)) == 72

    def test_kcl_19_1_porcento(self):
        # 191 mg/mL ÷ 74,55 mg/mmol = 2,562 mmol/mL
        assert mmol_por_ml_kcl(19.1) == pytest.approx(2.562, abs=0.001)

    def test_kcl_10_porcento(self):
        assert mmol_por_ml_kcl(10) == pytest.approx(1.341, abs=0.001)


class TestConversoes:
    @pytest.mark.parametrize(
        "valor, unidade, esperado",
        [(1, "g", 1_000_000), (1, "mg", 1_000), (250, "mcg", 250), (0.004, "g", 4_000)],
    )
    def test_massa_para_mcg(self, valor, unidade, esperado):
        assert massa_para_mcg(valor, unidade) == pytest.approx(esperado)

    def test_ida_e_volta(self):
        for unidade in ("g", "mg", "mcg"):
            assert mcg_para(massa_para_mcg(3.7, unidade), unidade) == pytest.approx(3.7)

    @pytest.mark.parametrize("funcao", [massa_para_mcg, mcg_para])
    def test_unidade_invalida(self, funcao):
        with pytest.raises(ValueError):
            funcao(1, "kg")

    def test_creatinina(self):
        assert creatinina_para_mg_dl(1.2, "mg/dL") == 1.2
        assert creatinina_para_mg_dl(88.4, "µmol/L") == pytest.approx(1.0, abs=0.001)
        with pytest.raises(ValueError):
            creatinina_para_mg_dl(1, "mmol/L")


class TestFormatacao:
    @pytest.mark.parametrize(
        "valor, casas, esperado",
        [
            (4200.5, 1, "4.200,5"),
            (0.1, 2, "0,10"),
            (26.25, 2, "26,25"),
            (131.25, 1, "131,3"),  # meio para cima, não bancário
            (2.675, 2, "2,68"),
            (-1234.5, 1, "-1.234,5"),
            (1_000_000, 0, "1.000.000"),
            (-0.0001, 2, "0,00"),
        ],
    )
    def test_fmt(self, valor, casas, esperado):
        assert fmt(valor, casas) == esperado

    @pytest.mark.parametrize("valor", [None, math.nan, math.inf, -math.inf, "abc", True])
    def test_fmt_valores_invalidos(self, valor):
        assert fmt(valor) == "—"

    @pytest.mark.parametrize("valor, esperado", [(4.0, "4"), (0.25, "0,25"), (16.0, "16"), (0.1, "0,1")])
    def test_fmt_auto(self, valor, esperado):
        assert fmt_auto(valor) == esperado
