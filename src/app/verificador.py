import streamlit as st
import joblib
import pandas as pd
import numpy as np
from src.data import preprocessing
from matplotlib import pyplot as plt
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
from annotated_text import annotated_text
from random import random
from sklearn.metrics import confusion_matrix

model = joblib.load('models/best_model.joblib')
classes = ["fake", "true"]

default_text = "O senador e a irmã foram acusados por pedirem e receberem R$ 2 milhões do empresário Joesley Batista, dono da J&F. A PGR diz que o dinheiro era propina para beneficiar o grupo com favores políticos. A defesa de Aécio e Andrea diz que o montante era para pagar advogados."


def page():
    st.title("Detector de fakenews")
    text = st.text_area(
        "Adicione texto da notícia",
        value=default_text,
        placeholder=default_text
                       )
    if st.button("Verificar"):
        with st.spinner(text='Consultando modelo...'):
            X_ = process_text(text)
            y_hat = model.predict(X_)
            probs = model.predict_proba(X_)[0]
            # -----------------------------
            show_simple_results(y_hat, probs)
            with st.expander("Detalhamento"):
                col1, col2 = st.columns([.6, .4])
                with col1:
                    st.markdown("### Palavra por palavra")
                    annotated_text(*worb_by_word_classification(text))
                    st.text("")
                with col2:
                    show_results(y_hat, probs)
            
            
            
def worb_by_word_classification(text):
    result = []
    for word in text.split(' '):
        X_ = process_text(word)
        # ------------------------------------------
        if len(X_) != 0:
            false_proba = model.predict_proba(X_)[0][0]
            # ----------------------------------
            if false_proba >= .95:
                result.append((f"{word} ", 'false'))
            elif false_proba <= .8:
                result.append((f"{word} ", 'true'))
            else:
                result.append(f"{word} ")
        else:
            result.append(f"{word} ")
    return result
    
            
def process_text(text):
    df = pd.DataFrame({
            "text": [text]
        })

    X_ = (
        df
        .assign(
            text = df['text']
            #.apply(str.lower) # coloca texto todo para minúscula
            #.apply(preprocessing.remove_date) # remove datas dd/mm/YYYY
            #.apply(preprocessing.remove_date, style='diamesextensoano') # remove datas com mês escrito por extenso
            #.apply(preprocessing.remove_weekday) # remove dias da semana
            #.apply(preprocessing.remove_linebreaks) # remove quebras de linha
            #.apply(preprocessing.remove_tabs) # remove tabs
            #.apply(preprocessing.symbol_remove) # remove caracteres especiais exceto o hífen
            #.apply(preprocessing.tokenize) # cria lista de palavras de cada texto
            #.apply(preprocessing.stopwords_remove) # remove palavras comuns de baixo valor semântico
            #.apply(preprocessing.stemming) # 
        )
    )
    return X_.text

            
def show_results(y_hat, probs):
    '''
        Cria visualização intuitiva do resultado da predição
    '''
    
    # col1, col2 = st.columns(2)
    # with col1:
    #     st.text('Disclaimer')
    # with col2:
    label = classes[int(y_hat)]    
    st.markdown(f"""### Escore""")

    
    fig = px.bar(x=classes, y=probs, template="simple_white", width=800, height=300)
    st.plotly_chart(fig, use_container_width=True)
    

def show_simple_results(y_hat, probs):
    label = classes[int(y_hat)]
    text = f"A notícia tem grande probabilidade de ser {label}."
    if probs[classes.index('fake')] >= .8:
        st.error(text)
    elif probs[classes.index('fake')] <= .2:
        st.success(text)
    else:
        st.info("O modelo não conseguiu identificar se a notícia é verdadeira ou falsa. Verifique os sites ---")
        
        
