import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def perform_pagerank(word_embeddings, clean_sentences, sentences):
    '''Function computes scores for every sentence

    Arguments:
        word_embeddings {dict} -- Dict with words as keys and numpy arrays with embeddings as values
        clean_sentences {list} -- Sentences without stopwords
        sentences {list} -- Original sentences as list of str
    '''

    sentence_vector = []
    for i in clean_sentences:
        if len(i) != 0:
            v = sum([word_embeddings.get(w, np.zeros((100,)))
                     for w in i.split()])/(len(i.split())+0.001)
        else:
            v = np.zeros(100,)
        sentence_vector.append(v)
    sim_mat = np.zeros([len(sentences), len(sentences)])
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i != j:
                sim_mat[i][j] = cosine_similarity(sentence_vector[i].reshape(
                    1, 100), sentence_vector[i].reshape(1, 100))[0, 0]
    nx_graph = nx.from_numpy_array(sim_mat)
    scores = nx.pagerank(nx_graph)
    ranked_sentences = sorted(
        ((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    return ranked_sentences
