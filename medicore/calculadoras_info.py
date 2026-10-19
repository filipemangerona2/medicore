"""Metadados das calculadoras: fórmula, fontes, versão original e alterações da auditoria."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .conteudo import Alteracao, ItemBloqueado
from .status import RevisaoClinica, Status


@dataclass(frozen=True)
class CalculadoraInfo:
    id: str
    titulo: str
    descricao: str
    formula: str
    status: Status
    refs: tuple[str, ...]
    original: str
    alteracoes: tuple[Alteracao, ...]
    bloqueados: tuple[ItemBloqueado, ...]
    pendencias: tuple[str, ...]
    revisao: Optional[RevisaoClinica] = None


CALCULADORAS: tuple[CalculadoraInfo, ...] = (
    CalculadoraInfo(
        id="infusao",
        titulo="Infusão contínua (vazão em mL/h)",
        descricao=(
            "Converte dose (mcg/kg/min, mcg/min, mg/h, UI/min e outras) em vazão de bomba (mL/h) e faz o cálculo "
            "inverso, a partir da concentração REAL da solução informada pelo usuário."
        ),
        formula="vazão (mL/h) = dose por hora na unidade-base ÷ concentração (unidade-base/mL)",
        status=Status.PENDENTE,
        refs=("bula_hyponor",),
        original="vazao = (dose_val * peso_kg * 60.0) / 16.0  — concentração fixa de 16 mcg/mL (4 mg/250 mL); a droga escolhida não alterava o cálculo.",
        alteracoes=(
            Alteracao(
                "Concentração",
                "Fixa em 16 mcg/mL",
                "Informada pelo usuário (quantidade + volume final, ou valor direto); sem valor padrão",
                "Não existe concentração universal; com 8 mg/250 mL a vazão exibida seria o dobro da correta.",
                ("bula_hyponor",),
            ),
            Alteracao(
                "Unidades",
                "Somente mcg/kg/min",
                "mcg/kg/min, mcg/kg/h, mcg/min, mcg/h, mg/kg/min, mg/kg/h, mg/min, mg/h, UI/kg/h, UI/min, UI/h, com bloqueio de combinações incompatíveis",
                "Permitir os fármacos do guia (ex.: amiodarona em mg/min, vasopressina em UI/min).",
            ),
            Alteracao(
                "Sal × base",
                "(ausente)",
                "Conversor de hemitartarato de norepinefrina para base (8 mg de sal = 4 mg de base, conforme bula)",
                "Evitar erro de fator 2.",
                ("bula_hyponor",),
            ),
            Alteracao(
                "Cálculo inverso e passos",
                "(ausente)",
                "Dose a partir da vazão e exibição de cada passo da análise dimensional",
                "Permitir conferência humana do cálculo.",
            ),
        ),
        bloqueados=(),
        pendencias=("Definir concentrações padrão institucionais, se desejado, com fonte e aprovação.",),
    ),
    CalculadoraInfo(
        id="clcr",
        titulo="Clearance de creatinina (Cockcroft-Gault)",
        descricao="Estimativa do clearance de creatinina em adultos e ajustes de dose previstos em bula para os fármacos do guia.",
        formula="ClCr (mL/min) = (140 − idade) × peso (kg) ÷ (72 × creatinina em mg/dL); × 0,85 se sexo feminino",
        status=Status.PENDENTE,
        refs=("cockcroft1976", "bula_meronem", "bula_meropenem_fk", "bula_ceftriaxona"),
        original="clcr = max(0, ((140 - idade) * peso * fator_sexo) / (72 * creatinina)); idade de 0 a 120 anos; alerta genérico 'ClCr < 50: ajuste para antimicrobianos'.",
        alteracoes=(
            Alteracao(
                "Idade",
                "0 a 120 anos",
                "18 a 120 anos, com aviso acima de 92 anos (faixa do estudo original: 18 a 92 anos)",
                "A fórmula foi derivada em adultos.",
                ("cockcroft1976",),
            ),
            Alteracao(
                "Unidade da creatinina",
                "Somente mg/dL",
                "mg/dL ou µmol/L (1 mg/dL = 88,40 µmol/L), com alerta de unidade provavelmente trocada",
                "Evitar erro de fator 88.",
            ),
            Alteracao(
                "Alerta renal",
                "ClCr < 50: necessário ajuste para antimicrobianos",
                "Faixas de ajuste das bulas de meropeném e ceftriaxona e orientações de amiodarona, midazolam e fentanil",
                "Substituir o alerta genérico por orientação específica com fonte.",
                ("bula_meronem", "bula_meropenem_fk", "bula_ceftriaxona", "bula_amiodarona", "bula_midazolam", "bula_fentanest"),
            ),
        ),
        bloqueados=(),
        pendencias=(
            "Definir qual peso usar em obesidade (real, ideal ou ajustado) conforme protocolo institucional.",
        ),
    ),
    CalculadoraInfo(
        id="superficie",
        titulo="Superfície corporal (Mosteller e DuBois)",
        descricao="Calcula a superfície corporal pelas fórmulas de Mosteller e de DuBois, identificadas pelo nome correto.",
        formula="Mosteller: √(altura cm × peso kg ÷ 3600)  |  DuBois: 0,007184 × peso^0,425 × altura^0,725",
        status=Status.PENDENTE,
        refs=("mosteller1987", "dubois1916"),
        original="sc_val = (peso_kg ** 0.425) * (altura_cm ** 0.725) * 0.007184, rotulado como 'Mosteller'.",
        alteracoes=(
            Alteracao(
                "Rótulo da fórmula",
                "Fórmula de DuBois rotulada como Mosteller",
                "As duas fórmulas, cada uma com o nome correto",
                "Erro de identificação; os valores diferem até cerca de 6% em obesos.",
                ("mosteller1987", "dubois1916"),
            ),
        ),
        bloqueados=(),
        pendencias=(),
    ),
    CalculadoraInfo(
        id="queimados",
        titulo="Reposição volêmica no grande queimado",
        descricao="Estimativa inicial de cristaloide em 24 h pela fórmula de Parkland (4 mL) ou pela estimativa inicial da ABA 2023 (2 mL).",
        formula="volume 24 h = fator (mL) × peso (kg) × %SCQ; metade nas primeiras 8 h e metade nas 16 h seguintes",
        status=Status.PENDENTE,
        refs=("aba2023_queimados", "msd_parkland", "aafp2025_aba"),
        original="vol_tot = 4 * peso_kg * pct_scq; metade em 8 h e metade em 16 h; calculava para qualquer %SCQ.",
        alteracoes=(
            Alteracao(
                "Fator",
                "Somente 4 mL/kg/%SCQ",
                "4 mL (Parkland) ou 2 mL (estimativa inicial recomendada pela ABA 2023 para adultos com ≥ 20% SCQ)",
                "A ABA 2023 recomenda iniciar com 2 mL/kg/%SCQ em adultos.",
                ("aba2023_queimados", "aafp2025_aba"),
            ),
            Alteracao(
                "Avisos",
                "(ausentes)",
                "Não contar queimaduras superficiais; titular pela resposta clínica; população da ABA",
                "Uso correto da estimativa.",
                ("msd_parkland", "aba2023_queimados"),
            ),
        ),
        bloqueados=(
            ItemBloqueado(
                "Início da contagem das 8 horas",
                "Primeiras 8h: metade do volume",
                "auditoria",
                "Não foi confirmado em fonte primária acessível se as 8 h contam a partir da queimadura ou da chegada; "
                "o aplicativo não ajusta pelo tempo decorrido.",
            ),
        ),
        pendencias=(
            "Definir o momento zero (queimadura × admissão) e a meta de débito urinário com fonte primária.",
            "Definir limiar de %SCQ para reposição formal e regras pediátricas.",
        ),
    ),
    CalculadoraInfo(
        id="potassio",
        titulo="Potássio: classificação e conferência de infusão",
        descricao=(
            "Classifica o potássio sérico (hipo e hipercalemia) e confere concentração e velocidade de soluções de "
            "potássio IV para adultos."
        ),
        formula="concentração (mmol/L) = mmol ÷ volume (L); velocidade (mmol/h) = concentração × vazão (mL/h) ÷ 1000",
        status=Status.PENDENTE,
        refs=("sps2024_hipocalemia", "smpc_kcl", "ukka_hipercalemia", "bula_kcl_blau"),
        original=(
            "K < 3,5: 'Hipocalemia Crítica — periférica máx 10 mEq/h; central 20 mEq/h'; K ≥ 3,5: '✅ Potássio dentro da "
            "faixa segura' (inclusive valores de hipercalemia até 7,0)."
        ),
        alteracoes=(
            Alteracao(
                "Hipercalemia",
                "Qualquer K ≥ 3,5 exibido como 'faixa segura'",
                "Classificação de hipercalemia leve, moderada e grave com condutas de monitorização (UKKA)",
                "Erro grave: falsa tranquilização diante de hipercalemia.",
                ("ukka_hipercalemia",),
            ),
            Alteracao(
                "Gravidade da hipocalemia",
                "3,4 mmol/L rotulado como 'crítica'",
                "Leve 3,0–3,4; moderada 2,5–2,9; grave < 2,5 (SPS)",
                "Classificação verificada.",
                ("sps2024_hipocalemia",),
            ),
            Alteracao(
                "Velocidade de reposição",
                "Periférica 10 mEq/h; central 20 mEq/h",
                "Usual até 10 mmol/h; até 20 mmol/h na deficiência grave sintomática; > 20 mmol/h só com monitorização (e, pelo SmPC, K < 2 com ECG contínuo); concentração periférica até 40 mmol/L",
                "As fontes definem a velocidade pela gravidade e pela monitorização, não pelo tipo de acesso.",
                ("sps2024_hipocalemia", "smpc_kcl"),
            ),
        ),
        bloqueados=(),
        pendencias=(
            "Adaptar à concentração de KCl padronizada na instituição (ex.: 19,1% ≈ 2,56 mmol/mL, por cálculo).",
            "Incluir protocolo de reposição pediátrica, se desejado, com fonte.",
        ),
    ),
)

CALCULADORAS_POR_ID: dict[str, CalculadoraInfo] = {c.id: c for c in CALCULADORAS}
