# test/conftest.py
import pytest

def pytest_addoption(parser):
    parser.addoption("--username", action="store", help="input useranme")
    parser.addoption("--password", action="store", help="input password")

@pytest.fixture
def params(request):
    params = {}
    params['username'] = request.config.getoption('--username')
    params['password'] = request.config.getoption('--password')
    if params['username'] is None or params['password'] is None:
        pytest.skip()
    return params