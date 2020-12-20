
from log_r_13_cart import *
import unittest

class ShoppingCartTest(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart().add("tuna sandwich", 15.00)

    def test_length(self):
        print("WHT")
        print("wht again")
        self.assertEqual(1, len(self.cart))

    def test_item(self):
        self.assertEqual("tuna sandwich", self.cart.item(1))

    def test_price(self):
        self.assertEqual(15.00, self.cart.price(1))

    def test_total_with_sales_tax(self):
        self.assertAlmostEquals(16.39, \
                                self.cart.total(9.25), 2)


# nosetests log_r_13.py - -verbosity = 2

# nosetests log_r_13_test.py --verbosity=2 --with-xunit

# nosetests log_r_13_test.py  -s --verbosity = 2 --with-coverage

# -s for print statements
# coverage test
# pip install coverage
# coverage run test.py arg1 arg2
# coverage report - m
# coverage html
