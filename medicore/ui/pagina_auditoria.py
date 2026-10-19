"""Aba: auditoria — critérios de liberação, resumo por módulo e fontes."""

from __future__ import annotations

import streamlit as st

from .. import DATA_AUDITORIA, __version__
from ..auditoria import FONTES_NAO_ACESSADAS, LIMITACOES, PROBLEMAS_TECNICOS
from ..calculadoras_info import CALCULADORAS
from ..farmacos import FARMACOS
from ..fluxogramas import FLUXOGRAMAS
from ..referencias import REFERENCIAS, Acesso
from ..status import DESCRICAO_STATUS, Status, rotulo_status
from . import componentes as c

URL_RELATORIO = "https://github.com/filipemangerona2/medicore/blob/main/docs/AUDITORIA.md"


def render() -> None:
    st.subheader("📋 Auditoria e critérios de liberação")
    st.caption(f"Versão {__version__} · auditoria de {DATA_AUDITORIA}")

    st.markdown("**Critérios de liberação**")
    st.markdown("\n".join(f"- **{rotulo_status(s)}** — {DESCRICAO_STATUS[s]}" for s in Status))
    st.info(
        "Nenhum conteúdo está VALIDADO: a revisão clínica por profissional habilitado ainda não foi feita. "
        "Trechos bloqueados não aparecem como orientação no aplicativo."
    )

    modulos = (
        [("Fármaco", f.nome, f.status, len(f.bloqueados), len(f.pendencias)) for f in FARMACOS]
        + [("Fluxograma", f.titulo, f.status, len(f.bloqueados), len(f.pendencias)) for f in FLUXOGRAMAS]
        + [("Calculadora", k.titulo, k.status, len(k.bloqueados), len(k.pendencias)) for k in CALCULADORAS]
    )
    st.markdown("**Situação por módulo**")
    st.markdown(
        "\n".join(
            f"- {tipo}: **{nome}** — {rotulo_status(status)} · {bloq} trecho(s) bloqueado(s) · {pend} pendência(s)"
            for tipo, nome, status, bloq, pend in modulos
        )
    )
    st.markdown(f"Relatório completo, com o texto original de cada módulo e o motivo de cada alteração: [docs/AUDITORIA.md]({URL_RELATORIO})")

    with st.expander(f"🛠️ Problemas técnicos corrigidos ({len(PROBLEMAS_TECNICOS)})"):
        st.markdown("\n".join(f"- **{p.problema}** ({p.onde}) → {p.correcao}" for p in PROBLEMAS_TECNICOS))
    with st.expander(f"⚖️ Limitações desta auditoria ({len(LIMITACOES)})"):
        st.markdown("\n".join(f"- {texto}" for texto in LIMITACOES))
    with st.expander(f"🚫 Fontes procuradas e não acessadas ({len(FONTES_NAO_ACESSADAS)})"):
        st.markdown("\n".join(f"- **{fonte}:** {motivo}" for fonte, motivo in FONTES_NAO_ACESSADAS))

    contagem = {a: sum(1 for r in REFERENCIAS.values() if r.acesso is a) for a in Acesso}
    st.markdown("**Fontes por nível de acesso**")
    st.markdown("\n".join(f"- {a.value}: {n}" for a, n in contagem.items() if n))
    c.lista_referencias(REFERENCIAS.keys(), titulo="📚 Todas as fontes consultadas")
