# A callable is anything you can call, using parenthesis, and possibly passing arguments.

# We have a number of callables in Python:
#
# Functions are callables
# Classes are callables
# Methods (which are functions that hang off of classes) are callables

# Instances of classes are NOT callable, but can be turned into callables
# If an object is an instance of some class then it is callable if the class has __call__ attribute.

# if your class has an explicit __call__ method, its instances are callable


def Geek():
    return 5

# an object is created of Geek()
let = Geek
print(callable(let)) # True

# a test variable
num = 5 * 5
print(callable(num)) # False


class Geek:
    def __init__(self):
        self.me = 'king'
        print('Hello GeeksforGeeks')

    # Suggests that the Geek class is callable


print(callable(Geek)) # True

# the instance of Geek is not callable()
print(callable(Geek()))  # False

# >>> zip
# <class 'zip'>
# >>> len
# <built-in function len>
# >>> int
# <class 'int'>

# >>> reversed
# <class 'reversed'>
# >>> enumerate
# <class 'enumerate'>
# >>> range
# <class 'range'>
# >>> filter
# <class 'filter'>


