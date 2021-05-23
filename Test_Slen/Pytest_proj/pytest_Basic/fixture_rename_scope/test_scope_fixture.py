"""Demo fixture scope."""
# 11/22/20
# 5/20/21
import pytest


@pytest.fixture(scope='function')
def func_scope():
    print()
    print("[func_scope] Starts")


@pytest.fixture(scope='module')
def mod_scope():
    print()
    print("[[mod_scope]] starts")


@pytest.fixture(scope='session')
def sess_scope():
    print()
    print("(sess_scope) starts")


@pytest.fixture(scope='class')
def class_scope():
    print()
    print("{class_scope} starts")
    """A class scope fixture."""


def test_1(sess_scope, mod_scope, func_scope):
    print()
    print("test_1 Starts")


def test_2(sess_scope, mod_scope, func_scope):
    print("test_2 Starts")

@pytest.mark.usefixtures('class_scope')
class TestSomething():
    """Demo class scope fixtures."""

    def test_3(self):
        print()
        print("Class Test--> test_3 Starts")

    def test_4(self):
        print()
        print("Class Test--> test_4 Starts")


# pytest test_scope_fixture.py::test_1 -v -s
# test_scope_fixture.py::test_1
# (sess_scope) starts
#
# [[mod_scope]] starts
#
# [func_scope] Starts
#
# test_1 Starts
# PASSED


# test_scope.py::test_2
# [func_scope] Starts
# test_2 Starts
# PASSED


# test_scope.py::TestSomething::test_3
# {class_scope} starts
#
# Class Test--> test_3 Starts
# PASSED

# class_scope only happens once for all the methods in a class

# test_scope.py::TestSomething::test_4
# Class Test--> test_4 Starts
# PASSED