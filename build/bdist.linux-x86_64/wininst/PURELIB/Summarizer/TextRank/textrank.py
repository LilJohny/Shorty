import pickle
import re

import networkx as nx
import numpy as np
try:
    from TextRank.text_processing import sanitize_sentences, get_stopwords
except ModuleNotFoundError:
    from text_processing import sanitize_sentences, get_stopwords
from nltk.tokenize import sent_tokenize
from sklearn.metrics.pairwise import cosine_similarity


class TextRankSummarizer:
    """Class that implements TextRank algorithm"""

    def __init__(self, language):
        """Method initializes new instance of TextRankSummarizer class
        
        Args:
            language (str): Language for TextRank algorithm
        """
        self._summary = None
        self._sentences = None
        self._word_embeddings = {}
        self._stopwords = None
        self.language = language
        self._load_word_embeddings()
        self._load_stop_words()

    def set_text(self, text):
        """Method sets text for TextRank processing
        
        Args:
            text (str): Text to process
        """
        self._original_sentences = sent_tokenize(text)
        self._sentences = sanitize_sentences(self._original_sentences)

    def get_text(self):
        """Method returns original text
        
        Returns:
            str: Original text
        """
        return self._original_sentences

    def _load_word_embeddings(self):
        """Method loads word embeddings
        """
        embeddings_file = open("data/glove.6B.100d.pkl", "rb")
        self._word_embeddings = pickle.load(embeddings_file)
        embeddings_file.close()

    def _load_stop_words(self):
        """Method loads stop words
        """
        self._stopwords = get_stopwords(self.language)

    def get_summary(self, number_of_sentences):
        """Method generates summary
        
        Args:
            number_of_sentences (int): Number of sentences in summary
        
        Returns:
            list: List of summary sentences
        """
        sentence_vectors = []
        for sentence in self._sentences:
            if len(sentence) != 0:
                vector = sum([self._word_embeddings.get(w, np.zeros((100,))) for w in sentence.split()]) / (
                        len(sentence.split()) + 0.001)
            else:
                vector = np.zeros((100,))
            sentence_vectors.append(vector)
        sim_mat = np.zeros([len(self._sentences), len(self._sentences)])
        for i in range(len(self._sentences)):
            for j in range(len(self._sentences)):
                if i != j:
                    sim_mat[i][j] = \
                        cosine_similarity(sentence_vectors[i].reshape(1, 100), sentence_vectors[j].reshape(1, 100))[
                            0, 0]
        nx_graph = nx.from_numpy_array(sim_mat)
        scores = nx.pagerank(nx_graph)
        ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(self._sentences)), reverse=True)
        summary = []
        for i in range(number_of_sentences):
            sentence = ranked_sentences[i][1]
            original_sentence = ""
            for original in self._original_sentences:
                if sanitize_sentences([original.lower()])[0] == sentence:
                    original_sentence = original.replace("\n", "")
                    original_sentence = re.sub(' +', ' ', original_sentence)
            summary.append(original_sentence)
        return summary
