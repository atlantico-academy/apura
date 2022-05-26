from sklearn.feature_extraction.text import CountVectorizer 
import re

def create_corpus(text_series):
    corpus = []
    news = text_series.str.split()
    news = news.values.tolist()
    corpus = [word for i in news for word in i]
    return corpus

def get_top_ngram(corpus, n=None, top=10, stop_words=None):
    vector = CountVectorizer(ngram_range=(n, n), stop_words = stop_words).fit(corpus) # cria um vetor com os termos do corpus
    bag_of_words = vector.transform(corpus) # gera a matriz de ausência 0 / presença 1 dos termos em cada texto
    sum_words = bag_of_words.sum(axis=0) # soma para calcular a presença de termos nos textos
    words_freq = [(word, sum_words[0, idx]) 
                  for word, idx in vector.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:top]

def remove_day(text):
    palavras = ['quarta-feira', 'segunda-feira', 'terça-feira', 'sexta-feira', 'quinta-feira']
    for i in palavras:
        text = re.sub(r'\s'+i+'([\s,\.])',r'\1',text) 
    return text