import unittest
from log_r_8 import *

class RomanNumeralTest(unittest.TestCase):
    def setUp(self):
        self.cvt = RomanNumeralConverter()

    def test_to_decimal1(self):
        self.assertEqual(0, self.cvt.convert_to_decimal(""))

    def test_to_decimal2(self):
        self.assertEqual(1, self.cvt.convert_to_decimal("I"))

    def test_to_decimal3(self):
        self.assertEqual(2010, \
                          self.cvt.convert_to_decimal("MMX"))

    def test_to_decimal4(self):
        self.assertEqual(4000, \
                          self.cvt.convert_to_decimal("MMMM"))

    def test_convert_to_roman1(self):
        self.assertEqual("", self.cvt.convert_to_roman(0))

    def test_convert_to_roman2(self):
        self.assertEqual("II", self.cvt.convert_to_roman(2))

    def test_convert_to_roman3(self):
        self.assertEqual("V", self.cvt.convert_to_roman(5))

    def test_convert_to_roman4(self):
        self.assertEqual("XII", \
                          self.cvt.convert_to_roman(12))

    def test_convert_to_roman5(self):
        self.assertEqual("MMX", \
                          self.cvt.convert_to_roman(2010))

    def test_convert_to_roman6(self):
        self.assertEqual("MMMM", \
                          self.cvt.convert_to_roman(4000))

if __name__ == "__main__":
    unittest.main()

