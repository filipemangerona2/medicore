"""Cockcroft-Gault e ajustes renais de bula."""

import math

import pytest

from medicore import calculos as calc
from medicore.calculos import EntradaInvalida


def cg(idade=45, peso=70, scr=1.0, unidade="mg/dL", sexo="masculino"):
    return calc.clcr_cockcroft_gault(idade, peso, scr, unidade, sexo)


class TestFormula:
    def test_homem_referencia(self):
        # (140 − 45) × 70 ÷ (72 × 1,0) = 6650 ÷ 72 = 92,36 mL/min
        assert cg().valor == pytest.approx(6650 / 72)

    def test_mulher_fator_0_85(self):
        assert cg(sexo="feminino").valor == pytest.approx(6650 / 72 * 0.85)

    def test_exemplo_independente_idosa(self):
        # (140 − 80) × 60 ÷ (72 × 1,2) × 0,85 = 3600 ÷ 86,4 × 0,85 = 35,42 mL/min
        assert cg(80, 60, 1.2, sexo="F").valor == pytest.approx(35.4167, abs=1e-3)

    def test_creatinina_em_micromol(self):
        r = cg(scr=88.4, unidade="µmol/L")
        assert r.valor == pytest.approx(92.36, abs=0.05)
        assert any("µmol/L" in p for p in r.passos)

    def test_proporcionalidade(self):
        # Dobrar a creatinina reduz o ClCr pela metade; dobrar o peso dobra o ClCr
        assert cg(scr=2.0).valor == pytest.approx(cg().valor / 2)
        assert cg(peso=140).valor == pytest.approx(cg().valor * 2)

    def test_referencia_da_formula(self):
        assert cg().referencias == ("cockcroft1976",)

    @pytest.mark.parametrize("sexo", ["M", "m", "Masculino", " masculino ", "masc"])
    def test_variacoes_de_sexo_masculino(self, sexo):
        assert cg(sexo=sexo).valor == pytest.approx(6650 / 72)

    @pytest.mark.parametrize("sexo", ["F", "f", "Feminino", "fem"])
    def test_variacoes_de_sexo_feminino(self, sexo):
        assert cg(sexo=sexo).valor == pytest.approx(6650 / 72 * 0.85)


class TestLimitesEAlertas:
    def test_idade_minima_18(self):
        assert cg(idade=18).valor > 0
        for idade in (17.9, 0, -1):
            with pytest.raises(EntradaInvalida):
                cg(idade=idade)

    def test_idade_maxima_120_e_alerta_acima_de_92(self):
        r = cg(idade=93)
        assert any("18 a 92" in a for a in r.alertas)
        assert not any("18 a 92" in a for a in cg(idade=92).alertas)
        assert cg(idade=120).valor > 0
        with pytest.raises(EntradaInvalida):
            cg(idade=121)

    def test_alerta_de_peso_em_obesidade_sempre_presente(self):
        assert any("obesidade" in a for a in cg().alertas)

    def test_alerta_de_unidade_trocada(self):
        assert any("µmol/L" in a for a in cg(scr=21).alertas)  # mg/dL alto demais
        assert any("mg/dL" in a for a in cg(scr=15, unidade="µmol/L").alertas)  # µmol/L baixo demais

    @pytest.mark.parametrize("scr", [0.09, 25.1, 0, -1, math.nan])
    def test_creatinina_fora_da_faixa_mg_dl(self, scr):
        with pytest.raises(EntradaInvalida):
            cg(scr=scr)

    @pytest.mark.parametrize("scr", [8.0, 2300])
    def test_creatinina_fora_da_faixa_umol(self, scr):
        with pytest.raises(EntradaInvalida):
            cg(scr=scr, unidade="µmol/L")

    @pytest.mark.parametrize("peso", [19.9, 350.1, None, "70"])
    def test_peso_invalido(self, peso):
        with pytest.raises(EntradaInvalida):
            cg(peso=peso)

    @pytest.mark.parametrize("sexo", ["x", "", None, 1])
    def test_sexo_invalido(self, sexo):
        with pytest.raises(EntradaInvalida):
            cg(sexo=sexo)

    def test_unidade_invalida(self):
        with pytest.raises(EntradaInvalida):
            cg(unidade="mmol/L")


class TestAjustesRenaisDeBula:
    def texto(self, clcr, farmaco):
        return next(a.texto for a in calc.ajustes_renais(clcr) if a.farmaco == farmaco)

    @pytest.mark.parametrize(
        "clcr, trecho",
        [
            (120, "não prevê ajuste"),
            (51, "não prevê ajuste"),
            (50.9, "26–50"),
            (26, "26–50"),
            (25.9, "10–25"),
            (10, "10–25"),
            (9.99, "< 10"),
            (0, "< 10"),
        ],
    )
    def test_faixas_do_meropenem(self, clcr, trecho):
        assert trecho in self.texto(clcr, "Meropeném")

    def test_ceftriaxona_limite_de_2_g_abaixo_de_10(self):
        assert "2 g" in self.texto(9.9, "Ceftriaxona")
        assert "Sem redução" in self.texto(10, "Ceftriaxona")

    def test_todos_os_ajustes_tem_fonte(self):
        for ajuste in calc.ajustes_renais(30):
            assert ajuste.referencias

    @pytest.mark.parametrize("clcr", [-1, math.nan, None, 1001])
    def test_clcr_invalido(self, clcr):
        with pytest.raises(EntradaInvalida):
            calc.ajustes_renais(clcr)
