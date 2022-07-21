import streamlit as st
from streamlit.components import v1 as components


def page():
    st.title('Análise exploratória')
    
    plot_file = open('notebooks/html_website/01 - Exploratory Data Analysis.html', 'r')
    plot = plot_file.read()
    components.html(plot, width=1100, height=700, scrolling=True)
    plot_file.close()
