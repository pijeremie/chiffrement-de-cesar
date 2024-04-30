import unittest
from boucle import boucle_alphabet

class TestBoucle(unittest.TestCase):
    def test_boucle_alphabet(self):          
        self.assertEqual(boucle_alphabet(ord('A')), ord('A'))
        self.assertEqual(boucle_alphabet(ord('Z')), ord('Z')) 
        self.assertEqual(boucle_alphabet(ord(']')), ord('C')) 