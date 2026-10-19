import streamlit as st

st.set_page_config(page_title="MediCore Urgent Pro", page_icon="⚡", layout="wide")

st.title("⚡ MediCore Urgent Pro")
st.markdown("### Plataforma de Suporte à Decisão Clínica e Urgência")
st.markdown("---")

st.sidebar.header("🎛️ Parâmetros do Paciente")
peso = st.sidebar.number_input("Peso (kg)", 1.0, 300.0, 70.0)
altura = st.sidebar.number_input("Altura (cm)", 30.0, 250.0, 170.0)

tab1, tab2 = st.tabs(["📖 Vade-Mécum", "💉 Calculadoras"])

with tab1:
st.subheader("Guia Farmacológico Rápido")
droga = st.selectbox("Selecione:", ["Noradrenalina", "Adrenalina"])
if droga == "Noradrenalina":
st.info("Noradrenalina: Diluir 4mg em 250ml SG5%. Iniciar 0.05 mcg/kg/min.")
else:
st.info("Adrenalina: PCR 1mg IV a cada 3-5 min.")

with tab2:
st.subheader("Calculadora de Vasoativas")
dose = st.number_input("Dose (mcg/kg/min)", 0.01, 5.0, 0.10, 0.01)
vazao = (dose * peso * 60.0) / 16.0
st.success(f"Velocidade: {vazao:.2f} mL/h")
