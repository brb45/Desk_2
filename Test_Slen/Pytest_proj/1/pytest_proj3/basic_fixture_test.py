import pytest


def test_comparewithAA(supply_AA_BB_CC):
    zz = 35
    assert supply_AA_BB_CC[0]==zz,"aa and zz comparison failed"


def test_comparewithBB(supply_AA_BB_CC):
    zz = 35
    assert supply_AA_BB_CC[1]==zz,"bb and zz comparison failed"


def test_comparewithCC(supply_AA_BB_CC):
    zz = 35
    assert supply_AA_BB_CC[2]==zz,"cc and zz comparison failed"

# pytest.raise

# input_arr = [100,'z', 100]
# def test_with_exception(input_arr):
#     if input_arr[1].is_alpha():
#         raise TypeError("Please provide a number")
#     return input_arr[1]

