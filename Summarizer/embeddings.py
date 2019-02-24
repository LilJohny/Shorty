from gensim.models import Word2Vec


def get_words_embeddings(sentences, size=100, window=5, min_count=5, workers=3, sg=0):
    model = Word2Vec(sentences=sentences, size=size, window=window,
                     min_count=min_count, workers=workers, sg=sg)
    words = list(model.wv.vocab)
    embeddings = {}
    for word in words:
        embeddings[word] = model[word]
    return embeddings


