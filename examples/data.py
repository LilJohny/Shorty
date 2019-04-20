import nltk
import wget
import os
import zipfile

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
if "glove.6B.100d.txt" not in os.listdir(os.sep.join([os.getcwd(), "data"])):
    wget.download("http://nlp.stanford.edu/data/glove.6B.zip", "glove.6B.zip")
    glove = zipfile.ZipFile("glove.6B.zip", "r")
    glove.extractall("data")
    glove.close()
    os.remove("glove.6B.zip")
