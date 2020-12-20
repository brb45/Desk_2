import unittest
from log_r_8 import *

class RomanNumeralTest(unittest.TestCase):
    def setUp(self):
        self.cvt = RomanNumeralConverter()

    def test_convert_to_decimal(self):
        self.assertEqual(0, self.cvt.convert_to_decimal(""))
        self.assertEqual(1, self.cvt.convert_to_decimal("I"))
        self.assertEqual(2010, \
                          self.cvt.convert_to_decimal("MMX"))
        self.assertEqual(4000, \
                          self.cvt.convert_to_decimal("MMMM"))

    def test_convert_to_roman(self):
        self.assertEqual("", self.cvt.convert_to_roman(0))
        self.assertEqual("II", self.cvt.convert_to_roman(2))
        self.assertEqual("V", self.cvt.convert_to_roman(5))
        self.assertEqual("XII", \
                          self.cvt.convert_to_roman(12))
        self.assertEqual("MMX", \
                          self.cvt.convert_to_roman(2010))
        self.assertEqual("MMMM", \
                          self.cvt.convert_to_roman(4000))

if __name__ == "__main__":
    unittest.main()

