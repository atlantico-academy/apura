# bibliotecas
import streamlit as st # site
from st_on_hover_tabs import on_hover_tabs # menus laterais
from src.app import verificador, analise_exploratoria, analise_comparativa, sobre

# configuração
st.set_page_config(layout='wide') # página em modo amplo

# st.header("Custom tab component for on-hover navigation bar")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

# menus laterais
with st.sidebar:
    tabs = on_hover_tabs(tabName=['Detector', 'Análise Exploratória', 'Análise Comparativa', 'Sobre'], 
                         iconName=['dashboard', 'search', 'analytics', 'info'],
                         default_choice=0,
                         styles = {
                            'navtab': {'text-transform': 'Captalize'}
                         }
                        )
    
if tabs == 'Detector':
    verificador.page()     
if tabs == 'Análise Exploratória':
    analise_exploratoria.page()
if tabs == 'Análise Comparativa':
    analise_comparativa.page()
if tabs == 'Sobre':
    sobre.page()    