from gensim.models import Word2Vec


def get_words_embeddings(sentences, size=100, window=5, min_count=5, workers=3, sg=0):
    '''Function computes word embeddings for given sentences
    
    Arguments:
        sentences {list} -- List of sentences, where each sentence is list of words as strings
    
    Keyword Arguments:
        size {int} -- Dimensionality of the feature vectors. (default: {100})
        window {int} -- The maximum distance between the current and predicted word within a sentence. (default: {5})
        min_count {int} --  Ignores all words with total absolute frequency lower than this (default: {5})
        workers {int} -- Use these many worker threads to train the model (=faster training with multicore machines) (default: {3})
        sg {int} -- 0 for CBOW and 1 for skip-gram (default: {0})
    
    Returns:
        [dict] -- word embeddings
    '''

    model = Word2Vec(sentences=sentences, size=size, window=window,
                     min_count=min_count, workers=workers, sg=sg)
    words = list(model.wv.vocab)
    embeddings = {}
    for word in words:
        embeddings[word] = model[word]
    return embeddings


