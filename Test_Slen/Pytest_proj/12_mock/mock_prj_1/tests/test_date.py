from datetime import date
from unittest.mock import patch
import unittest

# from django.test import TestCase

from apps import myfunc_using_date


def mocked_today():
    print("\nmocked_today is being called!!!")
    return date(year=2020, month=1, day=1)



class TestImmutableObject(unittest.TestCase):
    @patch("apps.get_today", mocked_today)
    def test_myfunc_using_date(self):
        self.assertEqual(myfunc_using_date().strftime("%Y-%m-%d"), "2020-01-01")


if __name__ == '__main__':
    unittest.main(verbosity=2)