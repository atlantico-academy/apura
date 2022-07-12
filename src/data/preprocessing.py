import re
import string

import pandas as pd
import spacy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')

# Converter para minúsculo
def lower_case(text_series):
    return text_series.apply(lambda x: x.lower())

# Tokenização
def tokenize(text_series):
    token_text = []
    for text in text_series:
        token_text.append(nltk.word_tokenize(text))
    return pd.Series(token_text)

# Remover termos específicos
def remove_weekday(text):
    palavras = ['quarta-feira', 'segunda-feira', 'terça-feira', 'sexta-feira', 'quinta-feira', 'sábado', 'domingo']
    for i in palavras:
        #text = re.sub(r'\s'+i+'([\s,\.])',r'\1',text) 
        text = text.replace(i, '')
    return text

def remove_date(text_series, style='diamesano'):
    if style == 'diamesextensoano':
        pattern = '([0-2][0-9]|(3)[0-1]) de *\w* de \d{4}'
    else:
        pattern = '([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}'
    size = text_series[text_series.str.contains(pattern)].size
    print("Modificando "+str(size)+" linhas contendo este padrão.")
    clean_text_series = text_series.apply(lambda x: re.sub(pattern,'', x))
    return clean_text_series

def remove_linebreaks(text_series):
    pattern = '\n'    
    size = text_series[text_series.str.contains(pattern, regex=False)].size
    print("Modificando "+str(size)+" linhas contendo este padrão.")
    clean_text_series = text_series.str.replace(pattern, ' ')
    return clean_text_series

def remove_tabs(text_series):
    pattern = '\t'    
    size = text_series[text_series.str.contains(pattern, regex=False)].size
    print("Modificando "+str(size)+" linhas contendo este padrão.")
    clean_text_series = text_series.str.replace(pattern, ' ')
    return clean_text_series

# Remover símbolos (caracteres especiais)
def symbol_remove(text_series):
    # Obtendo os caracteres especiais
    punctuation = list(string.punctuation) # Obtendo os caracteres especiais como lista
    del(punctuation[12]) # Excluindo da remoção o caractere especial "-"
    punctuation = "".join(punctuation) # Transformando novamente em string
    
    # Realizando a remoção
    size = 0
    for pattern in punctuation:
        size += text_series[text_series.str.contains(pattern, regex=False)].size
    print("Modificando "+str(size)+" linhas contendo este padrão.")
    clean_text_series = text_series.apply(lambda c: re.sub('[%s]' % re.escape(punctuation), '', c))
    return clean_text_series

# Remover stopwords
def stopwords_remove(tokenized_texts):
    text_no_stopwords = []
    for text in tokenized_texts:
        text_no_stopwords.append([word for word in text if word not in stopwords.words('portuguese')])
    return text_no_stopwords

# Lematização
def lemmatization(tokenized_texts):
    nlp = spacy.load('pt_core_news_sm')
    lemmas = []
    for text in tokenized_texts:
        doc = nlp(" ".join(text))
        lemmas.append([token.lemma_ for token in doc])
    return lemmas

# Stemming
def stemming(tokenized_texts):
    stemmer = nltk.stem.RSLPStemmer()
    stemmer_text = []
    for text in tokenized_texts:
        stemmer_text.append([stemmer.stem(palavra) for palavra in text])
    return stemmer_text