import os
import re
from pathlib import Path

import langdetect
from newspaper import Article
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize


def get_stopwords(language):
    """Function returns stopwords for given language

    Arguments:
        language {str} -- Full name of language, for example 'english' or  'german'
    """
    language = language.lower()
    try:
        words = stopwords.words(language)
    except OSError:
        words_path = str(Path(os.getcwd()).parent) + os.sep + 'stopwords'
        with open(f'{words_path}{os.sep}{language}.txt', 'r', encoding='utf-8') as f:
            words = f.readlines()
            words = list(map(lambda x: x.strip(), words))
    return words


def sanitize_sentences(article: list):
    """Function removes all non alphabet symbols from articles.

    Arguments:
        articles {list} -- List of  sentences.

    Returns:
        [list] -- List of list with sanitized sentences.
    """

    for i in range(len(article)):
        article[i] = re.sub(r'[^a-zA-Z]', ' ', article[i])
        article[i] = re.sub(r'\[[0-9]*\]', ' ', article[i])
        article[i] = re.sub(r'\s+', ' ', article[i])
        article[i] = article[i].lower()
    return article


def remove_stopwords(sentence: list, stopwords):
    """Function removes stopwords from sentence.

    Arguments:
        sentence {list} -- Sentence in english language.

    Returns:
        str -- Sentence without stopwords.
    """

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
        sentences.append(word_tokenize(st))
    return sentences


def split_into_sentences(article_text):
    '''Function splits text into sentences

    Arguments:
        article_text {str} -- Text to process

    Returns:
        list -- list of sentences from given text
    '''
    return sent_tokenize(article_text)


def get_text(url):
    '''Function returns article text by given url

    Arguments:
        url {str} -- URL to parse

    Returns:
        str -- Article text from given url.
    '''

    article = Article(url)
    article.download()
    article.parse()
    chunks = list(filter(lambda x: x != '', article.text.split('\n')))
    chunks = list(filter(lambda x: langdetect.detect(x)
                         == article.meta_lang, chunks))
    return '\n'.join(chunks)
