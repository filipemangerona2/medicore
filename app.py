import streamlit as st

st.set_page_config(page_title="MediCore Urgent Pro", page_icon="⚡", layout="wide")

st.title("⚡ MediCore Urgent Pro - Plataforma Médica de Urgência")
st.markdown("---")

# Barra Lateral de Parâmetros
st.sidebar.header("🎛️ Parâmetros do Paciente")
peso = st.sidebar.number_input("Peso (kg)", 1.0, 300.0, 70.0)
idade = st.sidebar.number_input("Idade (anos)", 0, 120, 45)

# Seção 1: Guia Farmacológico
st.markdown("## 📖 Guia Farmacológico e Condutas")
droga = st.selectbox("Selecione o Fármaco de Urgência:", ["Noradrenalina", "Adrenalina", "Amiodarona", "Ceftriaxona"])

if droga == "Noradrenalina":
    st.info("Classe: Vasopressor\nIndicação: Choque séptico / Hipotensão grave.\nPosologia: 0.05 a 0.1 mcg/kg/min.")
if droga == "Adrenalina":
    st.info("Classe: Inotrópico / Vasoativo\nIndicação: PCR / Anafilaxia.\nPosologia PCR: 1 mg IV a cada 3-5 min.")
if droga == "Amiodarona":
    st.info("Classe: Antiarrítmico\nIndicação: FV/TV sem pulso.\nPosologia: 300 mg IV em bolus rápido.")
if droga == "Ceftriaxona":
    st.info("Classe: Antibiótico\nIndicação: Infecções graves.\nPosologia: 1g a 2g IV a cada 24h.")

st.markdown("---")

# Seção 2: Calculadora de Vasoativas
st.markdown("## 💉 Calculadora de Infusão Contínua")
dose_desejada = st.number_input("Dose (mcg/kg/min)", 0.01, 5.0, 0.10, 0.01)
vazao_calculada = (dose_desejada * peso * 60.0) / 16.0
st.success(f"Velocidade recomendada na bomba: {vazao_calculada:.2f} mL/h")

st.markdown("---")

# Seção 3: Clearance de Creatinina
st.markdown("## 🫁 Clearance de Creatinina (Cockcroft-Gault)")
creatinina = st.number_input("Creatinina Sérica (mg/dL)", 0.2, 15.0, 1.0)
sexo = st.selectbox("Sexo Biológico", ["Masculino", "Feminino"])

fator = 0.85 if sexo == "Feminino" else 1.0
cl_cr = ((140 - idade) * peso * fator) / (72.0 * creatinina)
st.info(f"Clearance Estimado: {cl_cr:.1f} mL/min")
