import pytest
@pytest.fixture(scope="module")
def foo(request):
    print('\nfoo setup - module fixture')
    yield
    print('\nfoo teardown - module fixture')
    # request.addfinalizer(fin)

@pytest.fixture()
def bar(request, foo):
    print('bar setup - function fixture')
    yield
    print('bar teardown - function fixture')


@pytest.fixture()
def baz(request, bar):
    print('baz setup - function fixture')
    yield
    print('\nbaz teardown - function fixture')


def test_one(baz):
    print('\nin test_one()')

# test_2.py::test_one
# foo setup - module fixture
# bar setup - function fixture
# baz setup - function fixture
# in test_one()
# PASSEDbaz teardown - function fixture
# bar teardown - function fixture
# foo teardown - module fixture
