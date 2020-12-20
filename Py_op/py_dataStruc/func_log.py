# 1.
def check():
    pass

if check() is None:
    print("check() is ", check())
# check() is  None

#2.
def check():
    pass

if check():
    print("check() is ", check())
else:
    print(f"Retuning {check()} is False")
# Retuning None is False

#3.
def return_value_and_None():
    a = 10
    if a == 1:
        return a
    else:
        #return None
        pass # Same

print(f"return_value_and_None() is {return_value_and_None()}")
# return_value_and_None() is None
#4

def my_fun(*args):
    for i in range(len(args)):
        print(args[i], end=", ")
    # for ele in args:
    #     print(ele, end=", ")
    print()
my_fun(1,2,3) # 1, 2, 3,
tuple_data = (1,2,3)
list_data = [4,5,6]
set_data = {7,8,9}

my_fun(tuple_data) # (1, 2, 3),

# tuple unpacking
my_fun(*tuple_data) # 1, 2, 3,

my_fun(*list_data)
# 4, 5, 6,

my_fun(*set_data)
# 8, 9, 7,

def my_fun1(i, j, *args):
    print(i, j)
    print(len(args))

my_fun1(100, 200, 1,2)
# 100 200
# 2

# 5.

def helper(a,b, c):
    return a, b,c

print(type(helper(1,3, 5)))
# <class 'tuple'>


def helper(a,b):
    return a, b

print(type(helper(1,3)))
# <class 'tuple'>

# 6.
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









