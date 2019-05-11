from unittest import TestCase
from vocabulary import Vocabulary
import  os

class TestVocabulary(TestCase):
    def setUp(self):
        self.vocabulary = Vocabulary("data/tokens.pkl")

    def test_dump_source_data(self):
        dummy_data = ([0, 0, 0], [0, 0, 0])
        self.vocabulary.dump_source_data(dummy_data)
        self.assertTrue(os.path.isfile("data/vocabulary-embedding.data.pkl"))
        os.remove("data/vocabulary-embedding.data.pkl")
    def test_dump_embeddings(self):
        dummy_data = ([0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0])
        self.vocabulary.dump_embeddings(dummy_data)
        self.assertTrue(os.path.isfile("data/vocabulary-embedding.pkl"))
        os.remove("data/vocabulary-embedding.pkl")

    def test_get_dataset_size(self):
        self.assertEqual(self.vocabulary._get_dataset_size()[0], 400000)
