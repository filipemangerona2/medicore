"""Calculadoras médicas como funções puras (sem Streamlit).

Regras de projeto:

* Toda entrada é validada (tipo, valor finito, faixa). Erros levantam ``EntradaInvalida``
  com mensagem em português, que a interface mostra ao usuário.
* Nenhuma concentração, diluição ou dose padrão é presumida: tudo vem do usuário.
* Cada resultado traz os passos do cálculo (análise dimensional), alertas e as
  referências da fórmula, para conferência humana.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional

from .formatacao import fmt, fmt_auto
from .unidades import (
    FATOR_CREATININA_MGDL_PARA_UMOLL,
    MCG_POR_UNIDADE,
    creatinina_para_mg_dl,
)


class EntradaInvalida(ValueError):
    """Entrada fora do tipo, do formato ou da faixa aceita."""


# --------------------------------------------------------------------------- validação


def _numero(
    valor: object,
    nome: str,
    *,
    minimo: Optional[float] = None,
    maximo: Optional[float] = None,
    minimo_exclusivo: bool = False,
    unidade: str = "",
) -> float:
    if valor is None:
        raise EntradaInvalida(f"Informe {nome}.")
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        raise EntradaInvalida(f"{_maiuscula(nome)} deve ser um número.")
    numero = float(valor)
    if not math.isfinite(numero):
        raise EntradaInvalida(f"{_maiuscula(nome)} deve ser um número finito.")
    sufixo = f" {unidade}" if unidade else ""
    if minimo is not None:
        if minimo_exclusivo and numero <= minimo:
            raise EntradaInvalida(f"{_maiuscula(nome)} deve ser maior que {fmt_auto(minimo)}{sufixo}.")
        if not minimo_exclusivo and numero < minimo:
            raise EntradaInvalida(f"{_maiuscula(nome)} deve ser no mínimo {fmt_auto(minimo)}{sufixo}.")
    if maximo is not None and numero > maximo:
        raise EntradaInvalida(f"{_maiuscula(nome)} deve ser no máximo {fmt_auto(maximo)}{sufixo}.")
    return numero


def _maiuscula(texto: str) -> str:
    return texto[:1].upper() + texto[1:]


# --------------------------------------------------------------------------- resultados


@dataclass(frozen=True)
class Resultado:
    valor: float
    unidade: str
    passos: tuple[str, ...] = ()
    alertas: tuple[str, ...] = ()
    referencias: tuple[str, ...] = ()


# =========================================================================== infusão

LIMITE_PESO_INFUSAO = (0.3, 350.0)  # kg — faixa de digitação aceita (inclui neonatos)
LIMITE_QUANTIDADE = 100_000.0  # na unidade escolhida — barreira contra erro de digitação
LIMITE_VOLUME_ML = (1.0, 5_000.0)
LIMITE_DOSE = 100_000.0
LIMITE_VAZAO_ML_H = 10_000.0
FAIXA_PLAUSIVEL_VAZAO = (0.1, 1_000.0)  # mL/h — fora disso, alerta para conferir unidades


@dataclass(frozen=True)
class UnidadeDose:
    rotulo: str
    grandeza: str  # "massa" (base: mcg) ou "UI"
    fator_base: float  # converte a unidade para mcg (massa) ou UI
    por_kg: bool
    por_minuto: bool  # True: por minuto; False: por hora


UNIDADES_DOSE: dict[str, UnidadeDose] = {
    u.rotulo: u
    for u in (
        UnidadeDose("mcg/kg/min", "massa", 1.0, True, True),
        UnidadeDose("mcg/kg/h", "massa", 1.0, True, False),
        UnidadeDose("mcg/min", "massa", 1.0, False, True),
        UnidadeDose("mcg/h", "massa", 1.0, False, False),
        UnidadeDose("mg/kg/min", "massa", 1_000.0, True, True),
        UnidadeDose("mg/kg/h", "massa", 1_000.0, True, False),
        UnidadeDose("mg/min", "massa", 1_000.0, False, True),
        UnidadeDose("mg/h", "massa", 1_000.0, False, False),
        UnidadeDose("UI/kg/h", "UI", 1.0, True, False),
        UnidadeDose("UI/min", "UI", 1.0, False, True),
        UnidadeDose("UI/h", "UI", 1.0, False, False),
    )
}

UNIDADES_QUANTIDADE: dict[str, tuple[str, float]] = {
    "mg": ("massa", MCG_POR_UNIDADE["mg"]),
    "mcg": ("massa", MCG_POR_UNIDADE["mcg"]),
    "g": ("massa", MCG_POR_UNIDADE["g"]),
    "UI": ("UI", 1.0),
}

UNIDADES_CONCENTRACAO: dict[str, tuple[str, float]] = {
    "mcg/mL": ("massa", 1.0),
    "mg/mL": ("massa", 1_000.0),
    "UI/mL": ("UI", 1.0),
}

_ROTULO_BASE = {"massa": "mcg", "UI": "UI"}


@dataclass(frozen=True)
class Concentracao:
    valor_base_por_ml: float  # mcg/mL (massa) ou UI/mL
    grandeza: str
    descricao: str
    passos: tuple[str, ...] = ()

    @property
    def unidade_base(self) -> str:
        return f"{_ROTULO_BASE[self.grandeza]}/mL"


def concentracao_por_diluicao(quantidade: float, unidade_quantidade: str, volume_final_ml: float) -> Concentracao:
    """Concentração final = quantidade total do fármaco ÷ volume final da solução."""
    if unidade_quantidade not in UNIDADES_QUANTIDADE:
        raise EntradaInvalida(f"Unidade de quantidade não suportada: {unidade_quantidade!r}.")
    qtd = _numero(quantidade, "a quantidade de fármaco", minimo=0, minimo_exclusivo=True, maximo=LIMITE_QUANTIDADE, unidade=unidade_quantidade)
    vol = _numero(volume_final_ml, "o volume final", minimo=LIMITE_VOLUME_ML[0], maximo=LIMITE_VOLUME_ML[1], unidade="mL")
    grandeza, fator = UNIDADES_QUANTIDADE[unidade_quantidade]
    base = qtd * fator
    conc = base / vol
    rot = _ROTULO_BASE[grandeza]
    passos = []
    if fator != 1.0:
        passos.append(f"{fmt_auto(qtd, 4)} {unidade_quantidade} = {fmt_auto(base, 4)} {rot}")
    passos.append(f"{fmt_auto(base, 4)} {rot} ÷ {fmt_auto(vol, 2)} mL = {fmt_auto(conc, 4)} {rot}/mL")
    descricao = f"{fmt_auto(qtd, 4)} {unidade_quantidade} em {fmt_auto(vol, 2)} mL = {fmt_auto(conc, 4)} {rot}/mL"
    return Concentracao(conc, grandeza, descricao, tuple(passos))


def concentracao_direta(valor: float, unidade: str) -> Concentracao:
    if unidade not in UNIDADES_CONCENTRACAO:
        raise EntradaInvalida(f"Unidade de concentração não suportada: {unidade!r}.")
    v = _numero(valor, "a concentração", minimo=0, minimo_exclusivo=True, maximo=LIMITE_QUANTIDADE, unidade=unidade)
    grandeza, fator = UNIDADES_CONCENTRACAO[unidade]
    base = v * fator
    rot = _ROTULO_BASE[grandeza]
    passos = () if fator == 1.0 else (f"{fmt_auto(v, 4)} {unidade} = {fmt_auto(base, 4)} {rot}/mL",)
    return Concentracao(base, grandeza, f"{fmt_auto(v, 4)} {unidade}", passos)


def _validar_unidade_dose(unidade_dose: str, concentracao: Concentracao) -> UnidadeDose:
    if unidade_dose not in UNIDADES_DOSE:
        raise EntradaInvalida(f"Unidade de dose não suportada: {unidade_dose!r}.")
    if not isinstance(concentracao, Concentracao):
        raise EntradaInvalida("Informe a concentração da solução.")
    unidade = UNIDADES_DOSE[unidade_dose]
    if unidade.grandeza != concentracao.grandeza:
        raise EntradaInvalida(
            "Unidades incompatíveis: dose em "
            f"{'massa (mg/mcg)' if unidade.grandeza == 'massa' else 'UI'} e concentração em "
            f"{'massa (mg/mcg)' if concentracao.grandeza == 'massa' else 'UI'}."
        )
    return unidade


def _peso_se_necessario(unidade: UnidadeDose, peso_kg: Optional[float]) -> Optional[float]:
    if not unidade.por_kg:
        return None
    return _numero(peso_kg, "o peso", minimo=LIMITE_PESO_INFUSAO[0], maximo=LIMITE_PESO_INFUSAO[1], unidade="kg")


def _alertas_vazao(vazao: float) -> tuple[str, ...]:
    if vazao < FAIXA_PLAUSIVEL_VAZAO[0] or vazao > FAIXA_PLAUSIVEL_VAZAO[1]:
        return (
            f"Vazão de {fmt(vazao, 2)} mL/h está fora da faixa de {fmt_auto(FAIXA_PLAUSIVEL_VAZAO[0])} a "
            f"{fmt_auto(FAIXA_PLAUSIVEL_VAZAO[1])} mL/h: confira unidades, concentração e capacidade da bomba.",
        )
    return ()


def vazao_ml_h(
    dose: float,
    unidade_dose: str,
    concentracao: Concentracao,
    peso_kg: Optional[float] = None,
) -> Resultado:
    """Vazão (mL/h) = dose por hora (na unidade-base) ÷ concentração (unidade-base/mL)."""
    unidade = _validar_unidade_dose(unidade_dose, concentracao)
    d = _numero(dose, "a dose", minimo=0, minimo_exclusivo=True, maximo=LIMITE_DOSE, unidade=unidade_dose)
    peso = _peso_se_necessario(unidade, peso_kg)
    rot = _ROTULO_BASE[unidade.grandeza]
    passos = list(concentracao.passos)

    taxa = d * unidade.fator_base
    rotulo_atual = unidade_dose
    if unidade.fator_base != 1.0:
        rotulo_conv = rotulo_atual.replace("mg", "mcg", 1)
        passos.append(f"{fmt_auto(d, 4)} {rotulo_atual} = {fmt_auto(taxa, 4)} {rotulo_conv}")
        rotulo_atual = rotulo_conv
    if peso is not None:
        nova = taxa * peso
        rotulo_sem_kg = rotulo_atual.replace("/kg", "")
        passos.append(f"{fmt_auto(taxa, 4)} {rotulo_atual} × {fmt_auto(peso, 2)} kg = {fmt_auto(nova, 4)} {rotulo_sem_kg}")
        taxa, rotulo_atual = nova, rotulo_sem_kg
    if unidade.por_minuto:
        nova = taxa * 60.0
        passos.append(f"{fmt_auto(taxa, 4)} {rot}/min × 60 min/h = {fmt_auto(nova, 4)} {rot}/h")
        taxa = nova
    vazao = taxa / concentracao.valor_base_por_ml
    passos.append(f"{fmt_auto(taxa, 4)} {rot}/h ÷ {fmt_auto(concentracao.valor_base_por_ml, 4)} {rot}/mL = {fmt(vazao, 2)} mL/h")
    if vazao > LIMITE_VAZAO_ML_H:
        raise EntradaInvalida(
            f"Resultado de {fmt(vazao, 0)} mL/h é incompatível com infusão contínua: confira dose, unidade e concentração."
        )
    return Resultado(vazao, "mL/h", tuple(passos), _alertas_vazao(vazao), ())


def dose_pela_vazao(
    vazao: float,
    unidade_dose: str,
    concentracao: Concentracao,
    peso_kg: Optional[float] = None,
) -> Resultado:
    """Operação inversa: dose infundida = vazão × concentração, convertida para a unidade pedida."""
    unidade = _validar_unidade_dose(unidade_dose, concentracao)
    v = _numero(vazao, "a vazão", minimo=0, minimo_exclusivo=True, maximo=LIMITE_VAZAO_ML_H, unidade="mL/h")
    peso = _peso_se_necessario(unidade, peso_kg)
    rot = _ROTULO_BASE[unidade.grandeza]
    passos = list(concentracao.passos)
    por_hora = v * concentracao.valor_base_por_ml
    passos.append(f"{fmt_auto(v, 4)} mL/h × {fmt_auto(concentracao.valor_base_por_ml, 4)} {rot}/mL = {fmt_auto(por_hora, 4)} {rot}/h")
    taxa = por_hora
    if unidade.por_minuto:
        taxa = taxa / 60.0
        passos.append(f"{fmt_auto(por_hora, 4)} {rot}/h ÷ 60 = {fmt_auto(taxa, 4)} {rot}/min")
    if peso is not None:
        anterior = taxa
        taxa = taxa / peso
        tempo = "min" if unidade.por_minuto else "h"
        passos.append(f"{fmt_auto(anterior, 4)} {rot}/{tempo} ÷ {fmt_auto(peso, 2)} kg = {fmt_auto(taxa, 4)} {rot}/kg/{tempo}")
    dose = taxa / unidade.fator_base
    if unidade.fator_base != 1.0:
        passos.append(f"{fmt_auto(taxa, 4)} (em mcg) ÷ {fmt_auto(unidade.fator_base)} = {fmt_auto(dose, 4)} {unidade_dose}")
    return Resultado(dose, unidade_dose, tuple(passos), _alertas_vazao(v), ())


# Bula do Hyponor (Hypofarma): ampola de 4 mL com 8 mg de hemitartarato de norepinefrina,
# equivalente a 4 mg de norepinefrina base.
RAZAO_BASE_POR_HEMITARTARATO_NORA = 4.0 / 8.0


def norepinefrina_hemitartarato_para_base(mg_hemitartarato: float) -> Resultado:
    mg = _numero(mg_hemitartarato, "a quantidade de hemitartarato", minimo=0, minimo_exclusivo=True, maximo=LIMITE_QUANTIDADE, unidade="mg")
    base = mg * RAZAO_BASE_POR_HEMITARTARATO_NORA
    passos = (f"{fmt_auto(mg, 4)} mg de hemitartarato × (4 mg base ÷ 8 mg hemitartarato) = {fmt_auto(base, 4)} mg de norepinefrina base",)
    return Resultado(base, "mg (base)", passos, (), ("bula_hyponor",))


# =========================================================================== função renal

LIMITE_IDADE_CG = (18.0, 120.0)
FAIXA_IDADE_ESTUDO_CG = (18.0, 92.0)  # população do estudo original (resumo do artigo)
LIMITE_PESO_ADULTO = (20.0, 350.0)
LIMITE_CREATININA_MG_DL = (0.1, 25.0)
SEXOS = ("masculino", "feminino")


def _normalizar_sexo(sexo: object) -> str:
    if not isinstance(sexo, str):
        raise EntradaInvalida("Informe o sexo biológico (masculino ou feminino).")
    s = sexo.strip().lower()
    if s in ("m", "masc", "masculino"):
        return "masculino"
    if s in ("f", "fem", "feminino"):
        return "feminino"
    raise EntradaInvalida("Sexo biológico deve ser 'masculino' ou 'feminino'.")


def clcr_cockcroft_gault(
    idade_anos: float,
    peso_kg: float,
    creatinina: float,
    unidade_creatinina: str,
    sexo: str,
) -> Resultado:
    """ClCr (mL/min) = (140 − idade) × peso ÷ (72 × creatinina em mg/dL); × 0,85 no sexo feminino."""
    idade = _numero(idade_anos, "a idade", minimo=LIMITE_IDADE_CG[0], maximo=LIMITE_IDADE_CG[1], unidade="anos")
    peso = _numero(peso_kg, "o peso", minimo=LIMITE_PESO_ADULTO[0], maximo=LIMITE_PESO_ADULTO[1], unidade="kg")
    if unidade_creatinina not in ("mg/dL", "µmol/L"):
        raise EntradaInvalida("Unidade da creatinina deve ser mg/dL ou µmol/L.")
    if unidade_creatinina == "mg/dL":
        scr = _numero(creatinina, "a creatinina", minimo=LIMITE_CREATININA_MG_DL[0], maximo=LIMITE_CREATININA_MG_DL[1], unidade="mg/dL")
    else:
        bruto = _numero(
            creatinina,
            "a creatinina",
            minimo=round(LIMITE_CREATININA_MG_DL[0] * FATOR_CREATININA_MGDL_PARA_UMOLL, 1),
            maximo=round(LIMITE_CREATININA_MG_DL[1] * FATOR_CREATININA_MGDL_PARA_UMOLL, 0),
            unidade="µmol/L",
        )
        scr = creatinina_para_mg_dl(bruto, "µmol/L")
    sexo_n = _normalizar_sexo(sexo)

    passos = []
    alertas = []
    if unidade_creatinina == "µmol/L":
        passos.append(f"{fmt_auto(creatinina, 2)} µmol/L ÷ {fmt(FATOR_CREATININA_MGDL_PARA_UMOLL, 2)} = {fmt(scr, 3)} mg/dL")
        if creatinina < 20:
            alertas.append("Creatinina abaixo de 20 µmol/L: confirme se o valor não está em mg/dL.")
    elif scr > 20:
        alertas.append("Creatinina acima de 20 mg/dL: confirme se o valor não está em µmol/L.")
    bruto_m = (140.0 - idade) * peso / (72.0 * scr)
    passos.append(f"(140 − {fmt_auto(idade)}) × {fmt_auto(peso, 2)} ÷ (72 × {fmt_auto(scr, 3)}) = {fmt(bruto_m, 1)} mL/min")
    clcr = bruto_m
    if sexo_n == "feminino":
        clcr = bruto_m * 0.85
        passos.append(f"Sexo feminino: {fmt(bruto_m, 1)} × 0,85 = {fmt(clcr, 1)} mL/min")
    if idade > FAIXA_IDADE_ESTUDO_CG[1]:
        alertas.append("Idade acima da faixa do estudo original (18 a 92 anos): interpretar com cautela.")
    alertas.append(
        "O estudo original usou o peso corporal do paciente; em obesidade, a escolha do peso deve seguir "
        "o protocolo institucional (não definida nesta versão)."
    )
    return Resultado(clcr, "mL/min", tuple(passos), tuple(alertas), ("cockcroft1976",))


@dataclass(frozen=True)
class AjusteRenal:
    farmaco: str
    texto: str
    referencias: tuple[str, ...]


def ajustes_renais(clcr_ml_min: float) -> tuple[AjusteRenal, ...]:
    """Ajustes previstos em bula para os fármacos do guia, a partir do ClCr.

    Faixas fracionárias entre os limites das tabelas de bula (ex.: 50,5 ou 25,5 mL/min) são
    atribuídas à faixa de maior restrição.
    """
    c = _numero(clcr_ml_min, "o clearance de creatinina", minimo=0, maximo=1_000, unidade="mL/min")
    ajustes = []
    if c >= 51:
        mero = "ClCr ≥ 51 mL/min: a bula não prevê ajuste."
    elif c >= 26:
        mero = "ClCr 26–50 mL/min: 1 unidade de dose a cada 12 h."
    elif c >= 10:
        mero = "ClCr 10–25 mL/min: ½ unidade de dose a cada 12 h."
    else:
        mero = "ClCr < 10 mL/min: ½ unidade de dose a cada 24 h."
    ajustes.append(
        AjusteRenal(
            "Meropeném",
            mero + " (unidade de dose = 500 mg a 2 g, conforme indicação; a hemodiálise remove o fármaco — "
            "reiniciar a dose após a sessão).",
            ("bula_meronem", "bula_meropenem_fk"),
        )
    )
    if c < 10:
        cef = "ClCr < 10 mL/min: dose diária máxima de 2 g (se a função hepática estiver preservada)."
    else:
        cef = "Sem redução de dose pela bula enquanto a função hepática estiver preservada."
    ajustes.append(AjusteRenal("Ceftriaxona", cef, ("bula_ceftriaxona",)))
    ajustes.append(
        AjusteRenal(
            "Amiodarona",
            "A bula indica posologia habitual na insuficiência renal; a diálise não remove o fármaco.",
            ("bula_amiodarona",),
        )
    )
    ajustes.append(
        AjusteRenal(
            "Midazolam",
            "Insuficiência renal grave: sedação mais intensa e prolongada (acúmulo de metabólito); titular com cuidado.",
            ("bula_midazolam",),
        )
    )
    ajustes.append(
        AjusteRenal(
            "Fentanil",
            "A bula orienta administrar com cuidado na insuficiência renal, sem ajuste numérico.",
            ("bula_fentanest",),
        )
    )
    return tuple(ajustes)


# =========================================================================== superfície corporal

LIMITE_PESO_SC = (0.5, 350.0)
LIMITE_ALTURA_SC = (30.0, 250.0)


@dataclass(frozen=True)
class SuperficieCorporal:
    mosteller_m2: float
    dubois_m2: float
    passos: tuple[str, ...]
    referencias: tuple[str, ...] = ("mosteller1987", "dubois1916")


def superficie_corporal(peso_kg: float, altura_cm: float) -> SuperficieCorporal:
    peso = _numero(peso_kg, "o peso", minimo=LIMITE_PESO_SC[0], maximo=LIMITE_PESO_SC[1], unidade="kg")
    altura = _numero(altura_cm, "a altura", minimo=LIMITE_ALTURA_SC[0], maximo=LIMITE_ALTURA_SC[1], unidade="cm")
    mosteller = math.sqrt(altura * peso / 3600.0)
    dubois = 0.007184 * peso**0.425 * altura**0.725
    passos = (
        f"Mosteller: √({fmt_auto(altura, 1)} cm × {fmt_auto(peso, 2)} kg ÷ 3600) = {fmt(mosteller, 2)} m²",
        f"DuBois: 0,007184 × {fmt_auto(peso, 2)}^0,425 × {fmt_auto(altura, 1)}^0,725 = {fmt(dubois, 2)} m²",
    )
    return SuperficieCorporal(mosteller, dubois, passos)


# =========================================================================== queimados

FATORES_REPOSICAO: dict[float, str] = {
    4.0: "Parkland (clássica): 4 mL × kg × %SCQ",
    2.0: "Estimativa inicial da ABA 2023: 2 mL × kg × %SCQ",
}
LIMITE_PESO_QUEIMADO = (1.0, 350.0)


@dataclass(frozen=True)
class ReposicaoQueimado:
    fator_ml_kg_pct: float
    total_24h_ml: float
    volume_primeiras_8h_ml: float
    taxa_primeiras_8h_ml_h: float
    volume_16h_seguintes_ml: float
    taxa_16h_seguintes_ml_h: float
    passos: tuple[str, ...]
    alertas: tuple[str, ...]
    referencias: tuple[str, ...]


def reposicao_queimado(
    peso_kg: float,
    pct_scq: float,
    fator_ml_kg_pct: float = 4.0,
    adulto: Optional[bool] = None,
) -> ReposicaoQueimado:
    """Volume de cristaloide estimado para 24 h; metade nas primeiras 8 h e metade nas 16 h seguintes."""
    peso = _numero(peso_kg, "o peso", minimo=LIMITE_PESO_QUEIMADO[0], maximo=LIMITE_PESO_QUEIMADO[1], unidade="kg")
    pct = _numero(pct_scq, "a superfície corporal queimada", minimo=0, minimo_exclusivo=True, maximo=100, unidade="%")
    if isinstance(fator_ml_kg_pct, bool) or fator_ml_kg_pct not in FATORES_REPOSICAO:
        raise EntradaInvalida("Fator deve ser 4 mL/kg/%SCQ (Parkland) ou 2 mL/kg/%SCQ (ABA 2023).")
    fator = float(fator_ml_kg_pct)
    total = fator * peso * pct
    metade = total / 2.0
    taxa_8 = metade / 8.0
    taxa_16 = metade / 16.0
    passos = (
        f"{fmt_auto(fator)} mL × {fmt_auto(peso, 2)} kg × {fmt_auto(pct, 1)}% = {fmt(total, 0)} mL em 24 h",
        f"Primeiras 8 h: {fmt(total, 0)} ÷ 2 = {fmt(metade, 0)} mL → {fmt(metade, 0)} ÷ 8 h = {fmt(taxa_8, 1)} mL/h",
        f"16 h seguintes: {fmt(metade, 0)} mL → {fmt(metade, 0)} ÷ 16 h = {fmt(taxa_16, 1)} mL/h",
    )
    alertas = [
        "Contar apenas queimaduras não superficiais na %SCQ (queimaduras superficiais não entram no cálculo).",
        "Estimativa inicial: ajustar a infusão pela resposta clínica (débito urinário e parâmetros hemodinâmicos).",
        "Momento de início da contagem das 8 h (queimadura × chegada): não confirmado em fonte primária nesta "
        "revisão — seguir o protocolo institucional.",
    ]
    referencias = ["msd_parkland"]
    if fator == 2.0:
        referencias.insert(0, "aba2023_queimados")
        if pct < 20 or adulto is False:
            alertas.insert(0, "A recomendação da ABA 2023 abrange adultos com ≥ 20% de SCQ; este caso está fora dessa população.")
    else:
        referencias.append("aba2023_queimados")
        alertas.insert(0, "A ABA 2023 recomenda iniciar a reposição com 2 mL/kg/%SCQ em adultos com ≥ 20% de SCQ, em vez de 4 mL.")
    return ReposicaoQueimado(
        fator, total, metade, taxa_8, metade, taxa_16, passos, tuple(alertas), tuple(referencias)
    )


# =========================================================================== potássio

LIMITE_POTASSIO = (0.5, 15.0)  # mmol/L — faixa de digitação aceita


@dataclass(frozen=True)
class ClassificacaoPotassio:
    valor_mmol_l: float
    categoria: str
    nivel: str  # "critico", "alerta" ou "neutro"
    mensagens: tuple[str, ...]
    referencias: tuple[str, ...]


def classificar_potassio(potassio_mmol_l: float) -> ClassificacaoPotassio:
    """Classificação do potássio sérico (1 mmol/L = 1 mEq/L para o K⁺, íon monovalente)."""
    k = _numero(potassio_mmol_l, "o potássio sérico", minimo=LIMITE_POTASSIO[0], maximo=LIMITE_POTASSIO[1], unidade="mmol/L")
    extremos = []
    if k < 1.5 or k > 10:
        extremos.append("Valor extremo: confirme a amostra, a unidade e o laudo antes de agir.")
    hipo_refs = ("sps2024_hipocalemia", "smpc_kcl")
    hiper_refs = ("ukka_hipercalemia",)
    if k < 2.5:
        return ClassificacaoPotassio(
            k,
            "Hipocalemia grave (< 2,5 mmol/L)",
            "critico",
            tuple(
                extremos
                + [
                    "Reposição intravenosa em ambiente hospitalar; via oral não é adequada (SPS 2024).",
                    "Velocidade usual até 10 mmol/h; até 20 mmol/h na deficiência grave sintomática (SmPC).",
                    "Acima de 20 mmol/h exige monitorização cardíaca (SPS); até 40 mmol/h só com K < 2 mmol/L e ECG contínuo (SmPC).",
                    "Monitorar potássio, magnésio, função renal e ECG.",
                ]
            ),
            hipo_refs,
        )
    if k < 3.0:
        return ClassificacaoPotassio(
            k,
            "Hipocalemia moderada (2,5–2,9 mmol/L)",
            "alerta",
            tuple(
                extremos
                + [
                    "Reposição oral quando possível; IV se a via oral/enteral não for possível (SPS 2024).",
                    "Se IV: velocidade usual até 10 mmol/h e concentração periférica até 40 mmol/L (SPS; SmPC).",
                ]
            ),
            hipo_refs,
        )
    if k < 3.5:
        return ClassificacaoPotassio(
            k,
            "Hipocalemia leve (3,0–3,4 mmol/L)",
            "alerta",
            tuple(extremos + ["Reposição preferencialmente oral; IV apenas se a via oral/enteral não for possível (SPS 2024)."]),
            hipo_refs,
        )
    if k < 5.5:
        return ClassificacaoPotassio(
            k,
            "Fora das faixas de hipocalemia e hipercalemia das referências (3,5–5,4 mmol/L)",
            "neutro",
            tuple(extremos + ["Interpretar no contexto clínico e na tendência dos exames; esta faixa não é, por si só, garantia de segurança."]),
            hipo_refs + hiper_refs,
        )
    if k < 6.0:
        return ClassificacaoPotassio(
            k,
            "Hipercalemia leve (5,5–5,9 mmol/L)",
            "alerta",
            tuple(extremos + ["Resultado inesperado deve ser repetido (UKKA)."]),
            hiper_refs,
        )
    if k < 6.5:
        return ClassificacaoPotassio(
            k,
            "Hipercalemia moderada (6,0–6,4 mmol/L)",
            "critico",
            tuple(
                extremos
                + [
                    "ECG de 12 derivações urgente em paciente internado com K ≥ 6,0 mmol/L (UKKA 14.1).",
                    "Monitorização cardíaca contínua se houver alteração no ECG, instabilidade ou risco de elevação rápida (UKKA 14.2).",
                ]
            ),
            hiper_refs,
        )
    return ClassificacaoPotassio(
        k,
        "Hipercalemia grave (≥ 6,5 mmol/L)",
        "critico",
        tuple(
            extremos
            + [
                "Monitorização cardíaca contínua (UKKA 14.2) e tratamento de emergência conforme protocolo institucional.",
                "UKKA: cálcio IV se houver alteração no ECG; insulina-glicose na hipercalemia grave; salbutamol apenas como adjuvante.",
                "Se houver suspeita de pseudo-hipercalemia, repetir a coleta com técnica adequada (UKKA 15.3) — sem atrasar o tratamento.",
            ]
        ),
        hiper_refs,
    )


@dataclass(frozen=True)
class VerificacaoInfusaoPotassio:
    concentracao_mmol_l: float
    taxa_mmol_h: float
    passos: tuple[str, ...]
    alertas: tuple[str, ...]
    referencias: tuple[str, ...] = ("sps2024_hipocalemia", "smpc_kcl", "bula_kcl_blau")

    @property
    def dentro_dos_limites(self) -> bool:
        return not self.alertas


def verificar_infusao_potassio(
    potassio_total_mmol: float,
    volume_final_ml: float,
    vazao_ml_h: float,
    acesso_central: bool = False,
    ecg_continuo: bool = False,
    potassio_serico_mmol_l: Optional[float] = None,
) -> VerificacaoInfusaoPotassio:
    """Confere concentração (mmol/L) e velocidade (mmol/h) de uma solução de potássio IV para adultos."""
    total = _numero(potassio_total_mmol, "o potássio total na solução", minimo=0, minimo_exclusivo=True, maximo=500, unidade="mmol")
    volume = _numero(volume_final_ml, "o volume final", minimo=LIMITE_VOLUME_ML[0], maximo=LIMITE_VOLUME_ML[1], unidade="mL")
    vazao = _numero(vazao_ml_h, "a vazão", minimo=0, minimo_exclusivo=True, maximo=2_000, unidade="mL/h")
    for nome, flag in (("acesso central", acesso_central), ("ECG contínuo", ecg_continuo)):
        if not isinstance(flag, bool):
            raise EntradaInvalida(f"Indique sim/não para {nome}.")
    k_serico = None
    if potassio_serico_mmol_l is not None:
        k_serico = _numero(potassio_serico_mmol_l, "o potássio sérico", minimo=LIMITE_POTASSIO[0], maximo=LIMITE_POTASSIO[1], unidade="mmol/L")

    conc = total / (volume / 1000.0)
    taxa = conc * vazao / 1000.0
    passos = (
        f"{fmt_auto(total, 2)} mmol ÷ {fmt_auto(volume / 1000.0, 3)} L = {fmt(conc, 1)} mmol/L",
        f"{fmt(conc, 1)} mmol/L × {fmt_auto(vazao, 2)} mL/h ÷ 1000 = {fmt(taxa, 1)} mmol/h",
    )
    alertas = []
    if conc > 80:
        alertas.append("Concentração acima de 80 mmol/L: além do máximo descrito no SmPC.")
    elif conc > 40:
        if acesso_central:
            alertas.append(
                "Concentração acima de 40 mmol/L: o SmPC admite até 80 mmol/L apenas em adultos com K < 2 mmol/L; "
                "o SPS cita concentrações maiores só em casos graves, por acesso central e com bomba de infusão."
            )
            if k_serico is None or k_serico >= 2.0:
                alertas.append("Para concentração acima de 40 mmol/L o SmPC exige K sérico < 2 mmol/L (informe ou revise).")
        else:
            alertas.append("Concentração acima de 40 mmol/L, que é o máximo para acesso periférico (SPS 2024).")
    if taxa > 40:
        alertas.append("Velocidade acima de 40 mmol/h: além do máximo descrito no SmPC.")
    elif taxa > 20:
        alertas.append("Velocidade acima de 20 mmol/h exige monitorização cardíaca (SPS) e, pelo SmPC, só é admitida com K < 2 mmol/L e ECG contínuo.")
        if not ecg_continuo:
            alertas.append("ECG contínuo não indicado: velocidade não admitida.")
        if k_serico is None or k_serico >= 2.0:
            alertas.append("K sérico não informado ou ≥ 2 mmol/L: velocidade acima de 20 mmol/h não admitida pelo SmPC.")
    elif taxa > 10:
        if k_serico is None or k_serico >= 2.5:
            alertas.append(
                "Velocidade acima de 10 mmol/h: o SmPC reserva até 20 mmol/h para deficiência grave sintomática (K < 2,5 mmol/L)."
            )
    return VerificacaoInfusaoPotassio(conc, taxa, passos, tuple(alertas))


def volume_concentrado_potassio(potassio_mmol: float, concentracao_mmol_ml: float) -> Resultado:
    """mL de solução concentrada necessários para fornecer ``potassio_mmol`` (mmol = mEq para K⁺)."""
    total = _numero(potassio_mmol, "a quantidade de potássio", minimo=0, minimo_exclusivo=True, maximo=500, unidade="mmol")
    conc = _numero(concentracao_mmol_ml, "a concentração da ampola", minimo=0, minimo_exclusivo=True, maximo=5, unidade="mmol/mL")
    volume = total / conc
    passos = (f"{fmt_auto(total, 2)} mmol ÷ {fmt_auto(conc, 3)} mmol/mL = {fmt(volume, 2)} mL",)
    alertas = ("Solução concentrada: SEMPRE diluir antes da infusão; nunca administrar sem diluição.",)
    return Resultado(volume, "mL", passos, alertas, ("bula_kcl_blau", "smpc_kcl"))
