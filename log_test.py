# conftest.py

import pytest

@pytest.fixture(name='XXX', params=[1, 2, 3])
def common_login(request):
    yield request.param

# test_account_login.py

import pytest
@pytest.mark.usefixtures('XXX')
class TestUserLogin:

    def test_01_user_login(self):
        assert 1 == 1


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'log_test.py'])
