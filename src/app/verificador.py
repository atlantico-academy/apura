from random import random

import joblib
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import streamlit as st
from annotated_text import annotated_text
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix

from src.data import preprocessing

model = joblib.load('models/best_model.joblib')
classes = ["fake", "true"]

default_text = "Estudo mostra que crianças que não tomam vacinas são 5 vezes mais saudáveis. .  Além disso, foi identificado que houve um aumento 1000% na incidência de amigdalite nas crianças que receberam vacinas. Os estudos mostraram, sem dúvida, que crianças não vacinadas são mais saudáveis do que as vacinadas e, por esta razão, os dados devem ser cuidadosamente ponderados pelos pais e profissionais da área da medicina. A intenção da pesquisa era tentar provar que crianças vacinadas eram mais propensas a sofrer de asma, eczema, infecções de ouvido, hiperatividade e outras condições crônicas."

min_words = 50

def page():
    st.title("Detector de fakenews")
    text = st.text_area(
        f"Adicione texto da notícia (acima de {min_words} palavras)",
        value=default_text,
        placeholder=default_text,
        max_chars=5000
                       )
    if st.button("Verificar"):
        n_words = len(text.split(" "))
        if n_words < min_words:
            st.error(f"Essa notícia tem apenas {n_words} palavras. Por favor, insira uma notícia com mais de {min_words} palavras")
        else:
            with st.spinner(text='Consultando modelo...'):
                X_ = process_text(text)
                y_hat = model.predict(X_)
                probs = model.predict_proba(X_)[0]
                # -----------------------------
                col1, col2 = st.columns([.6, .4])
                with col1:
                    st.text("")
                    show_simple_results(y_hat, probs)
                    st.write("Caso queira mais informações sobre essa notícia, confira se ela aparece nos seguintes sites: [Agência Lupa](https://lupa.uol.com.br/), [G1 Fato ou Fake](https://g1.globo.com/fato-ou-fake/), [Boatos.org](https://www.boatos.org/), [E-farsas](https://www.e-farsas.com/) e outros especializados em curadoria de notícias falsas.")
                with col2:
                    show_results(y_hat, probs)

        '''        
        with st.expander("Detalhamento"):
            with st.spinner(text='Avaliando cada termo...'):
                col1, col2 = st.columns([.6, .4])
                with col1:
                    st.markdown("### Palavra por palavra")
                    annotated_text(*worb_by_word_classification(text))
                    st.text("")
                with col2:
                    show_results(y_hat, probs)
        '''
            
            
def worb_by_word_classification(text):
    result = []
    for word in text.split(' '):
        X_ = process_text(word)
        # ------------------------------------------
        if X_.iloc[0] != '':
            false_proba = model.predict_proba(X_)[0][0]
            # ----------------------------------
            if false_proba >= .96:
                result.append((f"{word} ", 'false'))
            elif false_proba <= .95:
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
            clean_text = df['text']
            .apply(str.lower) # coloca texto todo para minúscula
            .apply(preprocessing.remove_date) # remove datas dd/mm/YYYY
            .apply(preprocessing.remove_date, style='diamesextensoano') # remove datas com mês escrito por extenso
            .apply(preprocessing.remove_weekday) # remove dias da semana
            .apply(preprocessing.remove_linebreaks) # remove quebras de linha
            .apply(preprocessing.remove_tabs) # remove tabs
            .apply(preprocessing.symbol_remove) # remove caracteres especiais exceto o hífen
#            .apply(preprocessing.tokenize) # cria lista de palavras de cada texto
#            .apply(preprocessing.stopwords_remove) # remove palavras comuns de baixo valor semântico
#            .apply(preprocessing.stemming) # 
        )
    )

    X_ = (
        X_
        .assign(
            tokens = X_['clean_text'].apply(preprocessing.tokenize), # cria lista de palavras de cada texto
        )
    )
    
    X_ = (
        X_
        .assign(
            no_stopwords = X_.tokens.apply(preprocessing.stopwords_remove), # remove palavras comuns de baixo valor semântico
            lemmatization_plus_stop_words = X_.tokens.apply(preprocessing.lemmatization), # 
            stemming_plus_stopwords = X_.tokens.apply(preprocessing.stemming) #         
        )
    )
    
    X_ = (
        X_
        .assign(
            lemmatization_wo_stopwords = X_.no_stopwords.apply(preprocessing.lemmatization), # 
            stemming_wo_stopwords = X_.no_stopwords.apply(preprocessing.stemming) #         
        )
    )    

    return X_.lemmatization_wo_stopwords
            
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
        st.info("O modelo não conseguiu identificar se a notícia é verdadeira ou falsa. Verifique os sites: [Agência Lupa](https://lupa.uol.com.br/), [G1 Fato ou Fake](https://g1.globo.com/fato-ou-fake/), [Boatos.org](https://www.boatos.org/), [E-farsas](https://www.e-farsas.com/) e outros especializados em curadoria de notícias falsas.")
        


