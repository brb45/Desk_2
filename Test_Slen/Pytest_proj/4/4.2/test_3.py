import pytest


# @pytest.fixture
# def set_up():
#     print("it is time to set up database")
#     time.sleep(0.5)
#
# @pytest.fixture
# def tear_down():
#     print("it is time to wrap up")

def test_fixture(set_up, tear_down, need_parameter):
    print("Start to run test")
    # only called fixture set_up and tear_down,
    # didn't call need_parameter
    assert 1 == 1