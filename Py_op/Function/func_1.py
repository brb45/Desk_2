# Ordering Arguments
# When ordering arguments within a function or function call, arguments need to occur in a particular order:
#
# 1. Formal positional arguments
# 2. *args
# 3. Keyword arguments
# 4. **kwargs


# In practice, when working
# with explicit positional parameters along with * args and ** kwargs, your function would look like this:
#
#
# def example(arg_1, arg_2, *args, **kwargs):
#     ...
# And, when working
# with positional parameters along with named keyword parameters in addition to * args and ** kwargs, your function would look like this:
#

# def example2(arg_1, arg_2, *args, kw_1="shark", kw_2="blobfish", **kwargs):
#     ...

# unpacking operator (*)
# Using the Python args Variable in Function Definitions

# *args allow a function to take any number of positional arguments.

# Before the second example, it is better to explain the difference between a positional argument and a key word argument.
# Positional arguments are declared by a name only.
# Keyword arguments are declared by a name and a default value.

# When a function is called, values for positional arguments must be given. Otherwise, we will get an error.
# If we do not specify the value for a keyword argument, it takes the default value.


def addition(a, b=2): #a is positional, b is keyword argument
   return a + b
print(addition(1))
# 3
def addition(a, b): #a and b are positional arguments
   return a + b
print(addition(1))
# TypeError: addition() missing 1 required positional argument: 'b'

#-----------------------------
def arg_printer(a, b, *args):
   print(f'a is {a}')
   print(f'b is {b}')
   print(f'args are {args}')
arg_printer(3, 4, 5, 8, 3)
# a is 3
# b is 4
# args are (5, 8, 3)
# The first two values are given to a and b. The remaining values are stored in the args tuple.

#--------------
# Python wants us to put keyword arguments after positional arguments. We need to keep that in mind when calling a functions.
# Consider the following example:
# arg_printer(a=4, 2, 4, 5)
# SyntaxError: positional argument follows keyword argument
#____________________________________
# In the following function, the option is a keyword argument (it has a default value).
def addition(a, b, *args, option=True):
   result = 0
   if option:
      for i in args:
      result += i
      return a + b + result
   else:
      return result
# This function performs addition operation if option is True.
# Since the default value is True, the function returns the sum of the arguments unless option parameter is declared as False.
print(addition(1,4,5,6,7))
# 23
print(addition(1,4,5,6,7, option=False))
# 0
#--------------------------------------------------------------
# The **kwargs collect all the keyword arguments that are not explicitly defined.
# Thus, it does the same operation as *args but for keyword arguments.
# **kwargs allow a function to take any number of keyword arguments.
# By default, **kwargs is an empty dictionary. Each undefined keyword argument is stored as a key-value pair in the **kwargs dictionary.
def arg_printer(a, b, option=True, **kwargs):
   print(a, b)
   print(option)
   print(kwargs)
arg_printer(3, 4, param1=5, param2=6)
# 3 4
# True
# {'param1': 5, 'param2': 6}


#-----------------------------------------
# We can use both *args and **kwargs in a function but *args must be put before **kwargs.
def arg_printer(a, b, *args, option=True, **kwargs):
   print(a, b)
   print(args)
   print(option)
   print(kwargs)
arg_printer(1, 4, 6, 5, param1=5, param2=6)
# 1 4
# (6, 5)
# True
# {'param1': 5, 'param2': 6}

#-----------------------------------------

# We can pack and unpack variables using *args and **kwargs.
def arg_printer(*args):
   print(args)
# If we pass a list to the function above, it will stored in args tuple as one single element.
lst = [1,4,5]
arg_printer(lst)
# ([1, 4, 5],)

# If we put an asterisk before lst, the values in the list will be unpacked and stored in args tuple separately.
lst = [1,4,5]
arg_printer(*lst)
# (1, 4, 5)


# We can pass multiple iterables to be unpacked together with single elements. All values will be stored in the args tuple.
lst = [1,4,5]
tpl = ('a','b',4)
arg_printer(*lst, *tpl, 5, 6)
# (1, 4, 5, 'a', 'b', 4, 5, 6)

# We can do the packing and unpacking with keyword arguments as well.
def arg_printer(**kwargs):
   print(kwargs)
# But the iterable that is passed as keyword arguments must be a mapping such as a dictionary.
dct = {'param1':5, 'param2':8}
arg_printer(**dct)
# {'param1': 5, 'param2': 8}

def arg_printer(**kwargs):
   print(kwargs)
# But the iterable that is passed as keyword arguments must be a mapping such as a dictionary.
dct = {'param1':5, 'param2':8}
arg_printer(**dct)
# {'param1': 5, 'param2': 8}
#----
# If we also pass additional keyword arguments together with a dictionary, they will combined and stored in the kwargs dictionary.
dct = {'param1':5, 'param2':8}
arg_printer(param3=9, **dct)
# {'param3': 9, 'param1': 5, 'param2': 8}


#______________________________________________________________________
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))


# Note that args is just a name. You’re not required to use the name args.
# You can choose any name that you prefer, such as integers:

# Bear in mind that the iterable object you’ll get using the unpacking operator * is not a list but a tuple.
# A tuple is similar to a list in that they both support slicing and iteration.
# However, tuples are very different in at least one aspect: lists are mutable, while tuples are not.

# sum_integers_args_2.py
def my_sum(*integers):
    result = 0
    for x in integers:
        result += x
    return result

print(my_sum(1, 2, 3))

#
# Using the Python kwargs Variable in Function Definitions
# Like args, kwargs is just a name that can be changed to whatever you want.
# Again, what is important here is the use of the unpacking operator (**)
# Note that in the example above the iterable object is a standard dict

def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += "-"+arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
# -Real-Python-Is-Great-!
dic = dict(a="Real", b="Python", c="Is", d="Great", e="!")

# Ordering Arguments in a Function
# Now that you have learned what *args and **kwargs are for, you are ready to start writing functions
# that take a varying number of input arguments.
#
# But what if you want to create a function that takes a changeable number of both positional and named arguments?
#
# In this case, you have to bear in mind that order counts.
# Just as non-default arguments have to precede default arguments, so *args must come before **kwargs.
#
# To recap, the correct order for your parameters is:
#
#1. Standard arguments
#2. *args arguments
#3. **kwargs arguments

# correct_function_definition.py
def my_function(a, b, *args, **kwargs):
    pass

def my_fun(a, b, c = 100, *args, **kwargs):
    print(a, b, c)
    print(args)
    print(kwargs.values())

a, b,c = 1,2, 3
args = ('a', 'b')
# wrong way to pass args
my_fun(a,b, c, args, d="ppp")
print("--------------------------")
# 1 2 3
# (('a', 'b'),)
# dict_values(['ppp'])

my_fun(a,b,c, *args, d="ppp")
print("&&&&&&&&&&&&&&&&&&")


kwargs = {"k":"KKK", "g":"GGG"}
# Wrong way to pass kwargs
my_fun(a,b, c, args, kwargs)
# 1 2 3
# (('a', 'b'), {'k': 'KKK', 'g': 'GGG'})
#dict_values([])
print("!!!!!!!!!!!!!!!!!!!!")
my_fun(a,b, c, *args, **kwargs)

#*******************************
# my_fun(a,b, *args, **kwargs)

print(*args)
# a b
kwargs = {"k":"KKK", "g":"GGG"}
# print((**kwargs).values())










my_list = [1, 2, 3]
print("\n", my_list) # [1, 2, 3]
print(*my_list) # 1 2 3

# When you use the * operator to unpack a list and pass arguments to a function,
# it’s exactly as though you’re passing every single argument alone.
# This means that you can use multiple unpacking operators to get values from several lists and pass them all to a single function.