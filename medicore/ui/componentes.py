"""Componentes visuais reutilizados pelas páginas."""

from __future__ import annotations

from collections.abc import Iterable

import streamlit as st

from ..conteudo import Item, ItemBloqueado
from ..referencias import REFERENCIAS, rotulo
from ..status import DESCRICAO_STATUS, Status, rotulo_status

AVISO_GERAL = (
    "Protótipo em revisão. Todo o conteúdo está, no máximo, **PENDENTE DE REVISÃO CLÍNICA**: não usar para "
    "prescrição nem para decisão assistencial. Confira sempre a bula vigente e o protocolo da sua instituição."
)


def selo_status(status: Status) -> None:
    texto = f"**{rotulo_status(status)}** — {DESCRICAO_STATUS[status]}"
    if status is Status.BLOQUEADO:
        st.error(texto)
    elif status is Status.PENDENTE:
        st.warning(texto)
    else:
        st.success(texto)


def _sufixo_fontes(refs: Iterable[str]) -> str:
    rotulos = [rotulo(r) for r in refs]
    return f" *[{'; '.join(rotulos)}]*" if rotulos else ""


def lista_itens(itens: Iterable[Item]) -> None:
    linhas = []
    for item in itens:
        if item.status is Status.BLOQUEADO:  # nunca exibir conteúdo bloqueado como orientação
            continue
        marcador = "⚠️ " if item.alerta else ""
        linhas.append(f"- {marcador}{item.texto}{_sufixo_fontes(item.refs)}")
    if linhas:
        st.markdown("\n".join(linhas))


def lista_bloqueados(bloqueados: Iterable[ItemBloqueado]) -> None:
    bloqueados = tuple(bloqueados)
    if not bloqueados:
        return
    with st.expander(f"🔴 Trechos bloqueados nesta versão ({len(bloqueados)})"):
        st.caption("O texto original fica preservado no relatório de auditoria; aqui aparece apenas o motivo do bloqueio.")
        st.markdown("\n".join(f"- **{b.titulo}:** {b.motivo}" for b in bloqueados))


def lista_pendencias(pendencias: Iterable[str]) -> None:
    pendencias = tuple(pendencias)
    if pendencias:
        with st.expander(f"📝 Pendências para revisão humana ({len(pendencias)})"):
            st.markdown("\n".join(f"- {p}" for p in pendencias))


def lista_referencias(ids: Iterable[str], titulo: str = "📚 Fontes consultadas") -> None:
    ids = [i for i in dict.fromkeys(ids) if i in REFERENCIAS]
    if not ids:
        return
    with st.expander(f"{titulo} ({len(ids)})"):
        for ref_id in ids:
            ref = REFERENCIAS[ref_id]
            partes = [f"**{rotulo(ref_id)}** — {ref.instituicao}. *{ref.titulo}* ({ref.ano}). {ref.versao}."]
            if ref.doi:
                partes.append(f"DOI {ref.doi}.")
            partes.append(f"Seção: {ref.secao}. Acesso: {ref.acesso.value}.")
            if ref.observacao:
                partes.append(ref.observacao)
            partes.append(f"[Abrir fonte]({ref.url}) · consultado em {ref.consultado_em}")
            st.markdown(" ".join(partes))


def passos(passos_calculo: Iterable[str]) -> None:
    passos_calculo = tuple(passos_calculo)
    if passos_calculo:
        with st.expander("🧮 Como foi calculado"):
            st.markdown("\n".join(f"{i}. {p}" for i, p in enumerate(passos_calculo, start=1)))


def alertas(textos: Iterable[str]) -> None:
    for texto in textos:
        st.warning(texto)
