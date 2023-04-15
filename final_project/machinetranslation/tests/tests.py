"""
testing for english to french and vice versa
"""
import unittest

from translator import french_to_english, english_to_french


class TestEnglishToFrench(unittest.TestCase):
    """
    test for english to french
    """

    def test1(self):
        """
        test for english to french
        """
        self.assertEqual(english_to_french("hello"), "Bonjour")
        self.assertNotEqual(english_to_french("hello"), "Comment")


class TestFrenchToEnglish(unittest.TestCase):
    """
    test for english to frenc
    """

    def test2(self):
        """
        test for french to english
        """
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("bonne nuit"), "Good Evening")


unittest.main()
