import unittest
from translator import english_to_french, french_to_english


class LanguageTranslatorTests(unittest.TestCase):

    def test_englishToFrench(self):
        # Test English to French translation
        englishText = "Hello"
        frenchText = english_to_french(englishText)
        expected_frenchText = "Bonjour"
        self.assertEqual(frenchText, expected_frenchText)

    def test_frenchToEnglish(self):
        # Test French to English translation
        frenchText = "Bonjour"
        englishText = french_to_english(frenchText)
        expected_englishText = "Hello"
        self.assertEqual(englishText, expected_englishText)

if __name__ == '__main__':
    unittest.main()
