import pytest

@pytest.mark.parametrize("src, target", [("a",100), ("d",400), ("c", 'c'),("b",200)])
def test_params(src, target):
    print(f"\nsrc is {src}")
    print(f"target is {target}")
    assert src == target

@pytest.fixture(params=["third", ("offer", "tuple"), "Last"])
def qa_data(request):
    return request.param
# Mix parametrize and fixture
@pytest.mark.parametrize("src, target", [("a",100),("b",200)])
def test_mixture(src, target, qa_data):
# def test_mixture(qa_data, src, target):
# def test_mixture(src, qa_data, target):
    print(f"parametrize data is {src}, {target} and {qa_data}")

