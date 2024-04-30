import unittest
from cryptage import chiffrage


class TestCryptage(unittest.TestCase):
    def test_chiffrage(self):    
        self.assertEqual(chiffrage("A",8,True), "I")
        self.assertEqual(chiffrage("AB",8,True), "IJ")

    def test_decodage(self):
        self.assertEqual(chiffrage("I",-8,True), "A")
        self.assertEqual(chiffrage("IJ",-8,True), "AB")
        self.assertEqual(chiffrage("IJ",+8,True), "QR")