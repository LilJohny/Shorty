from gensim.models import Word2Vec


def get_words_embeddings(sentences, size=100, window=5, min_count=5, workers=3, sg=0):
    """Function computes word embeddings for given sentences
    
    Args:
        sentences (list): List of sentences, where each sentence is list of words as strings
        size (int, optional): Dimensionality of the feature vectors. Defaults to 100.
        window (int, optional): The maximum distance between the current and predicted word within a sentence. Defaults to 5.
        min_count (int, optional): Ignores all words with total absolute frequency lower than this. Defaults to 5.
        workers (int, optional): Use these many worker threads to train the model (=faster training with multicore machines) . Defaults to 3.
        sg (int, optional): 0 for CBOW and 1 for skip-gram. Defaults to 0.
    
    Returns:
        dict: Word embeddings
    """

    model = Word2Vec(sentences=sentences, size=size, window=window,
                     min_count=min_count, workers=workers, sg=sg)
    words = list(model.wv.vocab)
    embeddings = {}
    for word in words:
        embeddings[word] = model[word]
    return embeddings


