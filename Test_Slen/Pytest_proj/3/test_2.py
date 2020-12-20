import pytest
@pytest.fixture(scope="module")
def foo(request):
    print('\nfoo setup - module fixture')
    def fin():
        print('foo teardown - module fixture')
    request.addfinalizer(fin)

@pytest.fixture()
def bar(request, foo):
    print('bar setup - function fixture')
    def fin():
        print('bar teardown - function fixture')
    request.addfinalizer(fin)

@pytest.fixture()
def baz(request, bar):
    print('baz setup - function fixture')
    def fin():
        print('baz teardown - function fixture')
    request.addfinalizer(fin)

def test_one(baz):
    print('in test_one()')

# test_2.py::test_one
# foo setup - module fixture
# bar setup - function fixture
# baz setup - function fixture
# in test_one()
# PASSEDbaz teardown - function fixture
# bar teardown - function fixture
# foo teardown - module fixture
