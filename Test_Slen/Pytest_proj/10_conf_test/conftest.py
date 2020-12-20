import pytest
import os

@pytest.fixture(autouse = True)
def print_dir_root():
    print("\nROOT fixture -- 0")

@pytest.fixture(autouse = True)
def print_level_root():
    print(f"ROOT fixture -- 1 name is {__file__}")

@pytest.fixture(autouse = True)
def print_root_dir():
    print("ROOT fixture -- 2 ")
    print("DONE ROOT Fixture\n")