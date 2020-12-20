import pytest


# @pytest.fixture
# def set_up():
#     print("it is time to set up database")
#     time.sleep(0.5)
#
# @pytest.fixture
# def tear_down():
#     print("it is time to wrap up")

# @pytest.fixture
# def need_parameter():
#     def _need(param1, param2):
#         total = param1 + param2
#         print(f"sum is {total}")
#         return total
#
#     return _need

def test_fixture(set_up, tear_down, need_parameter):
    print("Start to run test")
    total = need_parameter(100, 200)
    print(f"total = {total}")

    assert 1 == 1