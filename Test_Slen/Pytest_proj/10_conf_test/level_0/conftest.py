import pytest
import os

@pytest.fixture(autouse = True)
def print_dir_level_0():
    print(f"\nLEVEL 0 fixture is {os.path.abspath(__file__)}")

@pytest.fixture(autouse = True)
def print_level():
    level = os.path.abspath(__file__).split('\\')[-2]
    print(f"Level is {level}")

@pytest.fixture(autouse = True)
def print_unique_key():
    print("print_unique_key")
    print("DONE fixture LEVEL_0\n")