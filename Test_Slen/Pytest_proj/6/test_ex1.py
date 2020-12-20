# Let's create a function that takes every argument
print("------------------------------------")
def foo(*args, **kwargs):
    return (args, kwargs)

print(foo())  # ((), {})
print(foo('a', 'b'))  # (('a', 'b'), {})
print(foo(('c',100))) # ((('c', 100),), {})
print(foo(a=100)) # ((), {'a': 100})
# print(foo('b'=100)) # error

print(foo('a', b=2, c='test')) # (('a',), {'b': 2, 'c': 'test'})

import pytest

@pytest.fixture
def argument_printer():
    def _foo(*args, **kwargs):
        return (args, kwargs)
    return _foo

def test_ex_1(argument_printer):
    first_case = argument_printer('a', 'b', c=100)
    assert first_case == (('a','b'), {'c': 100})
    print("it works the first time")

    second_case = argument_printer('a', b=2, c='test')
    assert second_case != (('a',), {'b': 2, 'c': 'test'})

    print("it works the second time")

