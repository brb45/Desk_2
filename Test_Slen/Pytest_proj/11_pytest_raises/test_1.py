# We can uses pytest.raises() to assert that a block of code raises a specific exception.
# Using pytest.raises is to test exceptions, that your own code is deliberately raising,

# whereas using @pytest.mark.xfail with a check function is probably better for
# something like documenting unfixed bugs (where the test describes what “should” happen) or bugs in dependencies
import pytest

def test_divide_NonZero():
    with pytest.raises(ZeroDivisionError) as excinfo:
        2/1
    assert "maximum recursion" in str(excinfo.value)

def testdivide_zero():
    with pytest.raises(ZeroDivisionError) as e:
        2/0
        print(e)
    # assert "maximum recursion" in str(e.value)



@pytest.mark.xfail(raises=ZeroDivisionError)
def testdivide_zero1():
    with pytest.raises(ZeroDivisionError) as e:
        2/0
        print(e)
    # assert "maximum recursion" in str(e.value)


@pytest.mark.xfail(raises=ZeroDivisionError)
def test_divide_NonZero2():
    with pytest.raises(ZeroDivisionError) as exe_error:
        2/1
        print(f"\nexe_error is {exe_error}")