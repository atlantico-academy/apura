import streamlit as st
import joblib
import pandas as pd
import numpy as np
from src.data import preprocessing
from matplotlib import pyplot as plt
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px

model = joblib.load('models/best_model.joblib')
label_encoder = joblib.load('models/best_label_encoder.joblib')
classes = label_encoder.classes_

default_text = "O senador e a irmã foram acusados por pedirem e receberem R$ 2 milhões do empresário Joesley Batista, dono da J&F. A PGR diz que o dinheiro era propina para beneficiar o grupo com favores políticos. A defesa de Aécio e Andrea diz que o montante era para pagar advogados."

def foo(y_hat):
    saida = 'Pinguin com '
    if y_hat[1] > .4 and y_hat[1] < .6:
        saida = 'O modelo não tem certeza do sexo do pinguin. Por favor verifique no site tal...'
    elif y_hat[1] < .5:
        saida = saida + f'{y_hat[0]*100:.2f}% de probabilidade de ser fêmea.'
    else:
        saida = saida + f'{y_hat[1]*100:.2f}% de probabilidade de ser macho.'
    return saida

def page():
    st.title("Detector de fakenews")
    text = st.text_area("Adicione texto da notícia",
                       value=default_text,
                       placeholder=default_text)
    if st.button("Verificar"):
        with st.spinner(text='Consultando modelo...'):
            # receber notícia e jogar no modelo

            df = pd.DataFrame({
                    "text": [text]
                })

            X_ = (
                df
                .assign(
                    text = df['text']
                    .apply(str.lower) # coloca texto todo para minúscula
                    .apply(preprocessing.remove_date) # remove datas dd/mm/YYYY
                    .apply(preprocessing.remove_date, style='diamesextensoano') # remove datas com mês escrito por extenso
                    .apply(preprocessing.remove_weekday) # remove dias da semana
                    .apply(preprocessing.remove_linebreaks) # remove quebras de linha
                    .apply(preprocessing.remove_tabs) # remove tabs
                    .apply(preprocessing.symbol_remove) # remove caracteres especiais exceto o hífen
                    .apply(preprocessing.tokenize) # cria lista de palavras de cada texto
                    .apply(preprocessing.stopwords_remove) # remove palavras comuns de baixo valor semântico
                    .apply(preprocessing.lemmatization) # 
                )
            )
            
            #highlight_text(text)
            y_hat = model.predict(X_)
            probs = model.predict_proba(X_)[0]
            
            show_results(y_hat, probs)
            
            
def process_text(text):
    df = pd.DataFrame({
            "text": [text]
        })

    X_ = (
        df
        .assign(
            text = df['text']
            .apply(str.lower) # coloca texto todo para minúscula
            .apply(preprocessing.remove_date) # remove datas dd/mm/YYYY
            .apply(preprocessing.remove_date, style='diamesextensoano') # remove datas com mês escrito por extenso
            .apply(preprocessing.remove_weekday) # remove dias da semana
            .apply(preprocessing.remove_linebreaks) # remove quebras de linha
            .apply(preprocessing.remove_tabs) # remove tabs
            .apply(preprocessing.symbol_remove) # remove caracteres especiais exceto o hífen
            .apply(preprocessing.tokenize) # cria lista de palavras de cada texto
            .apply(preprocessing.stopwords_remove) # remove palavras comuns de baixo valor semântico
            .apply(preprocessing.lemmatization) # 
        )
    )

            
def show_results(y_hat, probs):
    '''
        Cria visualização intuitiva do resultado da predição
    '''
    
    col1, col2 = st.columns(2)
    with col1:
        st.text('Disclaimer')
    with col2:
        label = classes[int(y_hat)]    
        st.markdown(f"""## Resultado""")
        
        st.text(f"""Temos uma notícia {label}""")
        fig = px.bar(x=classes, y=probs, template="simple_white")
        st.plotly_chart(fig, use_container_width=True)

#def plot_probs(probs):
    
#def highlight_text(text):