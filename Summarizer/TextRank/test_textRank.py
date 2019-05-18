from unittest import TestCase
from textrank import TextRankSummarizer
from nltk.tokenize import sent_tokenize
from text_processing import sanitize_sentences


class TestTextRank(TestCase):

    def setUp(self):
        self.summarizer = TextRankSummarizer("english")

    def test_set_text(self):
        text = "We had a bunch of photographs of the main PCB, a YouTube video with drain-voltage waveforms of " \
               "MOSFETs, a forum post with a breakdown of the capacitance values of LC circuit capacitors and also a " \
               "number of unboxing videos showing the heating-up of the soldering tip.The only thing that really " \
               "worried me was the video with the measurement of the peak power consumption during the " \
               "heating-up.There is nothing in the world more helpless and irresponsible and depraved than burned " \
               "cartridge newly bought for 60 bucks from Amazon.But let me start from the beginning. "
        self.summarizer.set_text(text)
        self.assertEqual(sent_tokenize(text), self.summarizer.get_text())
        text = "Let's see what we mean when we talk about a brand. A brand is, first of all, associations that people " \
               "immediately have when they hear the name of your company, mobile application, website, " \
               "etc.Brand building is a long process. Be prepared that it will take not one, not two, " \
               "or even 6 months — you must be ready to work on it all the time. "
        self.summarizer.set_text(text)
        self.assertEqual(sent_tokenize(text), self.summarizer.get_text())

    def test_get_summary(self):
        text = """We had a bunch of photographs of the main PCB, a YouTube video with drain-voltage waveforms of 
        MOSFETs, a forum post with a breakdown of the capacitance values of LC circuit capacitors and also a number 
        of unboxing videos showing the heating-up of the soldering tip. The only thing that really worried me was the 
        video with the measurement of the peak power consumption during the heating-up. There is nothing in the world 
        more helpless and irresponsible and depraved than burned cartridge newly bought for 60 bucks from Amazon. But 
        let me start from the beginning. """
        self.summarizer.set_text(text)
        self.assertEqual(self.summarizer.get_summary(1), ["The only thing that really worried me was the video with "
                                                          "the measurement of the peak power consumption during the "
                                                          "heating-up."])
        summary = self.summarizer.get_summary(2)
        self.assertEqual(self.summarizer.get_summary(2), [
            "The only thing that really worried me was the video with "
            "the measurement of the peak power consumption during the "
            "heating-up.",
            "There is nothing in the world more helpless and irresponsible and depraved than burned cartridge newly "
            "bought for 60 "
            "bucks from Amazon."])
