import streamlit as st

st.set_page_config(page_title='MediCore Urgent Pro', page_icon='⚕️', layout='wide')
st.title('MediCore Urgent Pro')
st.warning('Protótipo educacional em validação. Não utilizar para prescrição ou decisão clínica em pacientes.')

st.sidebar.header('Parâmetros')
peso = st.sidebar.number_input('Peso (kg)', min_value=1.0, max_value=300.0, value=70.0)
idade = st.sidebar.number_input('Idade (anos)', min_value=18, max_value=120, value=45)

st.header('Guia farmacológico')
st.info('Módulo em revisão clínica. Protocolos e doses serão disponibilizados após validação por profissionais responsáveis.')

st.header('Calculadora matemática de infusão — demonstração')
st.caption('Exemplo matemático somente. Confira prescrição, unidade e concentração real antes de qualquer uso clínico.')
dose = st.number_input('Dose informada (mcg/kg/min)', min_value=0.0, max_value=100.0, value=0.1, step=0.01)
concentracao = st.number_input('Concentração informada (mcg/mL)', min_value=0.01, max_value=100000.0, value=16.0)
vazao = dose * peso * 60 / concentracao
st.metric('Resultado matemático (mL/h)', f'{vazao:.2f}')
st.code('mL/h = dose (mcg/kg/min) × peso (kg) × 60 / concentração (mcg/mL)')

st.header('Estimativa de função renal — em validação')
st.info('Cálculo de Cockcroft-Gault temporariamente indisponível até inclusão de critérios de peso, limitações e testes clínicos.')
