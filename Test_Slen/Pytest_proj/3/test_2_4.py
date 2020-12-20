import pytest
@pytest.fixture()
def foo(request):
    print('\nfoo setup - module fixture')
    yield
    print('\nfoo teardown - module fixture')
    # request.addfinalizer(fin)

@pytest.fixture()
def bar(request):
    print('bar setup - function fixture')
    yield
    print('bar teardown - function fixture')

# @pytest.mark.usefixtures('bar')  # Not working
@pytest.fixture()
# @pytest.mark.usefixtures('bar')  # Not wroking
def baz(request):
    print('baz setup - function fixture')
    yield
    print('\nbaz teardown - function fixture')

@pytest.mark.usefixtures('baz')
@pytest.mark.usefixtures('bar')
@pytest.mark.usefixtures('foo')
def test_one():
    print('\nin test_one()')

# test_2_3.py::test_one
# foo setup - module fixture
# bar setup - function fixture
# baz setup - function fixture
#
# in test_one()
# PASSED
# baz teardown - function fixture
# bar teardown - function fixture

# foo teardown - module fixture
