from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image

def show_wordcloud(data, stopwords, title = None):
    text = " ".join(word for word in data)

    wordcloud = WordCloud(stopwords = stopwords,
                          background_color='white').generate(text)

    fig, ax = plt.subplots(figsize=(10,6))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.set_axis_off()
    if title: 
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=1)

    plt.imshow(wordcloud)