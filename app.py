# bibliotecas
import streamlit as st  # site
from streamlit_option_menu import option_menu # menu lateral

from src.app import (analise_comparativa, analise_exploratoria, sobre,
                     verificador)

# configuração
#st.set_page_config(layout='wide') # página em modo amplo
# st.header("Custom tab component for on-hover navigation bar")
#st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

# menus lateral
with st.sidebar:
    tabs = option_menu(
        menu_title = None,
        options = ["Detector", "Análise Exploratória", "Análise Comparativa", "Sobre"],
        icons=["search", "clipboard-data", "diagram-3-fill", "info-square"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            #"icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#D56439"},
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