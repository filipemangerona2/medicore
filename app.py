import streamlit as st

st.set_page_config(page_title="MediCore Urgent Pro", page_icon="⚡", layout="wide")

st.title("⚡ MediCore Urgent Pro - Plataforma Avançada de Suporte à Decisão Médica")
st.markdown("---")

# Barra Lateral: Parâmetros do Paciente
st.sidebar.header("🎛️ Parâmetros do Paciente")
peso = st.sidebar.number_input("Peso (kg)", 1.0, 300.0, 70.0)
idade = st.sidebar.number_input("Idade (anos)", 0, 120, 45)
funcao_renal = st.sidebar.selectbox("Função Renal / Clearance", ["Normal (> 50 mL/min)", "Comprometida (10-50 mL/min)", "Dialítico / Grave (< 10 mL/min)"])

# Abas Principais Abrangentes
tab1, tab2, tab3, tab4 = st.tabs([
"📖 Vade-Mécum & Posologia",
"🧠 Fluxogramas de Conduta",
"💉 Calculadoras de Urgência",
"⚡ Raciocínio Clínico & Sepse"
])

with tab1:
st.subheader("Guia Farmacológico e Ajustes de Dose")
droga = st.selectbox("Selecione o Fármaco de Urgência:", [
"Noradrenalina", "Adrenalina", "Amiodarona", "Ceftriaxona", "Fentanil", "Midazolam"
])

if droga == "Noradrenalina":
st.info("""
**Classe:** Amina simpatomimética / Vasopressor de escolha
**Indicação Principal:** Choque séptico refratário, choque distributivo e hipotensão grave.
**Diluição Padrão:** 4 mg a 8 mg em 250 mL de SG 5% ou SF 0,9%.
**Posologia Inicial:** 0,05 a 0,1 mcg/kg/min, titulado conforme PAM ≥ 65 mmHg.
**Cuidados:** Exige acesso venoso profundo preferencial; risco de necrose por extravasamento.
""")
elif droga == "Adrenalina":
st.info("""
**Classe:** Agente vasoativo / Inotrópico / Broncodilatador
**Indicação Principal:** Parada cardiorrespiratória (PCR), anafilaxia grave, choque cardiogênico.
**Posologia PCR:** 1 mg IV a cada 3 a 5 minutos.
**Posologia Anafilaxia:** 0,3 a 0,5 mg IM (1:1000).
""")
elif droga == "Amiodarona":
st.info("""
**Classe:** Antiarrítmico Classe III
**Indicação Principal:** FV/TV sem pulso refratária a choque; taquiarritmias sintomáticas.
**Posologia PCR:** 300 mg IV em bolus rápido (diluído em SG5%), seguido de dose de manutenção se necessário.
""")
elif droga == "Ceftriaxona":
st.info("""
**Classe:** Antibiótico Cefalosporina de 3ª geração
**Indicação Principal:** Sepse de foco pulmonar/urinário, meningite, infecções graves comunitárias.
**Posologia Padrão:** 1g a 2g IV a cada 12 a 24 horas.
""")
elif droga == "Fentanil":
st.info("""
**Classe:** Analgésico opioide potente de ação rápida
**Indicação Principal:** Analgesia para intubação orotraqueal (IOT) e procedimentos de emergência.
**Posologia:** 1 a 2 mcg/kg IV em bolus lento.
""")
elif droga == "Midazolam":
st.info("""
**Classe:** Benzodiazepínico sedativo / Hipnótico / Amnésico
**Indicação Principal:** Sedação para IOT, controle de crise convulsiva refratária.
**Posologia:** 0,05 a 0,15 mg/kg IV.
""")

with tab2:
st.subheader("Fluxogramas de Decisão Rápida em Urgência")
fluxo = st.selectbox("Escolha o Protocolo Clínico:", ["Manejo do Choque Séptico (Surviving Sepsis)", "Abordagem da PCR (ACLS)", "Crise Hipertensiva"])

if fluxo == "Manejo do Choque Séptico (Surviving Sepsis)":
st.markdown("""
### 🔄 Fluxograma: Sepse e Choque Séptico (Hora 1)
1. **Reconhecimento Imediato:** Avaliar critérios qSOFA ou SOFA e sinais de hipoperfusão (lactato > 2 mmol/L).
2. **Coleta de Exames:** Lactato sérico, hemoculturas (antes do antibiótico se não atrasar > 45 min), hemograma, função renal, coagulograma.
3. **Antibioticoterapia Precoce:** Administrar antibiótico de largo espectro na primeira hora.
4. **Reposição Volêmica:** 30 mL/kg de cristaloide em caso de hipotensão ou lactato ≥ 4.
5. **Drogas Vasoativas:** Se persistir PAM < 65 mmHg após volume, iniciar **Noradrenalina** como primeira escolha.
""")
elif fluxo == "Abordagem da PCR (ACLS)":
st.markdown("""
### 🔄 Fluxograma: Parada Cardiorrespiratória (ACLS)
1. **Checar Segurança e Responsividade** -> Chamar ajuda / Trazer desfibrilador.
2. **Iniciar RCP de Alta Qualidade:** 100-120 bpm, profundidade 5-6 cm, retorno total do tórax.
3. **Checar Ritmo:**
- *FV / TV sem pulso:* Choque imediato ➔ RCP por 2 min ➔ Adrenalina a cada 3-5 min ➔ Amiodarona no 2º choque.
- *Asistolia / AESP:* RCP imediata ➔ Adrenalina precoce ➔ Investigar 5 Hs e 5 Ts.
""")
else:
st.markdown("""
### 🔄 Fluxograma: Crise Hipertensiva
1. **Diferenciar:** Urgência Hipertensiva vs. Emergência Hipertensiva (presença de lesão de órgão-alvo aguda).
2. **Urgência:** Redução gradual da PA ao longo de 24-48h com medicação oral.
3. **Emergência:** Internação em UTI, monitorização invasiva e uso de drogas vasoativas endovenosas (ex: Nitroprussiato ou Nitroglicerina).
""")

with tab3:
st.subheader("Calculadoras Médicas Avançadas de Urgência")
st.markdown("#### 💉 Infusão Contínua de Drogas Vasoativas")
dose_desejada = st.number_input("Dose Desejada (mcg/kg/min)", 0.01, 5.0, 0.10, 0.01)
vazao_calculada = (dose_desejada * peso * 60.0) / 16.0
st.success(f"💡 **Velocidade na Bomba de Infusão:** **{vazao_calculada:.2f} mL/h** (Considerando padrão de 4 mg em 250 mL).")

st.markdown("---")
st.markdown("#### 🫁 Clearance de Creatinina Estimado (Cockcroft-Gault)")
creatinina = st.number_input("Creatinina Sérica (mg/dL)", 0.2, 15.0, 1.0)
sexo = st.selectbox("Sexo Biológico", ["Masculino", "Feminino"])

if sexo == "Feminino":
fator_sexo = 0.85
else:
fator_sexo = 1.0

cl_cr = ((140 - idade) * peso * fator_sexo) / (72.0 * creatinina)
st.info(f"📊 **Clearance Estimado:** **{cl_cr:.1f} mL/min**")

with tab4:
st.subheader("🧠 Raciocínio Clínico e Suporte à Conduta")
st.markdown("""
Esta seção serve como diretriz mental rápida para tomada de decisão em cenários críticos:
* **Avaliação Primária (ABCDE):** Vias aéreas, Respiração, Circulação, Incapacidade (neurológica), Exposição.
* **Segurança do Paciente:** Checar sempre alergias medicamentosas graves e interações antes de infundir drogas de alta vigilância.
* **Reavaliação Contínua:** Resposta hemodinâmica à volemia e drogas vasoativas a cada 5 a 15 minutos em pacientes instáveis.
""")
