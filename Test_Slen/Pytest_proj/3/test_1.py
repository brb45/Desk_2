import pytest
@pytest.fixture( params=[1,2,3] )
def test_data(request):
    return request.param

def test_not_2(test_data):
    print('test_data: %s' % test_data)
    assert test_data != 2

@pytest.fixture(params=["third", ("offer", "tuple"), "Last", ["check", 'balance']])
def qa_data(request):
    return request.param

def test_fixture_params(qa_data):

    print(f"qa_data is {qa_data}")


@pytest.mark.parametrize("src, target", [("a",100), ("d",400), ("c",300),("b",200)])
def test_params(src, target):
    print(f"\nsrc is {src}")
    print(f"target is {target}")


# Mix parametrize and fixture
@pytest.mark.parametrize("src, target", [("a",100),("b",200), ("c",300), ("d",400)])
def test_mixture(src, target, qa_data):
    print(f"\nqa_data is {qa_data}")
    print()
    print(f"parametrize data is {src} and {target}")


def is_odd(number):
    return number % 2 != 0

@pytest.mark.parametrize('even', range(0, 10, 2))
@pytest.mark.parametrize('odd', range(1, 11, 2))
def test_sum_odd_even_returns_odd(odd, even):
    assert is_odd(odd + even)

# parametrized fixture
# This achieves the same goal but the resulting code is far, far better!
# This flavor of fixtures allows to cover a lot of edge cases
# in multiple tests with minimum redundancy and effort, keeping the test code very neat and clean.
@pytest.fixture(params=range(1, 11, 2))
def odd(request):
    return request.param
@pytest.fixture(params=range(0, 10, 2))
def even(request):
    return request.param

def test_sum_odd_fixture(odd, even):
    assert is_odd(odd + even)