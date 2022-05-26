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

