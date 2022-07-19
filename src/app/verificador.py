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
    st.text(testa_modelo(model)) # debugging, remover depois
    # até aqui a confusion matrix é impressa corretamente
    text = st.text_area(
        "Adicione texto da notícia",
        value=default_text,
        placeholder=default_text
                       )
    if st.button("Verificar"):
        with st.spinner(text='Consultando modelo...'):
            # receber notícia e jogar no modelo
            
            # TODO: Substituir pela predição real
            
            #st.text(text) # debugging, remover depois
            X_ = process_text(text)
            st.dataframe(X_) # debugging, remover depois 
            
#             #highlight_text(text)
            y_hat = model.predict(X_)
            st.text(f"resultado {y_hat}") #debugging, remover depois
            probs = model.predict_proba(X_)[0]
            st.text(f"probabilidades {probs}") #debugging, remover depois
            #prob = random()
            #probs = [prob, 1-prob]
            #y_hat = np.round(np.argmax(probs))
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
        # TODO: modificar para preprocessamento real
        X_ = process_text(word)
        #X_ = [1]
        # ------------------------------------------
        if len(X_) != 0:
            # TODO: modificar para predição real
            false_proba = model.predict_proba(X_)[0][0]
            #false_proba = random()
            # ----------------------------------
            if false_proba >= .8:
                result.append((f"{word} ", 'false'))
            elif false_proba <= .2:
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
    return X_

            
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
        
        
def testa_modelo(model):
    # Adquire dados do arquivo produzido na etapa anterior
    input_path = 'data/processed/textos_pre-processados.csv'
    df = pd.read_csv(input_path)

    # Converte as colunas com texto em uma lista
    corpus = df.text.to_list()

    # Atribui codificação dos rótulos das notícias
    labels = df.label.replace({"true": 1, "fake": 0})

    #import joblib
    #approach = joblib.load('../models/best_model.joblib')

    y_hat = model.predict(corpus)

    return confusion_matrix(labels, y_hat)