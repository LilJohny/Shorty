from vocabulary import Vocabulary


def main():
    vocabulary = Vocabulary("data/tokens.pkl")
    embedding = vocabulary.get_embeddings()
    vocabulary.dump_embeddings(embedding)
    source_data = vocabulary.get_source_data()
    vocabulary.dump_source_data(source_data)


if __name__ == '__main__':
    main()
