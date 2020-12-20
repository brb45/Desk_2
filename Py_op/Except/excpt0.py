SyntaxError
NameError
ZeroDivisionError
AttributeError


TypeError
KeyError
ValueError

#1. Rasing an exception
class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even number can be added")
        super().append(integer)

e = EvenOnly()
# e.append("a string")
# e.append(3)
# e.append(2)

# 1.1 raise
def no_return():
    print("About to raise an exception")
    raise Exception("This is always raised")
    print("this line will never execute")
    return "I won't be returned"

# a = no_return()
#     raise Exception("This is always raised")
# Exception: This is always raised

#2 except handling with try/except block
try:
    no_return()
except: #too broad
    print("I caught an exception")
# I caught an exception
##
try:
    no_return()
except Exception:
# except BaseException:
    print("I caught an exception")
# I caught an exception
##
try:
    no_return()
except BaseException:
    print("I caught an exception")
# I caught an exception

#2.1
def test_division(divider):
    try:
        return 100/divider
    except ZeroDivisionError:
        return "Zero is not a good idea"

#2.2
def test_division1(divider):
    try:
        if divider == 13:
            raise ValueError("12 is an unlucky number")
        return 100 / divider
    except (ZeroDivisionError, TypeError):
        return "Enter a number other than zero"

# test_division1(13)
#     raise ValueError("12 is an unlucky number")
# ValueError: 12 is an unlucky number

# test_division1(0)
# No printout

# test_division1('s')
# unsupported operand type(s) for /: 'int' and 'str'

#2.3
def funny_division3(divider):
    try:
        if divider == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divider
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        print("No, No, not 13!")
        raise



