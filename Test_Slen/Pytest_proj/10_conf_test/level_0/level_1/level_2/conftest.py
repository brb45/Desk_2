import pytest
import os

@pytest.fixture(autouse = True)
def print_dir():
    print(f"\nFixture LEVEL - 2  is {os.path.abspath(__file__)}")
    print("DONE fixture LEVEL-2 \n")