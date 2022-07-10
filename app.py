# bibliotecas
import streamlit as st # site
from st_on_hover_tabs import on_hover_tabs # menus laterais

# configuração
st.set_page_config(layout='wide') # página em modo amplo

# st.header("Custom tab component for on-hover navigation bar")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

# menus laterais
with st.sidebar:
    tabs = on_hover_tabs(tabName=['Detector', 'Metodologia', 'Contato'], 
                         iconName=['dashboard', 'money', 'economy'],
                         default_choice=0)
    
if tabs =='Detector':
    
    st.title('Detector de Notícias Falsas 📰')
    
    # entrada da notícia falsa
    col1, col2= st.columns([3, 1])

    with col1:
        st.text_input('Insira texto da notícia (x caracteres ou mais)')
        st.button('Checar notícia')
        # inserir contador de caracteres
    #with col2:

elif tabs == 'Metodologia':    
    st.title("O projeto")
    
    st.markdown(
        "1. A notícia submetida para análise é tem suas palavras extraídas, contabilizadas e processadas. 2. Um modelo de aprendizado de máquina classifica as informações obtidas utilizando seus conhecimentos adquiridos pelo treinamento com XX notícias verdadeiras e XX notícias falsas.")
    st.image('./images/social-preview-github.png')
    
    
    
    
    st.write('Name of option is {}'.format(tabs))

elif tabs == 'Contato':
    st.title("Tom")
    st.write('Name of option is {}'.format(tabs))