import unittest
from final_project.machinetranslation.translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(), None)
        self.assertEqual(
            english_to_french('Hello')['translations'][0]['translation'],
            'Bonjour'
        )


class TestFrenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english(), None)
        self.assertEqual(
            french_to_english('Bonjour')['translations'][0]['translation'],
            'Hello'
        )