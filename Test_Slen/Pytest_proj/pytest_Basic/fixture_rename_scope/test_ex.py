"""Demonstrate autouse fixtures."""
# 11/22/20
# 5/20/21

# Using autouse for Fixtures That Always Get Used
# So far in this chapter, all of the fixtures used by tests were named by the tests
# (or used usefixtures for that one class example). However, you can use autouse=True
# to get a fixture to run all of the time.
import pytest
import time
from datetime import datetime


@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    """Report the time at the end of a session."""
    print('\n[footer_session_scope] starts')
    yield
    now = time.time()

    print('[footer_session_scope]: finished : {}'.format(time.strftime('%d %b %X', time.localtime(now))))
    print('[footer_session_scope]: ends')


@pytest.fixture(autouse=True)
def footer_function_scope():
    """Report test durations after each function."""
    print("(footer_function_scope) starts")
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print(f'\n(footer_function_scope)--> test duration : {delta:0.5} seconds')
    print("(footer_function_scope) --> ends")

def test_1():
    """Simulate long-ish running test."""
    print("test_1 starts")
    time.sleep(1)
    assert 0 == 0
    print("test_1 ends")

# @pytest.mark.skip("reason to skip")
# @pytest.mark.skipif(a > 10, reason="Give a reason")
# @pytest.mark.skip("Testing on skip; skip test_2()")
a= 100
@pytest.mark.skipif(a > 10, reason="a>10")
def test_2():
    """Simulate slightly longer test."""
    print("test_2 starts")
    time.sleep(2)
    print("test_2 ends")
    assert 1 == 2

def test_3():
    """Simulate slightly longer test."""
    print("test_3 starts")
    time.sleep(2)
    print("test_3 ends")
    assert 1 == 2


#---------------------------------------
#
# run specific test
# -k function-name-expression
# python -m pytest -v -s -k test_3

## pytest.mark.groupname
## python -m pytest -v -s -k test_group_1
@pytest.mark.test_group_1
def test_4():
    """Simulate slightly longer test."""
    print("test_4 starts")
    time.sleep(2)
    print("test_4 ends")
    assert 1 == 2
@pytest.mark.test_group_1
def test_4_1():
    """Simulate long-ish running test."""
    print("test4_1 starts")
    time.sleep(1)
    assert 0 == 0
    print("test4_1 ends")













