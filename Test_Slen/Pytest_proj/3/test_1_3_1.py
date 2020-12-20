import pytest

def is_odd(number):
    return number % 2 != 0

@pytest.mark.parametrize('even', range(0, 6, 2))
@pytest.mark.parametrize('odd', range(1, 7, 2))
def test_sum_odd_even_returns_odd(odd, even):
    assert is_odd(odd + even)




# # parametrized fixture
# # This achieves the same goal but the resulting code is far, far better!
# # This flavor of fixtures allows to cover a lot of edge cases
# # in multiple tests with minimum redundancy and effort, keeping the test code very neat and clean.
@pytest.fixture(params=range(1, 7, 2))
def odd(request):
    return request.param
@pytest.fixture(params=range(0, 6, 2))
def even(request):
    return request.param

def test_sum_odd_fixture(odd, even):
    assert is_odd(odd + even)

@pytest.fixture(params=[('a', 'a'), ('b', 'c'), ('d', 'd')])
def data(request):
    return request.param

def test_equal(data):
    assert data[0] == data[1]