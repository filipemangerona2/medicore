import streamlit as st

st.set_page_config(page_title="MediCore Urgent Pro", page_icon="⚡", layout="wide")

st.title("⚡ MediCore Urgent Pro")
st.markdown("### Plataforma de Suporte à Decisão Clínica e Urgência")
st.markdown("---")

st.sidebar.header("🎛️ Parâmetros do Paciente")
peso = st.sidebar.number_input("Peso (kg)", 1.0, 300.0, 70.0)

st.subheader("📖 Guia Farmacológico Rápido")
droga = st.selectbox("Selecione o Fármaco:", ["Noradrenalina", "Adrenalina", "Amiodarona", "Ceftriaxona"])
if droga == "Noradrenalina":
st.info("Classe: Vasoativo\nIndicação: Choque séptico / Hipotensão grave.\nPosologia: Diluir 4mg a 8mg em 250ml SG5%. Iniciar 0.05 a 0.1 mcg/kg/min.")
elif droga == "Adrenalina":
st.info("Classe: Vasoativo / Inotrópico\nIndicação: PCR / Anafilaxia.\nPosologia: PCR: 1mg IV a cada 3-5 min.")
elif droga == "Amiodarona":
st.info("Classe: Antiarrítmico\nIndicação: PCR por FV/TV.\nPosologia: 300 mg IV em bolus rápido.")
elif droga == "Ceftriaxona":
st.info("Classe: Antibiótico\nIndicação: Infecções graves.\nPosologia: 1g a 2g IV a cada 24h.")

st.markdown("---")
st.subheader("💉 Calculadora de Infusão Contínua")
dose_desejada = st.number_input("Dose (mcg/kg/min)", 0.01, 5.0, 0.10, 0.01)
vazao_calculada = (dose_desejada * peso * 60.0) / 16.0
st.success(f"Velocidade recomendada na bomba: {vazao_calculada:.2f} mL/h")
