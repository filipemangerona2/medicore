"""Testes de execução da interface com o Streamlit real (streamlit.testing.v1.AppTest).

Rodam o app.py de verdade: inicialização, navegação, cada fármaco e fluxograma, cada
calculadora com valores de referência, busca, mensagens de erro e ausência de conteúdo
bloqueado na tela.
"""

from __future__ import annotations

from pathlib import Path

import pytest

st_testing = pytest.importorskip("streamlit.testing.v1")
AppTest = st_testing.AppTest

from medicore.farmacos import FARMACOS  # noqa: E402
from medicore.fluxogramas import FLUXOGRAMAS  # noqa: E402

APP = str(Path(__file__).resolve().parent.parent / "app.py")


def novo_app() -> AppTest:
    at = AppTest.from_file(APP, default_timeout=90)
    at.run()
    return at


def com_ciencia() -> AppTest:
    at = novo_app()
    at.checkbox(key="ciencia").check().run()
    assert not at.exception, [e.value for e in at.exception]
    return at


def textos(at) -> str:
    partes = []
    for colecao in (at.title, at.subheader, at.markdown, at.caption, at.info, at.warning, at.error, at.success):
        partes.extend(str(el.value) for el in colecao)
    return "\n".join(partes)


def metricas(at) -> dict:
    return {m.label: m.value for m in at.metric}


# --------------------------------------------------------------------------- inicialização


def test_inicia_sem_erros_e_exige_ciencia():
    at = novo_app()
    assert not at.exception
    assert len(at.tabs) == 0  # nada clínico antes da declaração
    assert "Marque a declaração" in textos(at)


def test_abas_aparecem_apos_ciencia():
    at = com_ciencia()
    rotulos = [t.label for t in at.tabs]
    for esperado in ("💊 Fármacos", "🧮 Calculadoras", "🔀 Fluxogramas", "🔎 Busca", "📋 Auditoria"):
        assert esperado in rotulos
    for sub in ("Infusão", "Função renal", "Superfície corporal", "Queimados", "Potássio"):
        assert sub in rotulos


def test_campos_do_paciente_sem_valor_padrao():
    at = com_ciencia()
    for chave in ("peso_kg", "altura_cm", "idade_anos", "creatinina"):
        assert at.number_input(key=chave).value is None
    assert at.selectbox(key="sexo").value is None
    assert not metricas(at)  # nenhuma conta feita com valores presumidos


# --------------------------------------------------------------------------- conteúdo


def test_todos_os_farmacos_renderizam():
    at = com_ciencia()
    opcoes = at.selectbox(key="farmaco_escolhido").options
    assert len(opcoes) == len(FARMACOS)
    for nome in opcoes:
        at.selectbox(key="farmaco_escolhido").set_value(nome).run()
        assert not at.exception, nome
        texto = textos(at)
        assert nome in texto
        assert "PENDENTE DE REVISÃO CLÍNICA" in texto


def test_filtro_de_farmacos():
    at = com_ciencia()
    at.text_input(key="farmaco_filtro").input("antibiótico").run()
    assert set(at.selectbox(key="farmaco_escolhido").options) == {"Ceftriaxona", "Meropeném"}
    at.text_input(key="farmaco_filtro").input("inexistente").run()
    assert len(at.selectbox(key="farmaco_escolhido").options) == len(FARMACOS)


def test_todos_os_fluxogramas_renderizam():
    at = com_ciencia()
    opcoes = at.selectbox(key="fluxo_escolhido").options
    assert len(opcoes) == len(FLUXOGRAMAS)
    for titulo in opcoes:
        at.selectbox(key="fluxo_escolhido").set_value(titulo).run()
        assert not at.exception, titulo
        assert titulo in textos(at)


def test_conteudo_bloqueado_nunca_aparece_na_tela():
    at = com_ciencia()
    exibido = []
    for nome in at.selectbox(key="farmaco_escolhido").options:
        at.selectbox(key="farmaco_escolhido").set_value(nome).run()
        exibido.append(textos(at))
    for titulo in at.selectbox(key="fluxo_escolhido").options:
        at.selectbox(key="fluxo_escolhido").set_value(titulo).run()
        exibido.append(textos(at))
    tela = "\n".join(exibido)
    for modulo in list(FARMACOS) + list(FLUXOGRAMAS):
        for bloqueado in modulo.bloqueados:
            assert bloqueado.texto_original not in tela, bloqueado.titulo
            assert bloqueado.motivo in tela  # o motivo do bloqueio é mostrado


def test_abas_clinicas_sem_alegacoes_falsas():
    # A aba Auditoria descreve as alegações removidas; as abas clínicas não podem contê-las.
    at = com_ciencia()
    abas_clinicas = [t for t in at.tabs if t.label in ("💊 Fármacos", "🧮 Calculadoras", "🔀 Fluxogramas")]
    assert len(abas_clinicas) == 3
    tela = "\n".join(textos(aba) for aba in abas_clinicas)
    assert "PENDENTE DE REVISÃO CLÍNICA" in tela
    for alegacao in ("Validação Automática Ativa", "Sem Erros", "Relevância RAG", "Whitebook", "99,2"):
        assert alegacao not in tela


def test_componente_nunca_renderiza_item_bloqueado():
    def script():
        from medicore.conteudo import Item
        from medicore.status import Status
        from medicore.ui.componentes import lista_itens

        lista_itens(
            [
                Item("TEXTO-PERMITIDO", ("ssc2026",)),
                Item("TEXTO-BLOQUEADO", ("ssc2026",), status=Status.BLOQUEADO),
            ]
        )

    at = AppTest.from_function(script, default_timeout=30).run()
    assert not at.exception
    tela = " ".join(m.value for m in at.markdown)
    assert "TEXTO-PERMITIDO" in tela
    assert "TEXTO-BLOQUEADO" not in tela


def test_aba_auditoria():
    at = com_ciencia()
    texto = textos(at)
    assert "Nenhum conteúdo está VALIDADO" in texto
    assert "docs/AUDITORIA.md" in texto


# --------------------------------------------------------------------------- calculadoras


def preencher_infusao(at, qtd=4.0, unidade_qtd="mg", volume=250.0):
    at.number_input(key="inf_qtd").set_value(qtd)
    at.selectbox(key="inf_un_qtd").set_value(unidade_qtd)
    at.number_input(key="inf_vol").set_value(volume)


def test_infusao_vazao():
    at = com_ciencia()
    at.number_input(key="peso_kg").set_value(70.0)
    preencher_infusao(at)
    at.number_input(key="inf_dose").set_value(0.1)
    at.run()
    assert not at.exception
    assert metricas(at)["Vazão na bomba"] == "26,25 mL/h"


def test_infusao_dose_pela_vazao():
    at = com_ciencia()
    at.number_input(key="peso_kg").set_value(70.0)
    at.radio(key="inf_modo").set_value("Dose a partir da vazão (mL/h)").run()
    preencher_infusao(at)
    at.number_input(key="inf_vazao").set_value(26.25)
    at.run()
    assert metricas(at)["Dose infundida"] == "0,1 mcg/kg/min"


def test_infusao_por_kg_sem_peso_pede_peso():
    at = com_ciencia()
    preencher_infusao(at)
    at.number_input(key="inf_dose").set_value(0.1)
    at.run()
    assert "Vazão na bomba" not in metricas(at)
    assert "informe o peso" in textos(at)


def test_infusao_unidades_incompativeis():
    at = com_ciencia()
    preencher_infusao(at)
    at.selectbox(key="inf_unidade_dose").set_value("UI/min")
    at.number_input(key="inf_dose").set_value(0.03)
    at.run()
    assert not at.exception
    assert any("incompatíveis" in e.value for e in at.error)


def test_infusao_concentracao_direta_vasopressina():
    at = com_ciencia()
    at.radio(key="inf_forma_conc").set_value("Concentração já calculada").run()
    at.number_input(key="inf_conc").set_value(0.1)
    at.selectbox(key="inf_conc_un").set_value("UI/mL")
    at.selectbox(key="inf_unidade_dose").set_value("UI/min")
    at.number_input(key="inf_dose").set_value(0.01)
    at.run()
    assert metricas(at)["Vazão na bomba"] == "6,00 mL/h"


def test_conversor_noradrenalina_sal_base():
    at = com_ciencia()
    at.number_input(key="nora_sal").set_value(8.0).run()
    assert metricas(at)["Norepinefrina base"] == "4 mg"


def test_clearance_de_creatinina():
    at = com_ciencia()
    at.number_input(key="idade_anos").set_value(45)
    at.number_input(key="peso_kg").set_value(70.0)
    at.selectbox(key="sexo").set_value("Masculino")
    at.number_input(key="creatinina").set_value(1.0)
    at.run()
    assert metricas(at)["ClCr estimado (Cockcroft-Gault)"] == "92,4 mL/min"
    assert "Meropeném" in textos(at)


def test_clearance_em_micromol_e_feminino():
    at = com_ciencia()
    at.number_input(key="idade_anos").set_value(45)
    at.number_input(key="peso_kg").set_value(70.0)
    at.selectbox(key="sexo").set_value("Feminino")
    at.radio(key="unidade_creatinina").set_value("µmol/L")
    at.number_input(key="creatinina").set_value(88.4)
    at.run()
    assert metricas(at)["ClCr estimado (Cockcroft-Gault)"] == "78,5 mL/min"


def test_clearance_recusa_menor_de_18():
    at = com_ciencia()
    at.number_input(key="idade_anos").set_value(16)
    at.number_input(key="peso_kg").set_value(50.0)
    at.selectbox(key="sexo").set_value("Feminino")
    at.number_input(key="creatinina").set_value(0.7)
    at.run()
    assert not at.exception
    assert any("no mínimo 18" in e.value for e in at.error)


def test_superficie_corporal():
    at = com_ciencia()
    at.number_input(key="peso_kg").set_value(70.0)
    at.number_input(key="altura_cm").set_value(170.0)
    at.run()
    m = metricas(at)
    assert m["Mosteller"] == "1,82 m²"
    assert m["DuBois"] == "1,81 m²"


def test_queimados_parkland_e_aba():
    at = com_ciencia()
    at.number_input(key="peso_kg").set_value(70.0)
    at.number_input(key="q_pct").set_value(15.0)
    at.run()
    m = metricas(at)
    assert m["Volume estimado em 24 h"] == "4.200 mL"
    assert m["Primeiras 8 h"] == "262,5 mL/h"
    assert m["16 h seguintes"] == "131,3 mL/h"
    at.radio(key="q_fator").set_value(2.0).run()
    assert metricas(at)["Volume estimado em 24 h"] == "2.100 mL"


def test_potassio_hipercalemia_nao_e_segura():
    at = com_ciencia()
    at.number_input(key="k_serico").set_value(7.0).run()
    assert any("Hipercalemia grave" in e.value for e in at.error)
    assert "faixa segura" not in textos(at)


def test_potassio_conferencia_de_infusao():
    at = com_ciencia()
    at.number_input(key="kcl_mmol").set_value(40.0)
    at.number_input(key="kcl_volume").set_value(1000.0)
    at.number_input(key="kcl_vazao").set_value(250.0)
    at.run()
    m = metricas(at)
    assert m["Concentração"] == "40,0 mmol/L"
    assert m["Velocidade"] == "10,0 mmol/h"
    assert any("Dentro dos limites" in s.value for s in at.success)
    at.number_input(key="kcl_vazao").set_value(600.0).run()
    assert any("20 mmol/h" in e.value for e in at.error)


def test_potassio_volume_de_concentrado():
    at = com_ciencia()
    at.number_input(key="kcl_desejado").set_value(20.0)
    at.number_input(key="kcl_conc_ampola").set_value(2.562)
    at.run()
    assert metricas(at)["Volume da solução concentrada"] == "7,81 mL"


# --------------------------------------------------------------------------- busca


def test_busca_encontra_conteudo():
    at = com_ciencia()
    at.text_input(key="busca_consulta").input("choque séptico vasopressina").run()
    assert not at.exception
    texto = textos(at)
    assert "Sepse e choque séptico" in texto
    assert "termos encontrados: 3 de 3" in texto


def test_busca_sem_resultado():
    at = com_ciencia()
    at.text_input(key="busca_consulta").input("xyzqwv").run()
    assert "Nenhum conteúdo encontrado" in textos(at)
