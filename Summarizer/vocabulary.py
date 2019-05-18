import os
import pickle
import subprocess
from collections import Counter
import data
import numpy as np


class Vocabulary:
    """Class representing instance, that can create embedding voabulary of given size
    """
    EMPTY = 0
    EOS = 1
    START_IDX = EOS + 1
    GLOVE_THR = 0.5
    NB_UNKNOWN_WORDS = 100

    def __init__(self,
                 data_filename,
                 seed=42,
                 vocab_size=40000,
                 embedding_dim=100,
                 lower=False):
        """Method creates new instance of class Vocabulary
        
        
        Args:
            data_filename (str): Filename of binary data to read
            seed (int, optional): Value to seed random embeddings. Defaults to 42.
            vocab_size (int, optional): Maximum size of vocabulary. Defaults to 40000.
            embedding_dim (int, optional): Embedding dimensions. Defaults to 100.
            lower (bool, optional): Make text lower or not. Defaults to False.
        """
        self._data_filename = data_filename
        self._seed = seed
        self._vocab_size = vocab_size
        self._embedding_dim = embedding_dim
        self._lower = lower
        self._heads = []
        self._desc = []
        self._load_data()

    @staticmethod
    def _get_vocab(lst):
        vocab_count = Counter(word for text in lst for word in text.split())
        vocab = list(
            map(lambda x: x[0], sorted(vocab_count.items(),
                                       key=lambda x: -x[1])))
        return vocab, vocab_count

    def _load_data(self):
        with open(self._data_filename, 'rb') as fp:
            data = pickle.load(fp)
        for line in data:
            self._heads.append(line[0])
            self._desc.append(line[1])
        if self._lower:
            self._heads = [h.lower() for h in self._heads]
            self._desc = [h.lower() for h in self._desc]

    def _get_idx(self, vocab):
        word2idx = dict(
            (word, idx + self.START_IDX) for idx, word in enumerate(vocab))
        word2idx['<empty>'] = self.EMPTY
        word2idx['<eos>'] = self.EOS
        idx2word = dict((idx, word) for word, idx in word2idx.items())
        return word2idx, idx2word

    def get_embeddings(self):
        """Method computes dictionary of embedding of given size
        
        Returns:
            tuple: Tuple of computed dictionaries
        """
        vocab, vocab_count = self._get_vocab(self._heads + self._desc)
        self._word2idx, self._idx2word = self._get_idx(vocab)
        self._glove_n_symbols, self._glove_name = self._get_dataset_size()
        self._globale_scale = .1
        self._read_glove()
        self._generate_random_embedding()
        self._copy_duplicates()
        self._normalize()
        normed_embedding = self._embedding / np.array(
            [np.sqrt(np.dot(gweight, gweight))
             for gweight in self._embedding])[:, None]
        glove_idx2idx = self._finalize(normed_embedding)
        return self._embedding, self._idx2word, self._word2idx, glove_idx2idx

    def get_source_data(self):
        """Method returns flatten source data
        
        Returns:
            tuple: Tuple of X and Y data for given data
        """
        X = [[self._word2idx[token] for token in d.split()]
             for d in self._desc]
        Y = [[self._word2idx[token] for token in headline.split()]
             for headline in self._heads]
        return X, Y

    @staticmethod
    def dump_source_data(data):
        """Method dumps given source data into 'data/vocabulary-embedding.data.pkl' 
        
        Args:
            data (tuple): Source data to dump
        """
        X, Y = data
        with open('data/vocabulary-embedding.data.pkl', 'wb') as fp:
            pickle.dump((X, Y), fp, -1)

    @staticmethod
    def dump_embeddings(data):
        """Method dumps given embedding data into 'data/vocabulary-embedding.pkl'
        
        Args:
            data (tuple): Embedding data to dump
        """
        embedding, idx2word, word2idx, glove_idx2idx = data
        with open('data/vocabulary-embedding.pkl', 'wb') as fp:
            pickle.dump((embedding, idx2word, word2idx, glove_idx2idx), fp, -1)

    def _generate_random_embedding(self):
        np.random.seed(self._seed)
        shape = (self._vocab_size, self._embedding_dim)
        scale = self._glove_embedding_weights.std() * np.sqrt(12) / 2
        self._embedding = np.random.uniform(low=-scale, high=scale, size=shape)

    def _read_glove(self):
        self._glove_index_dict = {}
        self._glove_embedding_weights = np.empty(
            (self._glove_n_symbols, self._embedding_dim))
        with open(self._glove_name, 'r') as fp:
            i = 0
            for l in fp:
                l = l.strip().split()
                w = l[0]
                self._glove_index_dict[w] = i
                self._glove_embedding_weights[i, :] = list(map(float, l[1:]))
                i += 1
        self._glove_embedding_weights *= self._globale_scale
        for w, i in self._glove_index_dict.items():
            w = w.lower()
            if w not in self._glove_index_dict:
                self._glove_index_dict[w] = i

    def _copy_duplicates(self):
        for i in range(min(len(self._idx2word), self._vocab_size)):
            w = self._idx2word[i]
            g = self._glove_index_dict.get(
                w, self._glove_index_dict.get(w.lower()))
            if g is None and w.startswith('#'):
                w = w[1:]
                g = self._glove_index_dict.get(
                    w, self._glove_index_dict.get(w.lower()))
            if g is not None:
                self._embedding[i, :] = self._glove_embedding_weights[g, :]

    def _get_dataset_size(self):
        file_name = f'glove.6B.{self._embedding_dim}d.txt'
        glove_name = os.path.join("data", file_name)
        out = subprocess.Popen(['wc', '-l', glove_name],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()
        return int(stdout.split()[0]), glove_name

    def _normalize(self):
        self._word2glove = {}
        for w in self._word2idx:
            if w in self._glove_index_dict:
                g = w
            elif w.lower() in self._glove_index_dict:
                g = w.lower()
            elif w.startswith('#') and w[1:] in self._glove_index_dict:
                g = w[1:]
            elif w.startswith('#') and w[1:].lower() in self._glove_index_dict:
                g = w[1:].lower()
            else:
                continue
            self._word2glove[w] = g

    def _finalize(self, normed_embedding):
        glove_match = []
        for w, idx in self._word2idx.items():
            if idx >= self._vocab_size - self.NB_UNKNOWN_WORDS and w.isalpha(
            ) and w in self._word2glove:
                gidx = self._glove_index_dict[self._word2glove[w]]
                gweight = self._glove_embedding_weights[gidx, :].copy()
                # find row in embedding that has the highest cos score with gweight
                gweight /= np.sqrt(np.dot(gweight, gweight))
                score = np.dot(
                    normed_embedding[:self._vocab_size -
                                     self.NB_UNKNOWN_WORDS], gweight)
                while True:
                    embedding_idx = score.argmax()
                    s = score[embedding_idx]
                    if s < self.GLOVE_THR:
                        break
                    if self._idx2word[embedding_idx] in self._word2glove:
                        glove_match.append((w, embedding_idx, s))
                        break
                    score[embedding_idx] = -1
        glove_match.sort(key=lambda x: -x[2])
        glove_idx2idx = dict((self._word2idx[w], embedding_idx)
                             for w, embedding_idx, _ in glove_match)
        return glove_idx2idx
