"""Busca real (substitui a aba 'RAG' simulada)."""

import dataclasses

import pytest

from medicore.busca import ResultadoBusca, buscar, indice, normalizar, termos_da_consulta
from medicore.farmacos import FARMACOS
from medicore.fluxogramas import FLUXOGRAMAS


def test_normalizar_remove_acentos_e_simbolos():
    assert normalizar("Meropeném — ClCr < 50!") == "meropenem clcr 50"
    assert normalizar("PaO₂/FiO₂") == "pao2 fio2"


def test_termos_ignoram_palavras_vazias_e_repeticoes():
    assert termos_da_consulta("o choque e a sepse da sepse") == ("choque", "sepse")


def test_busca_por_nome_com_e_sem_acento():
    for consulta in ("meropeném", "MEROPENEM", "meropenem"):
        resultados = buscar(consulta)
        assert resultados
        assert "Meropeném" in resultados[0].documento.titulo


def test_busca_por_prefixo():
    assert any("Adrenalina" in r.documento.titulo for r in buscar("adrenal"))


def test_varios_termos_priorizam_documentos_com_todos():
    resultados = buscar("choque séptico vasopressina")
    assert resultados
    primeiro = resultados[0]
    assert primeiro.documento.titulo.startswith("Sepse")
    assert len(primeiro.termos_encontrados) == primeiro.total_termos == 3


def test_hipercalemia_encontra_calculadora_de_potassio():
    assert any(r.documento.tipo == "Calculadora" and "Potássio" in r.documento.titulo for r in buscar("hipercalemia"))


def test_resultado_nao_tem_pontuacao_inventada():
    campos = {f.name for f in dataclasses.fields(ResultadoBusca)}
    assert campos == {"documento", "termos_encontrados", "total_termos", "trecho"}


@pytest.mark.parametrize("consulta", ["", "   ", "o a de", "x", None, 123, "xyzqwv"])
def test_consultas_sem_resultado(consulta):
    assert buscar(consulta) == ()


@pytest.mark.parametrize("consulta", ["(.*)", "[", "\\", "a" * 10_000, "😀 choque", "' OR 1=1 --"])
def test_consultas_estranhas_nao_quebram(consulta):
    assert isinstance(buscar(consulta), tuple)


def test_limite_de_resultados():
    assert len(buscar("dose", limite=3)) <= 3


def test_indice_nao_contem_texto_original_bloqueado():
    textos = " ".join(d.texto for d in indice())
    for modulo in list(FARMACOS) + list(FLUXOGRAMAS):
        for bloqueado in modulo.bloqueados:
            assert bloqueado.texto_original not in textos


def test_bloqueado_aparece_com_motivo():
    resultados = buscar("hidrocortisona")
    assert any(r.documento.tipo == "Bloqueado" for r in resultados)
