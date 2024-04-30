import unittest
from numeric_converter import convertnumeric

class TestNumeric_Converter(unittest.TestCase):
    def test_numeric_converter(self):
        self.assertEqual(convertnumeric('10'), 10)
        self.assertEqual(convertnumeric('5'), 5)
        self.assertEqual(convertnumeric('-5'), 0)
        self.assertEqual(convertnumeric('0'), 0)