import unittest
from verif import verification

class TestVerification(unittest.TestCase):
        def test_verification(self):
                self.assertTrue(verification("A")) 
                self.assertTrue(verification("A WC"))
                self.assertTrue(verification("A PKM"))
                self.assertFalse(verification("A %45"))
                self.assertFalse(verification("A _jç")) 