"""Formatação numérica no padrão brasileiro (vírgula decimal, ponto de milhar).

Usa arredondamento "meio para cima" (131,25 → 131,3), o esperado em leitura clínica,
em vez do arredondamento bancário padrão do Python.
"""

from __future__ import annotations

import math
from decimal import ROUND_HALF_UP, Decimal


def fmt(valor: float, casas: int = 2) -> str:
    """Formata ``valor`` com ``casas`` decimais no padrão pt-BR.

    >>> fmt(4200.5, 1)
    '4.200,5'
    >>> fmt(131.25, 1)
    '131,3'
    """
    if valor is None or isinstance(valor, bool):
        return "—"
    try:
        numero = float(valor)
    except (TypeError, ValueError):
        return "—"
    if not math.isfinite(numero):
        return "—"
    quantizado = Decimal(repr(numero)).quantize(Decimal(1).scaleb(-casas), rounding=ROUND_HALF_UP)
    if quantizado == 0:
        quantizado = abs(quantizado)  # evita "-0,00"
    texto = f"{quantizado:,.{casas}f}"
    return texto.replace(",", "\u0000").replace(".", ",").replace("\u0000", ".")


def fmt_auto(valor: float, max_casas: int = 2) -> str:
    """Formata sem zeros finais desnecessários (ex.: 4,0 → '4'; 0,25 → '0,25')."""
    texto = fmt(valor, max_casas)
    if "," in texto:
        texto = texto.rstrip("0").rstrip(",")
    return texto
