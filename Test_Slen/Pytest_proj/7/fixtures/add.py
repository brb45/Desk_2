import pytest

@pytest.fixture
def add():
    print("True")
    return 100

