"""Aba: busca real no conteúdo do aplicativo."""

from __future__ import annotations

import streamlit as st

from ..busca import buscar
from ..status import rotulo_status


def render() -> None:
    st.subheader("🔎 Busca no conteúdo")
    st.caption(
        "Busca textual em fármacos, fluxogramas, calculadoras e fontes deste aplicativo. Não é um sistema de "
        "inteligência artificial e não consulta a internet."
    )
    consulta = st.text_input(
        "O que você procura?",
        placeholder="Ex.: choque séptico vasopressina, hipercalemia, meropeném renal",
        key="busca_consulta",
    )
    if not consulta or not consulta.strip():
        return
    resultados = buscar(consulta)
    if not resultados:
        st.info("Nenhum conteúdo encontrado. Tente outros termos (a busca ignora acentos e maiúsculas).")
        return
    st.caption(f"{len(resultados)} resultado(s).")
    for r in resultados:
        doc = r.documento
        st.markdown(
            f"**{doc.titulo}**  \n"
            f"{doc.tipo} · aba *{doc.onde}* · {rotulo_status(doc.status)} · "
            f"termos encontrados: {len(r.termos_encontrados)} de {r.total_termos}"
        )
        st.caption(r.trecho)
