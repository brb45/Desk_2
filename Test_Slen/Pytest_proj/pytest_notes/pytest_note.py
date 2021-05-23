python -m pytest -v
python - m pytest - v - s
-s : show print statement

# Disable pytest cache
pytest -p no:cacheprovider

@pytest.mark.parametrize("a,b,expected", [
    (NUMBER_1, NUMBER_2, NUMBER_2),
    (NUMBER_2, NUMBER_1, NUMBER_2),
    (NUMBER_2, NUMBER_2, NUMBER_2),
])
def test_minimum(calculator, a, b, expected):
    answer = calculator.minimum(a, b)
    verify_answer(expected, answer, calculator.last_answer)


@pytest.fixture
def calculator():
    return Calculator()


@pytest.mark.skip
def testadd_2():
	assert 100+200 == 300,"failed"

@pytest.mark.xfail
def testadd_3():
	assert 15+13 == 28,"failed"

conftest
put @pytest.fixture in conftest

@pytest.mark.run_these_please

@pytest.mark.smoke
@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield  # this is where the testing happens

    # Teardown : stop db
    tasks.stop_tasks_db()

with pytest.raises(TypeError):

def test_start_tasks_db_raises():
    """Make sure unsupported db raises an exception."""
    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db('some/great/path', 'mysql')
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'"

@pytest.mark.skip(reason='misunderstood the API')
def test_unique_id_1():
    """Calling unique_id() twice should return different numbers."""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2



@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    """Report the time at the end of a session."""
    yield
    now = time.time()
    print('--')
    print('finished : {}'.format(time.strftime('%d %b %X', time.localtime(now))))
    print('-----------------')


@pytest.fixture(autouse=True)
def footer_function_scope():
    """Report test durations after each function."""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print('\ntest duration : {:0.3} seconds'.format(delta))

--lf, --last-failed - to only re-run the failures.
--ff, --failed-first - to run the failures first and then the rest of the tests. For cleanup

#1. pytest pass parameters to test functions
#1.1 define global input parameters in test file
test_calc_func.py
import os
import pytest
from code_base.calc_func import *

NUMBER_1 = 3.0
NUMBER_2 = 2.0


def test_add():
    value = add(NUMBER_1, NUMBER_2)
    assert value == 5.0


def test_subtract():
    value = subtract(NUMBER_1, NUMBER_2)
    assert value == 1.0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        divide(NUMBER_1, 0)
    assert "division by zero" in str(e.value)

@pytest.mark.parametrize("a,b,expected", [
    (NUMBER_1, NUMBER_2, NUMBER_1),
    (NUMBER_2, NUMBER_1, NUMBER_1),
    (NUMBER_1, NUMBER_1, NUMBER_1),
])
def test_maximum(a, b, expected):
    assert maximum(a, b) == expected

