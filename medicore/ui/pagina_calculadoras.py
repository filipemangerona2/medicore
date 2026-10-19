"""Aba: calculadoras. Toda a matemática vem de ``medicore.calculos``."""

from __future__ import annotations

import streamlit as st

from .. import calculos as calc
from ..calculadoras_info import CALCULADORAS_POR_ID
from ..formatacao import fmt, fmt_auto
from ..referencias import rotulo
from ..unidades import mmol_por_ml_kcl
from . import componentes as c

SEXO_PARA_CALCULO = {"Masculino": "masculino", "Feminino": "feminino"}


# --------------------------------------------------------------------------- dados do paciente


def render_dados_paciente() -> None:
    """Campos compartilhados, na barra lateral (como na versão original). Sem valores padrão."""
    st.sidebar.header("🧍 Dados do paciente")
    st.sidebar.caption("Usados pelas calculadoras. Campos vazios não recebem valor padrão.")
    st.sidebar.number_input("Peso (kg)", min_value=0.3, max_value=350.0, value=None, step=0.5, format="%.1f", key="peso_kg")
    st.sidebar.number_input("Altura (cm)", min_value=30.0, max_value=250.0, value=None, step=1.0, format="%.0f", key="altura_cm")
    st.sidebar.number_input("Idade (anos)", min_value=0, max_value=120, value=None, step=1, key="idade_anos")
    st.sidebar.selectbox("Sexo biológico", ["Masculino", "Feminino"], index=None, placeholder="Selecione", key="sexo")
    st.sidebar.number_input(
        "Creatinina sérica", min_value=0.0, max_value=3000.0, value=None, step=0.1, format="%.2f", key="creatinina"
    )
    st.sidebar.radio("Unidade da creatinina", ["mg/dL", "µmol/L"], horizontal=True, key="unidade_creatinina")


def _paciente() -> dict:
    ss = st.session_state
    return {
        "peso": ss.get("peso_kg"),
        "altura": ss.get("altura_cm"),
        "idade": ss.get("idade_anos"),
        "sexo": ss.get("sexo"),
        "creatinina": ss.get("creatinina"),
        "unidade_creatinina": ss.get("unidade_creatinina") or "mg/dL",
    }


def _faltando(campos: dict) -> bool:
    ausentes = [nome for nome, valor in campos.items() if valor is None]
    if ausentes:
        st.info("Preencha em **Dados do paciente** (barra lateral, ícone ☰ ou ›): " + ", ".join(ausentes) + ".")
        return True
    return False


def _cabecalho(calc_id: str) -> None:
    info = CALCULADORAS_POR_ID[calc_id]
    st.markdown(f"#### {info.titulo}")
    st.caption(info.descricao)
    c.selo_status(info.status)
    st.code(info.formula, language=None)


def _rodape(calc_id: str, extras: tuple[str, ...] = ()) -> None:
    info = CALCULADORAS_POR_ID[calc_id]
    c.lista_bloqueados(info.bloqueados)
    c.lista_pendencias(info.pendencias)
    c.lista_referencias(tuple(info.refs) + tuple(extras))


# --------------------------------------------------------------------------- infusão


def _infusao() -> None:
    _cabecalho("infusao")
    modo = st.radio(
        "O que calcular",
        ["Vazão (mL/h) a partir da dose", "Dose a partir da vazão (mL/h)"],
        key="inf_modo",
    )
    unidade = st.selectbox("Unidade da dose", list(calc.UNIDADES_DOSE), key="inf_unidade_dose")
    forma = st.radio(
        "Como informar a concentração da solução",
        ["Quantidade de fármaco e volume final", "Concentração já calculada"],
        key="inf_forma_conc",
    )
    if forma.startswith("Quantidade"):
        col1, col2, col3 = st.columns(3)
        qtd = col1.number_input("Quantidade total", min_value=0.0, value=None, step=1.0, format="%.3f", key="inf_qtd")
        un_qtd = col2.selectbox("Unidade", list(calc.UNIDADES_QUANTIDADE), key="inf_un_qtd")
        vol = col3.number_input("Volume final (mL)", min_value=0.0, value=None, step=10.0, format="%.1f", key="inf_vol")
    else:
        col1, col2 = st.columns(2)
        conc_valor = col1.number_input("Concentração", min_value=0.0, value=None, step=0.1, format="%.4f", key="inf_conc")
        conc_un = col2.selectbox("Unidade", list(calc.UNIDADES_CONCENTRACAO), key="inf_conc_un")

    if modo.startswith("Vazão"):
        valor = st.number_input(f"Dose ({unidade})", min_value=0.0, value=None, step=0.01, format="%.4f", key="inf_dose")
    else:
        valor = st.number_input("Vazão da bomba (mL/h)", min_value=0.0, value=None, step=0.1, format="%.2f", key="inf_vazao")

    try:
        if forma.startswith("Quantidade"):
            if qtd is None or vol is None:
                st.info("Informe a quantidade total de fármaco e o volume final da solução.")
                return
            concentracao = calc.concentracao_por_diluicao(qtd, un_qtd, vol)
        else:
            if conc_valor is None:
                st.info("Informe a concentração da solução.")
                return
            concentracao = calc.concentracao_direta(conc_valor, conc_un)
        st.caption(f"Concentração considerada: {concentracao.descricao}")
        if valor is None:
            st.info("Informe a dose." if modo.startswith("Vazão") else "Informe a vazão.")
            return
        peso = _paciente()["peso"]
        if calc.UNIDADES_DOSE[unidade].por_kg and peso is None:
            st.info("Esta unidade é por kg: informe o peso em **Dados do paciente** (barra lateral).")
            return
        if modo.startswith("Vazão"):
            resultado = calc.vazao_ml_h(valor, unidade, concentracao, peso)
            st.metric("Vazão na bomba", f"{fmt(resultado.valor, 2)} mL/h")
        else:
            resultado = calc.dose_pela_vazao(valor, unidade, concentracao, peso)
            st.metric("Dose infundida", f"{fmt_auto(resultado.valor, 4)} {unidade}")
        c.alertas(resultado.alertas)
        c.passos(resultado.passos)
    except calc.EntradaInvalida as erro:
        st.error(str(erro))
    finally:
        with st.expander("Noradrenalina: converter hemitartarato (sal) em base"):
            st.caption("Conforme a bula consultada: 8 mg de hemitartarato = 4 mg de norepinefrina base.")
            sal = st.number_input("Hemitartarato (mg)", min_value=0.0, value=None, step=1.0, format="%.2f", key="nora_sal")
            if sal is not None:
                try:
                    base = calc.norepinefrina_hemitartarato_para_base(sal)
                    st.metric("Norepinefrina base", f"{fmt_auto(base.valor, 3)} mg")
                except calc.EntradaInvalida as erro:
                    st.error(str(erro))
        _rodape("infusao")


# --------------------------------------------------------------------------- função renal


def _clcr() -> None:
    _cabecalho("clcr")
    p = _paciente()
    if _faltando({"idade": p["idade"], "peso": p["peso"], "sexo biológico": p["sexo"], "creatinina": p["creatinina"]}):
        _rodape("clcr")
        return
    try:
        r = calc.clcr_cockcroft_gault(p["idade"], p["peso"], p["creatinina"], p["unidade_creatinina"], SEXO_PARA_CALCULO[p["sexo"]])
    except calc.EntradaInvalida as erro:
        st.error(str(erro))
        _rodape("clcr")
        return
    st.metric("ClCr estimado (Cockcroft-Gault)", f"{fmt(r.valor, 1)} mL/min")
    c.alertas(r.alertas)
    c.passos(r.passos)
    st.markdown("**Ajustes previstos em bula para os fármacos do guia**")
    linhas = []
    extras: list[str] = []
    for ajuste in calc.ajustes_renais(r.valor):
        fontes = "; ".join(rotulo(ref) for ref in ajuste.referencias)
        linhas.append(f"- **{ajuste.farmaco}:** {ajuste.texto} *[{fontes}]*")
        extras.extend(ajuste.referencias)
    st.markdown("\n".join(linhas))
    _rodape("clcr", tuple(extras))


# --------------------------------------------------------------------------- superfície corporal


def _superficie() -> None:
    _cabecalho("superficie")
    p = _paciente()
    if _faltando({"peso": p["peso"], "altura": p["altura"]}):
        _rodape("superficie")
        return
    try:
        sc = calc.superficie_corporal(p["peso"], p["altura"])
    except calc.EntradaInvalida as erro:
        st.error(str(erro))
        _rodape("superficie")
        return
    col1, col2 = st.columns(2)
    col1.metric("Mosteller", f"{fmt(sc.mosteller_m2, 2)} m²")
    col2.metric("DuBois", f"{fmt(sc.dubois_m2, 2)} m²")
    c.passos(sc.passos)
    _rodape("superficie")


# --------------------------------------------------------------------------- queimados


def _queimados() -> None:
    _cabecalho("queimados")
    p = _paciente()
    pct = st.number_input(
        "Superfície corporal queimada (% SCQ) — sem contar queimaduras superficiais",
        min_value=0.0,
        max_value=100.0,
        value=None,
        step=1.0,
        format="%.1f",
        key="q_pct",
    )
    fator = st.radio(
        "Fórmula",
        options=[4.0, 2.0],
        format_func=lambda f: calc.FATORES_REPOSICAO[f],
        key="q_fator",
    )
    if _faltando({"peso": p["peso"]}) or pct is None:
        if pct is None:
            st.info("Informe a % de superfície corporal queimada.")
        _rodape("queimados")
        return
    adulto = None if p["idade"] is None else p["idade"] >= 18
    try:
        r = calc.reposicao_queimado(p["peso"], pct, fator, adulto)
    except calc.EntradaInvalida as erro:
        st.error(str(erro))
        _rodape("queimados")
        return
    st.metric("Volume estimado em 24 h", f"{fmt(r.total_24h_ml, 0)} mL")
    col1, col2 = st.columns(2)
    col1.metric("Primeiras 8 h", f"{fmt(r.taxa_primeiras_8h_ml_h, 1)} mL/h", help=f"{fmt(r.volume_primeiras_8h_ml, 0)} mL no período")
    col2.metric("16 h seguintes", f"{fmt(r.taxa_16h_seguintes_ml_h, 1)} mL/h", help=f"{fmt(r.volume_16h_seguintes_ml, 0)} mL no período")
    c.alertas(r.alertas)
    c.passos(r.passos)
    _rodape("queimados", r.referencias)


# --------------------------------------------------------------------------- potássio


def _potassio() -> None:
    _cabecalho("potassio")
    k = st.number_input(
        "Potássio sérico (mmol/L — igual a mEq/L para o potássio)",
        min_value=0.0,
        max_value=20.0,
        value=None,
        step=0.1,
        format="%.1f",
        key="k_serico",
    )
    if k is not None:
        try:
            cl = calc.classificar_potassio(k)
        except calc.EntradaInvalida as erro:
            st.error(str(erro))
        else:
            caixa = {"critico": st.error, "alerta": st.warning}.get(cl.nivel, st.info)
            caixa(f"**{cl.categoria}**")
            st.markdown("\n".join(f"- {m}" for m in cl.mensagens))

    st.markdown("##### Conferir solução de potássio IV (adulto)")
    col1, col2, col3 = st.columns(3)
    mmol = col1.number_input("Potássio na solução (mmol)", min_value=0.0, value=None, step=1.0, format="%.1f", key="kcl_mmol")
    volume = col2.number_input("Volume final (mL)", min_value=0.0, value=None, step=50.0, format="%.0f", key="kcl_volume")
    vazao = col3.number_input("Vazão (mL/h)", min_value=0.0, value=None, step=10.0, format="%.1f", key="kcl_vazao")
    central = st.checkbox("Acesso venoso central", key="kcl_central")
    ecg = st.checkbox("ECG contínuo disponível", key="kcl_ecg")
    if None not in (mmol, volume, vazao):
        try:
            v = calc.verificar_infusao_potassio(mmol, volume, vazao, central, ecg, k)
        except calc.EntradaInvalida as erro:
            st.error(str(erro))
        else:
            a, b = st.columns(2)
            a.metric("Concentração", f"{fmt(v.concentracao_mmol_l, 1)} mmol/L")
            b.metric("Velocidade", f"{fmt(v.taxa_mmol_h, 1)} mmol/h")
            if v.alertas:
                for texto in v.alertas:
                    st.error(texto)
            else:
                st.success("Dentro dos limites das referências consultadas. Não substitui o protocolo institucional.")
            c.passos(v.passos)
    else:
        st.caption("Preencha potássio, volume e vazão para conferir a solução.")

    st.markdown("##### Volume de solução concentrada")
    col1, col2 = st.columns(2)
    desejado = col1.number_input("Potássio desejado (mmol)", min_value=0.0, value=None, step=1.0, format="%.1f", key="kcl_desejado")
    conc = col2.number_input(
        "Concentração da ampola (mmol/mL)",
        min_value=0.0,
        value=None,
        step=0.01,
        format="%.3f",
        key="kcl_conc_ampola",
        help=f"Confira o rótulo. Por cálculo, KCl 19,1% ≈ {fmt(mmol_por_ml_kcl(19.1), 2)} mmol/mL (191 mg/mL ÷ 74,55 mg/mmol).",
    )
    if desejado is not None and conc is not None:
        try:
            r = calc.volume_concentrado_potassio(desejado, conc)
        except calc.EntradaInvalida as erro:
            st.error(str(erro))
        else:
            st.metric("Volume da solução concentrada", f"{fmt(r.valor, 2)} mL")
            c.alertas(r.alertas)
    _rodape("potassio")


# --------------------------------------------------------------------------- página


def render() -> None:
    st.subheader("🧮 Calculadoras")
    st.caption("Os resultados mostram cada passo do cálculo para conferência. Nenhum valor é preenchido por padrão.")
    abas = st.tabs(["Infusão", "Função renal", "Superfície corporal", "Queimados", "Potássio"])
    with abas[0]:
        _infusao()
    with abas[1]:
        _clcr()
    with abas[2]:
        _superficie()
    with abas[3]:
        _queimados()
    with abas[4]:
        _potassio()
