import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud


def show_wordcloud(comp=True):
    """Generate a wordcloud and show the image"""
    if comp:
        df = pd.read_csv('competitor_keywords_nltk.csv')
    else:
        df = pd.read_csv('influencer_keywords_nltk.csv')

    d = {}
    for n, a, x in df.values:
        d[a] = x
    wordcloud = WordCloud(background_color='white', width=1920, height=1080)
    wordcloud.generate_from_frequencies(frequencies=d)

    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


show_wordcloud(comp=True)

# [2021-01-12] (NLP) schedule note: Add visualization for NLP

# [2021-03-09] (Marketing) schedule note: Document market insights for Marketing

# [2021-04-27] (NLP) schedule note: Improve influencer clustering around NLP

# [2021-06-09] (Marketing) schedule note: Improve influencer clustering around Marketing

# [2022-12-20] (Clustering) schedule note: Document market insights for Clustering
