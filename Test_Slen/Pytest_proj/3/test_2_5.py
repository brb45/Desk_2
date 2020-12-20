import pytest
# fixtures with autouse=True always run first before any other fixtures or tests

@pytest.fixture()
def foo(request):
    print('\nfoo setup - module fixture')
    yield
    print('foo teardown - module fixture')
    # request.addfinalizer(fin)

@pytest.fixture(autouse=True)
def bar(request):
    print('\nbar setup - function fixture')
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
@pytest.mark.usefixtures('foo')
def test_one():
    print('\nin test_one()')

# test_2_5.py::test_one
# bar setup - function fixture
#
# foo setup - module fixture
# baz setup - function fixture
#
# in test_one()
# PASSED
# baz teardown - function fixture
# foo teardown - module fixture
# bar teardown - function fixture
