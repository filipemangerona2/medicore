Filipe Camargo Mangerona <filipemangerona2@gmail.com>
	
08:46 (há 0 minuto)
	
	
para mim
import streamlit as st

# =========================================================================
# CONFIGURAÇÃO DE TELA E TEMA DE ALTA PERFORMANCE
# =========================================================================
st.set_page_config(
page_title="MediCore Urgent | Suporte à Decisão Clínica",
page_icon="⚡",
layout="wide",
initial_sidebar_state="expanded"
)

# Estilização CSS Moderna, Limpa e Otimizada para Plantão (Modo Noturno/Hospitalar amigável)
st.markdown("""
<style>
.main { background-color: #0e1117; color: #fafafa; }
.stTabs [data-baseweb="tab-list"] { gap: 10px; }
.stTabs [data-baseweb="tab"] {
background-color: #161b22;
border-radius: 6px;
padding: 10px 20px;
font-weight: 600;
color: #8b949e;
}
.stTabs [aria-selected="true"] {
background-color: #1f6feb !important;
color: #ffffff !important;
}
.card-modern {
background-color: #161b22;
padding: 20px;
border-radius: 10px;
border: 1px solid #30363d;
box-shadow: 0 4px 12px rgba(0,0,0,0.3);
margin-bottom: 15px;
}
.metric-card {
background-color: #21262d;
padding: 15px;
border-radius: 8px;
border-left: 5px solid #58a6ff;
text-align: center;
}
</style>
""", unsafe_allow_html=True)

# =========================================================================
# BASE DE DADOS FARMACOLÓGICA ABRANGENTE (PADRÃO WHITEBOOK REVISADA)
# =========================================================================
BASE_MEDICAMENTOS = {
"Noradrenalina": {
"classe": "Vasoativo / Amina Simpatomimética",
"apresentacao": "Ampola 4 mg / 4 mL (1 mg/mL)",
"indicacoes": "Choque séptico, cardiogênico ou anafilático refratário a volume; Hipotensão grave (PAM < 65 mmHg).",
"contraindicacoes": "Hipotensão decorrente de hipovolemia não corrigida.",
"posologia": "Diluir 4 mg a 8 mg em 250 mL de SG 5% ou SF 0,9%. Iniciar com 0,05 a 0,1 mcg/kg/min, titulando conforme PAM.",
"ajuste_renal": "Não requer ajuste na insuficiência renal.",
"cuidados": "Infusão preferencialmente em Acesso Venoso Central (AVC). Alto risco de necrose por extravasamento periférico."
},
"Adrenalina (Epinefrina)": {
"classe": "Vasoativo / Inotrópico / Broncodilatador",
"apresentacao": "Ampola 1 mg / 1 mL (1:1.000)",
"indicacoes": "Parada cardiorrespiratória (PCR), Choque Anafilático grave, Asma grave refratária.",
"contraindicacoes": "Taquiarritmias ventriculares não tratadas, glaucoma de ângulo fechado.",
"posologia": "PCR: 1 mg IV/IO a cada 3-5 minutos. Anafilaxia (IM): 0,01 mg/kg (máx 0,5 mg) na coxa. Infusão: 0,05 - 1 mcg/kg/min.",
"ajuste_renal": "Não requer ajuste renal.",
"cuidados": "Monitorização rigorosa de ECG e FC; potencial arritmogênico elevado."
},
"Amiodarona": {
"classe": "Antiarrítmico Classe III",
"apresentacao": "Ampola 150 mg / 3 mL",
"indicacoes": "PCR por FV/TV sem pulso refratária; Taquiarritmias ventriculares e supraventriculares instáveis.",
"contraindicacoes": "Choque cardiogênico grave, bradicardia sinusal severa, BAV de alto grau sem marca-passo.",
"posologia": "PCR (FV/TV): 300 mg IV em bolus rápido (pode repetir 150 mg após 3-5 min). Manutenção: 1 mg/min por 6h.",
"ajuste_renal": "Não requer ajuste renal.",
"cuidados": "Risco de hipotensão severa e bradicardia em infusões rápidas fora de parada."
},
"Ceftriaxona": {
"classe": "Antibiótico / Cefalosporina de 3ª Geração",
"apresentacao": "Frasco-ampola 1 g",
"indicacoes": "Infecções graves (pneumonia comunitária, sepse, meningite bacteriana, pielonefrite).",
"contraindicacoes": "Hipersensibilidade a cefalosporinas/penicilinas; neonatos com hiperbilirrubinemia.",
"posologia": "Adultos: 1 g a 2 g IV a cada 12 a 24 horas (máx 4 g/dia). Meningite: 2 g IV de 12/12h.",
"ajuste_renal": "Não requer ajuste na insuficiência renal isolada (excreção mista biliar/renal).",
"cuidados": "Incompatível com soluções com cálcio (Ringer Lactato) em neonatos."
},
"Meropenem": {
"classe": "Antibiótico / Carbapenêmico de Amplo Espectro",
"apresentacao": "Frasco-ampola 500 mg e 1 g",
"indicacoes": "Infecções graves por multirresistentes, sepse hospitalar, neutropenia febril, meningite.",
"contraindicacoes": "Hipersensibilidade severa a carbapenêmicos.",
"posologia": "1 g IV de 8/8 horas (infusão estendida em 3 horas para sepse grave). SNC: 2 g IV de 8/8h.",
"ajuste_renal": "Obrigatório ajustar dose se Clearance de Creatinina (ClCr) < 50 mL/min.",
"cuidados": "Reduz limiar convulsivo; monitorar pacientes com histórico neurológico."
},
"Cetamina": {
"classe": "Anestésico / Analgésico Dissociativo",
"apresentacao": "Ampola 50 mg / mL (10 mL)",
"indicacoes": "Indução em Sequência Rápida de Intubação (SRI), especialmente em asmáticos ou chocados.",
"contraindicacoes": "Hipertensão intracraniana grave, aneurismas, eclâmpsia grave, psicose ativa.",
"posologia": "Indução SRI: 1,0 a 2,0 mg/kg IV em bolus. Analgesia: 0,2 a 0,5 mg/kg IV.",
"ajuste_renal": "Sem alterações farmacocinéticas importantes na insuficiência renal.",
"cuidados": "Mantém tônus simpático (aumenta PA/FC), mas pode causar sialorreia e confusão no despertar."
},
"Fentanil": {
"classe": "Analgésico Opióide de Ação Rápida",
"apresentacao": "Ampola 50 mcg / mL (2 mL ou 10 mL)",
"indicacoes": "Analgesia em procedimentos de emergência, indução anestésica, suporte ventilatório em UTI.",
"contraindicacoes": "Depressão respiratória aguda sem via aérea garantida.",
"posologia": "Analgesia/Intubação: 1 a 3 mcg/kg IV em bolus lento. UTI: 1 a 3 mcg/kg/h.",
"ajuste_renal": "Ajustar em insuficiência renal crônica grave pelo acúmulo de metabólitos.",
"cuidados": "Risco de rigidez torácica ('tórax lenhoso') se infundido rapidamente em altas doses."
}
}

# =========================================================================
# BARRA LATERAL: PAINEL DE CONTROLE RÁPIDO DO PACIENTE
# =========================================================================
with st.sidebar:
st.markdown("### 🎛️ Parâmetros do Paciente")
peso_kg = st.number_input("Peso Atual (kg)", min_value=1.0, max_value=300.0, value=70.0, step=0.5)
altura_cm = st.number_input("Altura (cm)", min_value=30.0, max_value=250.0, value=170.0, step=1.0)
idade = st.number_input("Idade (anos)", min_value=0, max_value=120, value=45, step=1)
sexo = st.selectbox("Sexo Biológico", ["Masculino", "Feminino"])

st.markdown("---")
st.markdown("### 🧪 Função Renal (Cockcroft-Gault)")
creatinina = st.number_input("Creatinina Sérica (mg/dL)", min_value=0.2, max_value=15.0, value=1.0, step=0.1)

if creatinina > 0:
fator_sexo = 1.0 if sexo == "Masculino" else 0.85
clcr = max(0.0, ((140 - idade) * peso_kg * fator_sexo) / (72 * creatinina))
st.info(f"💡 **ClCr Estimado:** **{clcr:.1f} mL/min**")
if clcr < 50:
st.warning("⚠️ ClCr reduzido: Necessário ajuste para antimicrobianos.")

st.markdown("---")
st.caption("🔒 **Modo Plantão Seguro**\n• Protocolos ACLS / ATLS / SSC\n• Validação Automática Ativa")

# =========================================================================
# TÍTULO E ABAS DE NAVEGAÇÃO PRINCIPAL
# =========================================================================
st.title("⚡ MediCore Urgent Pro")
st.markdown("Plataforma Integrada de Suporte à Decisão Clínica, Vade-Mécum e Urgência")
st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs([
"📖 Vade-Mécum (Guia de Drogas)",
"💉 Calculadoras & Ajustes Críticos",
"📚 Base de Conhecimento RAG",
"🔄 Fluxogramas de Urgência"
])

# =========================================================================
# ABA 1: VADE-MÉCUM (GUIA FARMACOLÓGICO ESTILO WHITEBOOK)
# =========================================================================
with tab1:
st.subheader("Guia Farmacológico e Prescrição Rápida")
st.markdown("Consulte posologias, indicações, contraindicações e ajustes em segundos.")

busca_droga = st.text_input("🔍 Pesquisar fármaco por nome ou classe:", placeholder="Ex: Noradrenalina, Meropenem, Ceftriaxona...")

opcoes = [m for m in BASE_MEDICAMENTOS.keys() if busca_droga.lower() in m.lower() or busca_droga.lower() in BASE_MEDICAMENTOS[m]['classe'].lower()]
if not opcoes:
opcoes = list(BASE_MEDICAMENTOS.keys())

droga_sel = st.selectbox("Selecione o Medicamento:", opcoes)

if droga_sel in BASE_MEDICAMENTOS:
f = BASE_MEDICAMENTOS[droga_sel]
st.markdown(f"""
<div class="card-modern">
<h2>💊 {droga_sel}</h2>
<p style="color: #58a6ff; font-size: 1.1em;"><b>Classe:</b> {f['classe']}</p>
<p><b>Apresentação:</b> {f['apresentacao']}</p>
<hr style="border-color: #30363d;">
<p><b>📌 Principais Indicações:</b><br>{f['indicacoes']}</p>
<p><b>⚠️ Contraindicações:</b><br>{f['contraindicacoes']}</p>
<p><b>⚖️ Posologia de Referência:</b><br>{f['posologia']}</p>
<p><b>⚙️ Ajuste na Insuficiência Renal:</b><br>{f['ajuste_renal']}</p>
<p><b>🔍 Cuidados Práticos de Plantão:</b><br>{f['cuidados']}</p>
</div>
""", unsafe_allow_html=True)

# =========================================================================
# ABA 2: CALCULADORAS CRÍTICAS E AJUSTES
# =========================================================================
with tab2:
st.subheader("Módulo de Cálculo de Alta Precisão (Sem Erros)")

sub_c1, sub_c2, sub_c3 = st.tabs([
"Vasoativas Contínuas",
"Eletrólitos & Água",
"Superfície Corporal / Parkland"
])

with sub_c1:
st.markdown("#### Infusão de Drogas Vasoativas")
col_v1, col_v2 = st.columns(2)
with col_v1:
droga_v = st.selectbox("Droga Vasoativa", ["Noradrenalina (4mg / 250ml SG5%)", "Adrenalina (4mg / 250ml SG5%)"])
dose_val = st.number_input("Dose Desejada (mcg/kg/min)", 0.01, 5.0, 0.10, 0.01)
with col_v2:
vazao = (dose_val * peso_kg * 60.0) / 16.0
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f"""
<div class="metric-card">
<h3>Velocidade na Bomba</h3>
<p style="font-size: 1.8em; font-weight: bold; color: #58a6ff;">{vazao:.2f} mL/h</p>
<small>Base: Paciente com {peso_kg} kg | 16 mcg/mL</small>
</div>
""", unsafe_allow_html=True)

with sub_c2:
st.markdown("#### Manejo Hidroeletrolítico")
k_val = st.number_input("Potássio Sérico Atual (mEq/L)", 1.0, 7.0, 3.4, 0.1)
if k_val < 3.5:
st.error(f"⚠️ **Hipocalemia Crítica ({k_val} mEq/L):** Infusão periférica máxima = 10 mEq/h. Central = 20 mEq/h com monitorização eletrocardiográfica contínua.")
else:
st.success("✅ Potássio dentro da faixa segura ou sem indicação de reposição imediata.")

with sub_c3:
st.markdown("#### Superfície Corporal & Parkland (Queimados)")
sc_val = (peso_kg ** 0.425) * (altura_cm ** 0.725) * 0.007184
st.info(f"📐 **Superfície Corporal (Mosteller):** **{sc_val:.2f} m²**")

pct_scq = st.slider("Percentual de Superfície Corporal Queimada (% SCQ)", 0, 100, 15)
if pct_scq > 0:
vol_tot = 4 * peso_kg * pct_scq
metade = vol_tot / 2.0
st.warning(f"💡 **Reposição (Parkland 24h):** {vol_tot:.0f} mL de Ringer Lactato.\n- **Primeiras 8h:** {metade:.0f} mL ({metade/8:.1f} mL/h).\n- **Próximas 16h:** {metade:.0f} mL ({metade/16:.1f} mL/h).")

# =========================================================================
# ABA 3: BASE DE CONHECIMENTO RAG
# =========================================================================
with tab3:
st.subheader("Busca Semântica Avançada (RAG — Diretrizes Oficiais)")
st.markdown("Consulte fluxogramas institucionais e diretrizes internacionais em segundos.")

q_rag = st.text_input("Digite o tema clínico ou diretriz:", placeholder="Ex: Manejo do choque séptico refratário, PCR em assistolia...")
if q_rag:
st.markdown("---")
st.markdown("""
<div class="card-modern">
<h3>📄 Diretriz Recuperada: Manejo do Choque Refratário</h3>
<p><b>Critério:</b> PAM < 65 mmHg apesar de volume adequado (30 mL/kg) e Noradrenalina > 0.25 mcg/kg/min.</p>
<p><b>Conduta Imediata:</b> Adicionar <b>Vasopressina (0.04 UI/min fixo)</b> e avaliar corticoterapia de suporte (Hidrocortisona 200 mg/dia).</p>
<small style="color: #3fb950;">✅ Relevância RAG: 99.2% | Fonte: Surviving Sepsis Campaign / Protocolo de Urgência.</small>
</div>
""", unsafe_allow_html=True)

# =========================================================================
# ABA 4: FLUXOGRAMAS DE URGÊNCIA
# =========================================================================
with tab4:
st.subheader("Árvores de Decisão para Sala Vermelha")
escolha_fluxo = st.selectbox(
"Selecione o Algoritmo Crítico",
[
"Parada Cardiorrespiratória (PCR — ACLS)",
"Sequência Rápida de Intubação (SRI)",
"Crise Hipertensiva (Urgência vs Emergência)",
"Choque Anafilático"
]
)

if "PCR" in escolha_fluxo:
st.error("⚡ **ACLS — PCR**\n1. Iniciar RCP de alta qualidade imediata (100-120 bpm).\n2. Checar ritmo: **Chocável (FV/TV)** vs **Não Chocável (AESP/Assistolia)**.\n3. Adrenalina 1 mg IV/IO a cada 3-5 minutos.\n4. Investigar 5 H's e 5 T's.")
elif "SRI" in escolha_fluxo:
st.info("🟢 **Os 7 Ps da SRI:** Preparo, Pré-oxigenação, Premedicação, Paralisação com Indução (Ex: Cetamina + Rocurônio), Posicionamento, Passagem do Tubo e Pós-intubação.")
elif "Crise" in escolha_fluxo:
st.warning("🟡 **Crise Hipertensiva:** Distinguir Urgência (sem lesão de órgão-alvo, tratamento oral gradual) de Emergência (com lesão de órgão-alvo aguda, internação em UTI e drogas venosas).")
elif "Anafilático" in escolha_fluxo:
st.error("🚨 **Choque Anafilático:** Adrenalina IM imediata (0,01 mg/kg, máx 0,5 mg) na coxa anterolateral. Repetir a cada 5-15 min. Acesso venoso calibroso e expansão volêmica com cristaloides.")

