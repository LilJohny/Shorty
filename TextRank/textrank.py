import numpy as np
from nltk.tokenize import sent_tokenize
import data
from sklearn.metrics.pairwise import cosine_similarity
from text_processing import sanitize_sentences, get_stopwords
import networkx as nx


class TextRank:
    def __init__(self, language):
        self._summary = None
        self._sentences = None
        self._word_embeddings = {}
        self._stopwords = None
        self.language = language

    def set_text(self, text):
        self._sentences = sent_tokenize(text)
        self._sentences = sanitize_sentences(self._sentences)

    def _load_word_embeddings(self):
        f = open('data/glove.6B.100d.txt', encoding='utf-8')
        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype='float32')
            self._word_embeddings[word] = coefs

    def _load_stop_words(self):
        self._stopwords = get_stopwords(self.language)

    def get_summary(self, number_of_sentences):
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
            summary.append(ranked_sentences[i][1])
        return summary
