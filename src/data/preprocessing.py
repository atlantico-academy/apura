import re
import string

import pandas as pd
import spacy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')

# Tokenização
def tokenize(text):
    tokens = nltk.word_tokenize(text)
    return tokens

# Remover termos específicos
def remove_weekday(text):
    palavras = ['quarta-feira', 'segunda-feira', 'terça-feira', 'sexta-feira', 'quinta-feira', 'sábado', 'domingo']
    for i in palavras:
        #text = re.sub(r'\s'+i+'([\s,\.])',r'\1',text) 
        text = text.replace(i, '')
    return text

def remove_date(text, style='diamesano'):
    if style == 'diamesextensoano':
        pattern = '([0-2][0-9]|(3)[0-1]) de *\w* de \d{4}'
    else:
        pattern = '([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}'
    clean_text = re.sub(pattern,'', text)
    return clean_text

def remove_linebreaks(text):
    pattern = '\n'    
    clean_text = text.replace(pattern, ' ')
    return clean_text

def remove_tabs(text):
    pattern = '\t'    
    clean_text = text.replace(pattern, ' ')
    return clean_text

# Remover símbolos (caracteres especiais)
def symbol_remove(text):
    # Obtendo os caracteres especiais
    punctuation = list(string.punctuation) # Obtendo os caracteres especiais como lista
    del(punctuation[12]) # Excluindo da remoção o caractere especial "-"
    punctuation = "".join(punctuation) # Transformando novamente em string
    
    # Realizando a remoção
    size = 0
    clean_text = re.sub('[%s]' % re.escape(punctuation), '', text)
    return clean_text

# Remover stopwords
def stopwords_remove(tokens):
    pt_stopwords = stopwords.words('portuguese')
    clean_tokens = tuple(filter(lambda word: word not in pt_stopwords, tokens))
    return clean_tokens

# Lematização
def lemmatization(text):
    nlp = spacy.load('pt_core_news_sm')
    doc = nlp(" ".join(text))
    lemma_tokens = [token.lemma_ for token in doc]
    lemmas = ' '.join(lemma_tokens)
    return lemmas

# Stemming
def stemming(text):
    stemmer = nltk.stem.RSLPStemmer()
    stem_tokens = [stemmer.stem(word) for word in text]
    stemmer_text = ' '.join(stem_tokens)
    return stemmer_text