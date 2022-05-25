from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image

def show_wordcloud(data, stopwords, title = None):
    text = " ".join(word for word in data)

    wordcloud = WordCloud(stopwords = stopwords,
                          collocations=False,
                          background_color='white').generate(text)

    fig, ax = plt.subplots(figsize=(10,6))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.set_axis_off()
    if title: 
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=1)

    plt.imshow(wordcloud)
    
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