import pytest

@pytest.mark.usefixtures('add')
def test_adding(add):
    print(add)



