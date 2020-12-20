import pytest
@pytest.fixture( params=[1,2,3] )
def data_for_test(request):
    return request.param

def test_data_1(data_for_test):
    print(f'data_for_test: {data_for_test}')
    assert data_for_test != 2
#

@pytest.mark.usefixtures('data_for_test')
def test_data_2(data_for_test):
    print(f'data_for_test: {data_for_test}')
    assert data_for_test != 2

@pytest.mark.usefixtures('data_for_test')
def test_data_3():
    print(f'data_for_test: {data_for_test}')
    # assert data_for_test() != 2 # error
    # Fixture "data_for_test" called directly. Fixtures are not meant to be called
    # directly, but are created automatically when test functions request them
    # as parameters.
