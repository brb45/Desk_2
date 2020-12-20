# import pytest
#
# def test_divide_NonZero():
#     with pytest.raises(ZeroDivisionError):
#         2/1
#
# def test_divide_zero():
#     with pytest.raises(ZeroDivisionError):
#         2/0

import re
import pytest

def check_email_format(email):
    """check that the entered email format is correct"""
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        raise Exception("Invalid email format")
    else:
        return "Email format is ok"

def test_email_exception():
    """test that exception is raised for invalid emails"""
    with pytest.raises(Exception):
        assert check_email_format("good@email.com")


def test_email_exception_mod():
    """test that exception is raised for invalid emails"""
    with pytest.raises(Exception) as e:
        assert check_email_format("bademail.com")
    assert str(e.value) == "Invalid email format"
