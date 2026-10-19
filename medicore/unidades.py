"""Conversões de unidades usadas pelas calculadoras.

Contém apenas constantes físico-químicas (massas molares e prefixos SI). Nenhuma
constante clínica fica aqui.
"""

from __future__ import annotations

# Prefixos de massa, convertidos para micrograma (mcg)
MCG_POR_UNIDADE: dict[str, float] = {"g": 1_000_000.0, "mg": 1_000.0, "mcg": 1.0}

# Massas molares (g/mol = mg/mmol)
MASSA_MOLAR_CREATININA = 113.12
MASSA_MOLAR_GLICOSE = 180.16
MASSA_MOLAR_KCL = 74.55

# 1 mg/dL = 10 mg/L; dividido pela massa molar (mg/mmol) dá mmol/L; × 1000 dá µmol/L.
FATOR_CREATININA_MGDL_PARA_UMOLL = 10.0 * 1000.0 / MASSA_MOLAR_CREATININA  # ≈ 88,40
# 1 mmol/L de glicose = 180,16 mg/L = 18,016 mg/dL
FATOR_GLICOSE_MMOLL_PARA_MGDL = MASSA_MOLAR_GLICOSE / 10.0  # ≈ 18,016

UNIDADES_CREATININA = ("mg/dL", "µmol/L")


def massa_para_mcg(valor: float, unidade: str) -> float:
    try:
        return valor * MCG_POR_UNIDADE[unidade]
    except KeyError as exc:
        raise ValueError(f"Unidade de massa desconhecida: {unidade!r}") from exc


def mcg_para(valor_mcg: float, unidade: str) -> float:
    try:
        return valor_mcg / MCG_POR_UNIDADE[unidade]
    except KeyError as exc:
        raise ValueError(f"Unidade de massa desconhecida: {unidade!r}") from exc


def creatinina_para_mg_dl(valor: float, unidade: str) -> float:
    if unidade == "mg/dL":
        return valor
    if unidade == "µmol/L":
        return valor / FATOR_CREATININA_MGDL_PARA_UMOLL
    raise ValueError(f"Unidade de creatinina desconhecida: {unidade!r}")


def glicose_mmol_l_para_mg_dl(valor_mmol_l: float) -> float:
    return valor_mmol_l * FATOR_GLICOSE_MMOLL_PARA_MGDL


def mmol_por_ml_kcl(percentual_m_v: float) -> float:
    """Potássio (mmol/mL) numa solução de KCl a X% (m/v).

    X% m/v = X g/100 mL = 10·X mg/mL. Dividindo pela massa molar (74,55 mg/mmol) obtém-se
    mmol de KCl por mL; cada mmol de KCl libera 1 mmol de K⁺, e para um íon monovalente
    1 mmol = 1 mEq.
    """
    return percentual_m_v * 10.0 / MASSA_MOLAR_KCL
