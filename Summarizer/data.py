import os

import nltk
import wget


def download_data():
    """Function checks if needed data if presented and if not downloads it
    """
    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        nltk.download("punkt")
    try:
        nltk.data.find("corpora/stopwords")
    except LookupError:
        nltk.download("stopwords")


if __name__ == "__main__":
    download_data()
