import pytest
import os

@pytest.fixture(autouse = True)
def print_dir_level_1():
    print(f"\n Fixture-level_ 1 is {os.path.abspath(__file__)}")
    print("Done Fixture LEVEL-1\n")