"""MediCore Urgent Pro — ponto de entrada do Streamlit.

Este arquivo só monta a página. A lógica fica no pacote ``medicore``:
cálculos em ``calculos.py``, conteúdo clínico em ``farmacos.py`` e ``fluxogramas.py``,
fontes em ``referencias.py`` e interface em ``medicore/ui``.
"""

import streamlit as st

from medicore import __version__
from medicore.ui import (
    componentes,
    pagina_auditoria,
    pagina_busca,
    pagina_calculadoras,
    pagina_farmacos,
    pagina_fluxogramas,
)

TEXTO_CIENCIA = (
    "Sou profissional ou estudante da área da saúde e entendo que este aplicativo é um protótipo em revisão: "
    "o conteúdo está PENDENTE DE REVISÃO CLÍNICA e não deve ser usado para decisões assistenciais."
)

st.set_page_config(page_title="MediCore Urgent Pro", page_icon="⚕️", layout="wide")

st.title("⚕️ MediCore Urgent Pro")
st.caption(f"Consulta rápida para urgência · versão {__version__}")
st.warning(componentes.AVISO_GERAL)

if not st.checkbox(TEXTO_CIENCIA, key="ciencia"):
    st.info("Marque a declaração acima para acessar o conteúdo.")
    st.stop()

pagina_calculadoras.render_dados_paciente()

abas = st.tabs(["💊 Fármacos", "🧮 Calculadoras", "🔀 Fluxogramas", "🔎 Busca", "📋 Auditoria"])
with abas[0]:
    pagina_farmacos.render()
with abas[1]:
    pagina_calculadoras.render()
with abas[2]:
    pagina_fluxogramas.render()
with abas[3]:
    pagina_busca.render()
with abas[4]:
    pagina_auditoria.render()
