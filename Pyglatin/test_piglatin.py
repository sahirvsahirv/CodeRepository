import unittest

from Piglatin import *

class PiglatinTest(unittest.TestCase):
    def test_translate_sentence(self):
        translate = PigLatinTranslate()
        translatedtext = translate.piglatinTranslateSentence("I am a girl")
        self.assertTrue("I amway away irlgay " == translatedtext)

if __name__ == '__main__':
    unittest.main()
    
