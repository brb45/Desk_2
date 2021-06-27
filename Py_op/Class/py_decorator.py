# example 1

def run_test(func):
    def add_function(func):
        print("calling default function")
        func()

    print("Not sure if called")
    return add_function(func)


@run_test
def test_f():
    print("whatever")


# Not sure if called
# calling default function
# whatever

# ex 2
def run_test(func):
    def add_function( ):
        print("calling default function")
        func()
    print("Not sure if called")
    return add_function()

@run_test
def test_f():
    print("whatever")

# Not sure if called
# calling default function
# whatever

# ex 3
def test():
    i, j = 99, 199
    print("WU HU")
kk, gg= 33, 66
def run_test(func):
    def add_function( ):
        print("calling add_function()")
        func()
        kk = 999
        print(f"kk is {kk}, and gg is {gg}")
    return add_function # return add_function() --> big difference

@run_test
def test_f():
    print("Calling test_f()")
    kk = 0
    print(f"kk is {kk}")

test_f()
print("END")
# calling add_function()
# Calling test_f()
# kk is 0
# kk is 999, and gg is 66
# END

# ex 4
def decorator_fun(*args, **kwargs):
    # print("Inside decorator")

    def inner(func):
        # code functionality here
        # print("Inside inner function")
        print("I like", kwargs['like'])
        print(f"args[0] is {args[0]}")
        print(f"i is {kwargs['i']}")

        func()

    # reurning inner function
    return inner


@decorator_fun(100, like="geeksforgeeks", i=100)
def my_func():
    print("Inside actual function")


# I like geeksforgeeks
# args[0] is 100
# i is 100
# Inside actual function

# ex 5

def decorator_fun(*args, **kwargs):
    # print("Inside decorator")

    def inner(func):
        # code functionality here
        # print("Inside inner function")
        # print("I like", kwargs['like'])
        # print(f"args[0] is {args[0]}")
        print(f"i is {kwargs['i']}")

        func(args[0],args[1])

    # reurning inner function
    return inner


@decorator_fun(100, 200,like="geeksforgeeks", i=100)
def my_func(i,j):
    print(f"i-->{i}, j --> {j}")
# i is 100
# i-->100, j --> 200

#6
i , j = 55 , 555
def decorator_fun(*args, **kwargs):
    # print("Inside decorator")

    def inner(func):
        # code functionality here
        # print("Inside inner function")
        # print("I like", kwargs['like'])
        # print(f"args[0] is {args[0]}")
        # print(f"i is {kwargs['i']}")

        func(args[0],args[1])

    # reurning inner function
    return inner


@decorator_fun(i,j)
def my_func(i,j):
    print(f"i-->{i}, j --> {j}")
# i-->55, j --> 555
# 7.
# defining a decorator
def hello_decorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behavior
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()

# Hello, this is before function execution
# This is inside the function !!
# This is after function execution






# 8
def decorator3(func):
    def wrapper():
        print("First Function")
        func()
        print("End of Function")
    return wrapper

@decorator3
def test_func():
    print("this is test_func")

test_func()

# 9
# pass function with parameters
def func_called(func):
    def wrapper(a, b):
        print("func_called is called!")
        print(f"{func(a,b)}")
    return wrapper


@func_called
def foo(a,b):
    print("foo is called!")
    return a+b

print(foo(100,200))
# func_called is called!
# foo is called!
# 300
# None

# 10
# importing libraries
import time
import math


# decorator to calculate duration
# taken by any function.
def calculate_time(func):
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
        # storing time before function execution
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1


# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))


# calling the function.
factorial(10)
# 3628800
# Total time taken in :  factorial 2.000807762145996

# 11
def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")

        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")

        # returning the value to the original frame
        return returned_value + 100

    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))
# before Execution
# Inside the function
# after Execution
# Sum = 103

# Decorator with parameters

def decorators(*args, **kwargs):
	def inner(func):
		'''
		do operations with func
		'''
		return func
	return inner #this is the fun_obj mentioned in the above content

@decorators(params)
def func():
	"""
		function implementation
	"""
#
def memoize_factorial(f):
    memory = {}

    # This inner function has access to memory
    # and 'f'
    def inner(*args, **kwargs):
        if num not in memory:
            memory[num] = f(num)
        return memory[num]

    return inner


@memoize_factorial
def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num - 1)

print(facto(5))
# 120

## 12

# A function can be decorated multiple times. We need to define the decorator first
# that we want to wrap the output string with, and then apply them to the function using the ‘@’ .
# One simply needs to place the decorators above the desired function.

Syntax :

@function1
@function2
def function(name):
      print(f"{name}")
Nested decorators follow a bottom to top approach i.e the reverse order.
def italic(func):
    def wrapper():
        return '<i>' + func() + '</i>'

    return wrapper


def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'

    return wrapper


@italic
@strong
def introduction():
    return 'This is a basic program'


print(introduction())
# <i><strong>This is a basic program</strong></i>

# 13
def decor1(func):
    def inner():
        x = func()
        return x * x

    return inner


def decor(func):
    def inner():
        x = func()
        return 2 * x

    return inner


@decor1
@decor
def num():
    return 10


print(num())

# 400






print("________________Python decorator 1 _____________")


# Python program to explain property()
# function using decorator

class Alphabet:
    def __init__(self, value):
        self._value = value

    # getting the values
    @property
    def value(self):
        print('Getting value')
        return self._value

    # setting the values
    @value.setter
    def value(self, value):
        print('Setting value to ' + value)
        self._value = value

    # deleting the values
    @value.deleter
    def value(self):
        print('Deleting value')
        del self._value

    # passing the value


x = Alphabet('Peter')
print(x.value)

x.value = 'Diesel'

del x.value

print("________________End of Python decorator 1 _____________")

print("________________Python decorator 2 _____________")


# Python program to explain property() function

# Alphabet class
class Alphabet:
    def __init__(self, value):
        self._value = value

        # getting the values

    def getValue(self):
        print('Getting value')
        return self._value

        # setting the values

    def setValue(self, value):
        print('Setting value to ' + value)
        self._value = value

        # deleting the values

    def delValue(self):
        print('Deleting value')
        del self._value

    value = property(getValue, setValue, delValue, )


# passing the value
x = Alphabet('GeeksforGeeks')
print(x.value)

x.value = 'GfG'

del x.value

print("________________End of Python decorator 2 _____________")

print("\n\n________________Python decorator 3 _____________")

class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    @full_name.setter
    def full_name(self, value):
        first_name, last_name = value.split(' ')
        self.first_name = first_name
        self.last_name = last_name

    @full_name.deleter
    def full_name(self):
        del self.first_name
        del self.last_name

worker = Person("Jeffery", "Epstain")
print("worker's full name is {}".format(worker.full_name))
worker.full_name = "Gelain Maxwell"
print("worker's full name is {}".format(worker.full_name))


print("________________End of Python decorator 3 _____________")