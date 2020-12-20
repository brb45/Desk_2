import pytest
import time

@pytest.fixture
def set_up():
    print("it is time to set up database")
    time.sleep(0.5)
    assert 1 == 2
    yield
    print("\nsetup is done")

@pytest.fixture
def tear_down():
    print("it is time to wrap up")

@pytest.fixture
def need_parameter():
    def _need(param1, param2):
        total = param1 + param2
        print(f"sum is {total}")
        return total

    return _need