"""Critérios de liberação do conteúdo clínico.

Definidos pelo responsável pelo projeto:

* VALIDADO — conferido com fontes verificáveis, cálculos testados quando aplicável e
  revisão clínica concluída por profissional habilitado.
* PENDENTE DE REVISÃO CLÍNICA — tecnicamente revisado, com fonte rastreável, mas ainda
  sem aprovação de profissional habilitado.
* BLOQUEADO — erro relevante, informação insuficiente ou potencial de causar dano.
  Fica indisponível no aplicativo até a correção e a aprovação.

Conteúdo recuperado nunca vira VALIDADO automaticamente: o status VALIDADO exige um
registro de revisão clínica (``RevisaoClinica``), verificado pelos testes automatizados.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Status(str, Enum):
    VALIDADO = "VALIDADO"
    PENDENTE = "PENDENTE DE REVISÃO CLÍNICA"
    BLOQUEADO = "BLOQUEADO"


DESCRICAO_STATUS: dict[Status, str] = {
    Status.VALIDADO: (
        "Conferido com fontes verificáveis, cálculos testados quando aplicável e revisão "
        "clínica concluída por profissional habilitado."
    ),
    Status.PENDENTE: (
        "Revisado tecnicamente, com fonte rastreável, mas ainda sem aprovação de profissional "
        "habilitado. Não usar para decisão assistencial."
    ),
    Status.BLOQUEADO: (
        "Erro relevante, informação insuficiente ou potencial de dano. Indisponível no "
        "aplicativo até correção e aprovação."
    ),
}

ICONE_STATUS: dict[Status, str] = {
    Status.VALIDADO: "🟢",
    Status.PENDENTE: "🟡",
    Status.BLOQUEADO: "🔴",
}


@dataclass(frozen=True)
class RevisaoClinica:
    """Registro obrigatório para que um conteúdo possa ser marcado como VALIDADO."""

    revisor: str
    registro_profissional: str  # ex.: "CRM-SP 000000"
    data: str  # AAAA-MM-DD
    observacao: str = ""

    def esta_completa(self) -> bool:
        return all(campo.strip() for campo in (self.revisor, self.registro_profissional, self.data))


def rotulo_status(status: Status) -> str:
    return f"{ICONE_STATUS[status]} {status.value}"
