"""Demonstrate fixture renaming."""

import pytest

# use fixture to pass parameters
@pytest.fixture(name='const')
def data_constant():
    """Return ultimate answer."""
    return 42


def test_const_val(const):
    """Use the shorter name."""
    print(f"\nconst is {const}")
    assert const == 42
