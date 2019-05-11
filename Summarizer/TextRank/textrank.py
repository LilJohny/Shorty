import numpy as np
from nltk.tokenize import sent_tokenize
import data
from sklearn.metrics.pairwise import cosine_similarity
from text_processing import sanitize_sentences, get_stopwords
import networkx as nx
import  re

class TextRank:
    """Class that implements TextRank algorithm"""
    def __init__(self, language):
        """Method initializes new instance of class TextRank
        
        Arguments:
            language {str} -- Language ofr TextRank algorithm
        """
        self._summary = None
        self._sentences = None
        self._word_embeddings = {}
        self._stopwords = None
        self.language = language

    def set_text(self, text):
        """Method sets text for TextRank processing
        
        Arguments:
            text {str} -- Text to process
        """
        self._original_sentences = sent_tokenize(text)
        self._sentences = sanitize_sentences(self._original_sentences)

    def get_text(self):
        """Method returns original text
        
        Returns:
            str -- Original text
        """
        return self._original_sentences

    def _load_word_embeddings(self):
        """Method loads word embeddings
        """
        f = open('data/glove.6B.100d.txt', encoding='utf-8')
        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype='float32')
            self._word_embeddings[word] = coefs

    def _load_stop_words(self):
        """Method loads stop words
        """
        self._stopwords = get_stopwords(self.language)

    def get_summary(self, number_of_sentences):
        """Method generates summary 
        
        Arguments:
            number_of_sentences {int} -- Number of sentences in summary
        
        Returns:
            list -- List of summary sentences
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
