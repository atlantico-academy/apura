from matplotlib import pyplot as plt
from PIL import Image
from wordcloud import WordCloud
import matplotlib
matplotlib.rcParams["figure.dpi"] = 300

def show_wordcloud(data, stopwords = None, title = None):
    text = " ".join(word for word in data)

    wordcloud = WordCloud(stopwords = stopwords,
                          collocations=False,
                          width=1000, height=500,
                          max_font_size=200, 
                          background_color='white').generate(text)

    fig, ax = plt.subplots(figsize=(16,12))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.set_axis_off()
    if title: 
        fig.suptitle(title, fontsize=30)
        fig.subplots_adjust(top=1)

    plt.imshow(wordcloud)
    
def dict_to_wordcloud(dictionary, title = None, colormap = None):
    cloud = WordCloud(width=1000, height=500, 
                      max_words=1000, max_font_size=200, 
                      #min_font_size=15,
                      colormap = colormap,
                      background_color='white').generate_from_frequencies(dictionary)
    fig, ax = plt.subplots(figsize=(16,12))
    ax.imshow(cloud, interpolation='bilinear')
    ax.set_axis_off()
    if title:
        fig.suptitle(title, fontsize=30)
        fig.subplots_adjust(top=1)
    plt.imshow(cloud)
    
def show_ngrams(true_n_gram, fake_n_gram):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 8))
    fig.suptitle('N-gramas mais presentes nas notícias')

    x_true,y_true=map(list,zip(*true_n_gram))
    ax1.barh(y=x_true[::-1], width=y_true[::-1], color='green')
    ax1.title.set_text("Verdadeiras")

    x_fake,y_fake=map(list,zip(*fake_n_gram))
    ax2.barh(y=x_fake[::-1], width=y_fake[::-1], color='red')
    ax2.title.set_text("Falsas")
    ax2.invert_xaxis()
    ax2.yaxis.tick_right()