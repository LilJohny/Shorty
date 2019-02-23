from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
import re

stopwords = stopwords.words('english')


def sanitize_sentence(articles: list):
    '''Function removes all non alphabet symbols from articles.

    Arguments:
        articles {list} -- List of lists with sentences.

    Returns:
        [list] -- List of list with sanitized sentences.
    '''

    for article in articles:
        for i in range(len(article)):
            article[i] = re.sub(r'[a-zA-Z]', ' ', article[i])
            article[i] = re.sub(r'\[[0-9]*\]', ' ', article[i])
            article[i] = re.sub(r'\s+', ' ', article[i])
            article[i] = article[i].lower()
    return articles


def remove_stopwords(sentence: list):
    '''Function removes stopwords from sentence.

    Arguments:
        sentence {list} -- Sentence in english language.

    Returns:
        str -- Sentence without stopwords.
    '''

    ret_sen = ' '.join([word for word in sentence if word not in stopwords])
    return ret_sen


def tokenize(article_text: list):
    '''Function tokenizes sentences into words.

    Arguments:
        article_text {list} -- List of sentences.

    Returns:
        list -- List of lists with tokenized sentences.
    '''

    sentences = []
    for st in article_text:
        sentences.append(sent_tokenize(st))
    return sentences
