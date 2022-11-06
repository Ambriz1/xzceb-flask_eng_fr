import unittest
from translator import english_to_french, french_to_english

class TestTranslator1(unittest.TestCase):
    def test_english_to_french(self):
        #self.assertEqual(english_to_french(None), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('goodbye'), 'au revoir')
        #self.assertEqual(english_to_french('How are you?'), 'Comment ça va')
        
class TestTranslator2(unittest.TestCase): 
    def test_french_to_english(self):
        #self.assertEqual(french_to_english(None), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('au revoir'), 'goodbye')
        #self.assertEqual(french_to_english('mon nom est'), 'My name is')

if __name__ =='__main__':
  unittest.main()