import pytest

def test_params(params):
    print(params)
    assert params['username'] == 'test@gmail.com'
    assert params['password'] == '12345'


# pytest -s -v test_1.py  --username=test@gmail.com --password=12345