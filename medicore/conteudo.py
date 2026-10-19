"""Estruturas de dados do conteúdo clínico (fármacos e fluxogramas).

Cada conteúdo guarda, além do texto revisado com fontes:

* ``original`` — o texto clínico recuperado das versões anteriores, campo a campo;
* ``alteracoes`` — o que mudou, por quê e com base em qual fonte;
* ``bloqueados`` — trechos originais sem fonte verificável ou com risco, que NÃO são
  exibidos como orientação (apenas o motivo do bloqueio aparece no aplicativo);
* ``pendencias`` — o que ainda exige decisão ou revisão humana.

Assim nada é excluído silenciosamente.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .status import RevisaoClinica, Status


@dataclass(frozen=True)
class Item:
    texto: str
    refs: tuple[str, ...]
    status: Status = Status.PENDENTE
    alerta: bool = False  # destaque visual de segurança


@dataclass(frozen=True)
class Secao:
    titulo: str
    itens: tuple[Item, ...]


@dataclass(frozen=True)
class ItemBloqueado:
    titulo: str
    texto_original: str
    origem: str
    motivo: str


@dataclass(frozen=True)
class Alteracao:
    campo: str
    antes: str
    depois: str
    motivo: str
    refs: tuple[str, ...] = ()


@dataclass(frozen=True)
class Farmaco:
    id: str
    nome: str
    classe: str
    status: Status
    alertas_principais: tuple[str, ...]
    secoes: tuple[Secao, ...]
    bloqueados: tuple[ItemBloqueado, ...]
    alteracoes: tuple[Alteracao, ...]
    original: dict
    origem_original: str
    pendencias: tuple[str, ...]
    revisao: Optional[RevisaoClinica] = None

    def itens(self) -> tuple[Item, ...]:
        return tuple(item for secao in self.secoes for item in secao.itens)

    def referencias_usadas(self) -> tuple[str, ...]:
        vistos: list[str] = []
        for item in self.itens():
            for ref in item.refs:
                if ref not in vistos:
                    vistos.append(ref)
        for alt in self.alteracoes:
            for ref in alt.refs:
                if ref not in vistos:
                    vistos.append(ref)
        return tuple(vistos)


@dataclass(frozen=True)
class Etapa:
    titulo: str
    itens: tuple[Item, ...]


@dataclass(frozen=True)
class Fluxograma:
    id: str
    titulo: str
    publico: str
    status: Status
    etapas: tuple[Etapa, ...]
    bloqueados: tuple[ItemBloqueado, ...]
    alteracoes: tuple[Alteracao, ...]
    original: str
    origem_original: str
    pendencias: tuple[str, ...]
    divergencias: tuple[str, ...] = field(default=())
    revisao: Optional[RevisaoClinica] = None

    def itens(self) -> tuple[Item, ...]:
        return tuple(item for etapa in self.etapas for item in etapa.itens)

    def referencias_usadas(self) -> tuple[str, ...]:
        vistos: list[str] = []
        for item in self.itens():
            for ref in item.refs:
                if ref not in vistos:
                    vistos.append(ref)
        for alt in self.alteracoes:
            for ref in alt.refs:
                if ref not in vistos:
                    vistos.append(ref)
        return tuple(vistos)


def I(texto: str, *refs: str, alerta: bool = False) -> Item:  # noqa: E743 - atalho de leitura
    """Atalho para declarar itens de conteúdo com suas referências."""
    return Item(texto=texto, refs=tuple(refs), alerta=alerta)
