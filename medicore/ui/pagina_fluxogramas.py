"""Aba: fluxogramas de urgência."""

from __future__ import annotations

import streamlit as st

from ..fluxogramas import FLUXOGRAMAS
from . import componentes as c


def render() -> None:
    st.subheader("🔀 Fluxogramas de urgência")
    st.caption("Sequências revisadas com diretrizes verificáveis. Itens com ⚠️ são pontos críticos de segurança.")

    titulos = [f.titulo for f in FLUXOGRAMAS]
    escolhido = st.selectbox("Fluxograma", titulos, key="fluxo_escolhido")
    fluxo = next(f for f in FLUXOGRAMAS if f.titulo == escolhido)

    st.markdown(f"### {fluxo.titulo}")
    st.caption(f"Público: {fluxo.publico}")
    c.selo_status(fluxo.status)

    for divergencia in fluxo.divergencias:
        st.info(f"ℹ️ {divergencia}")

    for etapa in fluxo.etapas:
        st.markdown(f"#### {etapa.titulo}")
        c.lista_itens(etapa.itens)

    c.lista_bloqueados(fluxo.bloqueados)
    c.lista_pendencias(fluxo.pendencias)
    c.lista_referencias(fluxo.referencias_usadas())
