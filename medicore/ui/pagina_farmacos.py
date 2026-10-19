"""Aba: guia de fármacos."""

from __future__ import annotations

import streamlit as st

from ..busca import normalizar
from ..farmacos import FARMACOS
from . import componentes as c


def _filtrar(consulta: str):
    termo = normalizar(consulta or "")
    if not termo:
        return list(FARMACOS)
    return [f for f in FARMACOS if termo in normalizar(f"{f.nome} {f.classe}")]


def render() -> None:
    st.subheader("💊 Guia de fármacos")
    st.caption("Conteúdo auditado em 19/10/2026 com bulas e diretrizes rastreáveis. Cada item mostra a fonte entre colchetes.")

    consulta = st.text_input(
        "Filtrar por nome ou classe",
        placeholder="Ex.: noradrenalina, antibiótico, opioide",
        key="farmaco_filtro",
    )
    opcoes = _filtrar(consulta)
    if not opcoes:
        st.info("Nenhum fármaco do guia corresponde ao filtro. Mostrando a lista completa.")
        opcoes = list(FARMACOS)

    nomes = [f.nome for f in opcoes]
    escolhido = st.selectbox("Fármaco", nomes, key="farmaco_escolhido")
    farmaco = next(f for f in opcoes if f.nome == escolhido)

    st.markdown(f"### {farmaco.nome}")
    st.caption(farmaco.classe)
    c.selo_status(farmaco.status)
    for alerta in farmaco.alertas_principais:
        st.error(f"⚠️ {alerta}")

    for indice, secao in enumerate(farmaco.secoes):
        with st.expander(secao.titulo, expanded=indice < 2):
            c.lista_itens(secao.itens)

    c.lista_bloqueados(farmaco.bloqueados)
    c.lista_pendencias(farmaco.pendencias)
    c.lista_referencias(farmaco.referencias_usadas())
