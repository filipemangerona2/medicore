"""Integridade do conteúdo clínico: fontes, status, preservação do original e nada excluído em silêncio."""

import ast
from pathlib import Path

import pytest

from medicore.calculadoras_info import CALCULADORAS
from medicore.farmacos import FARMACOS
from medicore.fluxogramas import FLUXOGRAMAS
from medicore.referencias import REFERENCIAS, ROTULOS, Acesso
from medicore.status import RevisaoClinica, Status

RAIZ = Path(__file__).resolve().parent.parent
LEGADO = RAIZ / "legado"

MODULOS = list(FARMACOS) + list(FLUXOGRAMAS)


def _base_original_1292114() -> dict:
    linhas = (LEGADO / "app_original_1292114.txt").read_text(encoding="utf-8").splitlines()
    inicio = next(i for i, l in enumerate(linhas) if l.startswith("BASE_MEDICAMENTOS = {"))
    fim = next(i for i in range(inicio + 1, len(linhas) - 1) if linhas[i] == "}" and linhas[i + 1] == "}") + 1
    return ast.literal_eval("\n".join(linhas[inicio : fim + 1]).split("=", 1)[1])


class TestNadaFoiPerdido:
    def test_todos_os_farmacos_recuperados(self):
        originais = set(_base_original_1292114())
        nomes = {f.nome for f in FARMACOS}
        # Os 7 do original (com nomes revisados) + Midazolam da versão intermediária
        assert len(originais) == 7
        assert {f.id for f in FARMACOS} == {
            "noradrenalina", "adrenalina", "amiodarona", "ceftriaxona", "meropenem", "cetamina", "fentanil", "midazolam",
        }
        assert len(nomes) == 8

    def test_texto_original_preservado_campo_a_campo(self):
        base = _base_original_1292114()
        mapa = {
            "Noradrenalina": "noradrenalina",
            "Adrenalina (Epinefrina)": "adrenalina",
            "Amiodarona": "amiodarona",
            "Ceftriaxona": "ceftriaxona",
            "Meropenem": "meropenem",
            "Cetamina": "cetamina",
            "Fentanil": "fentanil",
        }
        por_id = {f.id: f for f in FARMACOS}
        for nome_original, farmaco_id in mapa.items():
            assert por_id[farmaco_id].original == base[nome_original], farmaco_id

    def test_midazolam_preserva_texto_da_versao_intermediaria(self):
        texto = (LEGADO / "app_intermediario_b161d85.txt").read_text(encoding="utf-8")
        midazolam = next(f for f in FARMACOS if f.id == "midazolam")
        for valor in midazolam.original.values():
            assert valor in texto

    def test_todos_os_fluxogramas_recuperados(self):
        assert {f.id for f in FLUXOGRAMAS} == {"pcr", "sri", "crise_hipertensiva", "anafilaxia", "sepse", "abcde"}

    @pytest.mark.parametrize(
        "trecho",
        [
            "Investigar 5 H's e 5 T's",
            "Os 7 Ps da SRI",
            "Distinguir Urgência",
            "Adrenalina IM imediata (0,01 mg/kg, máx 0,5 mg)",
            "Vasopressina (0.04 UI/min fixo)",
            "Hidrocortisona 200 mg/dia",
        ],
    )
    def test_trechos_originais_dos_fluxogramas_preservados(self, trecho):
        assert any(trecho in f.original for f in FLUXOGRAMAS)
        assert trecho in (LEGADO / "app_original_1292114.txt").read_text(encoding="utf-8")

    def test_todas_as_calculadoras_recuperadas(self):
        assert {c.id for c in CALCULADORAS} == {"infusao", "clcr", "superficie", "queimados", "potassio"}


class TestFontes:
    @pytest.mark.parametrize("modulo", MODULOS, ids=lambda m: m.id)
    def test_todo_item_tem_fonte_existente(self, modulo):
        for item in modulo.itens():
            assert item.refs, f"Item sem fonte em {modulo.id}: {item.texto[:60]}"
            for ref in item.refs:
                assert ref in REFERENCIAS, f"Referência inexistente {ref} em {modulo.id}"

    def test_alteracoes_e_calculadoras_usam_fontes_existentes(self):
        for modulo in list(MODULOS) + list(CALCULADORAS):
            for alteracao in modulo.alteracoes:
                for ref in alteracao.refs:
                    assert ref in REFERENCIAS
        for calc in CALCULADORAS:
            for ref in calc.refs:
                assert ref in REFERENCIAS

    def test_nenhuma_referencia_orfa(self):
        usadas = set()
        for modulo in MODULOS:
            usadas.update(modulo.referencias_usadas())
        for calc in CALCULADORAS:
            usadas.update(calc.refs)
            for alteracao in calc.alteracoes:
                usadas.update(alteracao.refs)
        assert set(REFERENCIAS) == usadas

    @pytest.mark.parametrize("ref", list(REFERENCIAS.values()), ids=lambda r: r.id)
    def test_registro_completo_da_referencia(self, ref):
        assert ref.instituicao and ref.titulo and ref.ano and ref.versao and ref.secao
        assert ref.url.startswith("https://")
        assert isinstance(ref.acesso, Acesso)
        assert ref.consultado_em == "2026-10-19"
        assert ref.id in ROTULOS

    def test_fontes_nao_lidas_sao_declaradas(self):
        assert REFERENCIAS["sbc2025_has"].acesso is Acesso.SOMENTE_IDENTIFICACAO
        assert REFERENCIAS["das2025"].acesso is Acesso.RESUMO_SECUNDARIO


class TestCriteriosDeLiberacao:
    def test_nada_validado_sem_revisao_clinica(self):
        for modulo in list(MODULOS) + list(CALCULADORAS):
            if modulo.status is Status.VALIDADO:
                revisao = getattr(modulo, "revisao", None)
                assert isinstance(revisao, RevisaoClinica) and revisao.esta_completa(), modulo.id
            for item in getattr(modulo, "itens", lambda: ())():
                assert item.status is not Status.VALIDADO, "Item VALIDADO exige revisão clínica do módulo"

    def test_estado_atual_nenhum_validado(self):
        # Conteúdo recuperado não vira VALIDADO automaticamente
        assert all(m.status is Status.PENDENTE for m in list(MODULOS) + list(CALCULADORAS))

    def test_revisao_clinica_incompleta(self):
        assert not RevisaoClinica("", "CRM-SP 1", "2026-10-19").esta_completa()
        assert RevisaoClinica("Dra. Fulana", "CRM-SP 1", "2026-10-19").esta_completa()

    @pytest.mark.parametrize("modulo", list(MODULOS) + list(CALCULADORAS), ids=lambda m: m.id)
    def test_bloqueados_tem_motivo_e_origem(self, modulo):
        for bloqueado in modulo.bloqueados:
            assert bloqueado.motivo and bloqueado.texto_original and bloqueado.origem

    @pytest.mark.parametrize("modulo", list(MODULOS) + list(CALCULADORAS), ids=lambda m: m.id)
    def test_pendencias_declaradas(self, modulo):
        # Todo módulo com conteúdo clínico tem pendências registradas, exceto fórmulas puramente matemáticas
        if modulo.id != "superficie":
            assert modulo.pendencias


class TestTextoSeguro:
    def test_textos_exibidos_nao_reproduzem_trechos_bloqueados(self):
        for modulo in MODULOS:
            exibidos = " ".join(i.texto for i in modulo.itens())
            for bloqueado in modulo.bloqueados:
                assert bloqueado.texto_original not in exibidos

    def test_sem_alegacoes_falsas_da_versao_original(self):
        exibidos = " ".join(i.texto for m in MODULOS for i in m.itens())
        for alegacao in ("Validação Automática", "Sem Erros", "WHITEBOOK", "99,2", "99.2"):
            assert alegacao not in exibidos

    def test_unidade_de_compressao_corrigida(self):
        pcr = next(f for f in FLUXOGRAMAS if f.id == "pcr")
        assert "bpm" not in " ".join(i.texto for i in pcr.etapas[0].itens)
