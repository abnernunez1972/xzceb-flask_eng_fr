
import unittest
from translator import english_to_french, french_to_english

class TestMachineTranslation(unittest.TestCase):
    
    # Prueba que la función english_to_french maneje correctamente una entrada nula.
    def test_english_to_french_null_input(self):
        self.assertNotEqual(english_to_french(None), None)

    # Prueba que la función english_to_french maneje correctamente una entrada vacía.
    def test_english_to_french_empty_string(self):
        self.assertEqual(english_to_french(""), "")
        
    # Prueba que la función english_to_french traduzca correctamente "Hello" a "Bonjour".
    def test_english_to_french_hello(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        
    
    # Prueba que la función french_to_english maneje correctamente una entrada nula.
    def test_french_to_english_null_input(self):
        self.assertNotEqual(french_to_english(None), None)               
        
    # Prueba que la función french_to_english maneje correctamente una entrada vacía.
    def test_french_to_english_empty_string(self):
        self.assertEqual(french_to_english(""), "")

    # Prueba que la función french_to_english traduzca correctamente "Bonjour" a "Hello".
    def test_french_to_english_bonjour(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

        
if __name__ == '__main__':
    unittest.main()
