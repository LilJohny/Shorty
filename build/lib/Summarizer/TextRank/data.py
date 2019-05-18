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
    if "data" not in os.listdir(os.getcwd()):
        os.mkdir("data/")
    if "glove.6B.100d.pkl" not in os.listdir(os.sep.join([os.getcwd(), "data"])):
        wget.download("https://doc-14-68-docs.googleusercontent.com/docs/securesc/dg109s2vqv57kb64g6hfhghsu9m671u8"
                      "/ola8a3lkirqch2ae9c9sk6pvo4i6ri5h/1558180800000/17248041771668612386/17248041771668612386"
                      "/1WtZCbj8mHUx_QMVYKbkUBzfSd4gkh3wB?e=download&h=06751138000822233008&nonce=q71lkqthtongs&user"
                      "=17248041771668612386&hash=5o2kqo65fqbnma4negmlr02c32bkg3v3", "glove.6B.100d.pkl")
        os.rename("glove.6B.100d.pkl", "data/glove.6B.100d.pkl")


if __name__ == "__main__":
    download_data()
