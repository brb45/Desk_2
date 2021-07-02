# Ordering Arguments
# When ordering arguments within a function or function call, arguments need to occur in a particular order:
#
# 1. Formal positional arguments
# 2. *args --> treated as a tuple
# 3. Keyword arguments
# 4. **kwargs

def adder(*args):
    print(type(args)) # <class 'tuple'>
    print(args)

var = [1,2,3]
#without unpack
adder(var) # ([1, 2, 3],)
# unpack with *
adder(*var) # (1, 2, 3)





# In practice, when working
# with explicit positional parameters along with * args and ** kwargs, your function would look like this:
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
    print(type(kwargs)) # <class 'dict'>
    print(kwargs)

# But the iterable that is passed as keyword arguments must be a mapping such as a dictionary.
dct = {'param1': 5, 'param2': 8}
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

def my_fun(a, b,  *args, c = 100,**kwargs):
    print(a, b, c)
    print(args)
    print(kwargs.values())

a, b = 1,2
args = ('a', 'b')
my_fun(a,b,  args, d="ppp")
# 1 2 100
# (('a', 'b'),)
# dict_values(['ppp'])


# incorrect to define a function, c=100 should be after *args and before **kwargs
def my_fun(a, b, c = 100, *args, **kwargs):
    print(a, b, c)
    print(args)
    print(kwargs.values())
a, b,c = 1,2, 3
args = ('a', 'b')
# wrong way to pass args
my_fun(a,b, args, d="ppp")
print("--------------------------")
# 1 2 3
# (('a', 'b'),)
# dict_values(['ppp'])

################


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

# kwargs in **kwargs is just variable name. You can very well have **anyVariableName
# kwargs stands for "keyword arguments".

#
#  So we give names param1 and param2 to two parameter values passed to the function as
# follows: func(param1="val1",param2="val2"), instead of passing only values: func(val1,val2).

# Thus, I feel they should be appropriately called "arbitrary number of named arguments" as we can specify
# any number of these parameters (that is, arguments) if func has signature func(**kwargs)
# So being said that let me explain "named arguments" first and then "arbitrary number of named arguments" kwargs.
#
# Named arguments
#
# named args should follow positional args
# order of named args is not important
# Example

def function1(param1, param2="arg2", param3="arg3"):
    print("\n" + str(param1) + " " + str(param2) + " " + str(param3) + "\n")


function1(1)  # 1 arg2 arg3   #1 positional arg
function1(param1=1)  # 1 arg2 arg3   #1 named arg
function1(1, param2=2)  # 1 2 arg3      #1 positional arg, 1 named arg
function1(param1=1, param2=2)  # 1 2 arg3      #2 named args
function1(param2=2, param1=1)  # 1 2 arg3      #2 named args out of order
function1(1, param3=3, param2=2)  # 1 2 3         #


# function1()                      #invalid: required argument missing
# function1(param2=2,1)            #invalid: SyntaxError: non-keyword arg after keyword arg
# function1(1,param1=11)           #invalid: TypeError: function1() got multiple values for argument 'param1'
# function1(param4=4)              #invalid: TypeError: function1() got an unexpected keyword argument 'param4'
# Arbitrary number of named arguments kwargs
#
# Sequence of function parameters:
# positional parameters
# formal parameter capturing arbitrary number of arguments (prefixed with *)
# named formal parameters
# formal parameter capturing arbitrary number of named parameters (prefixed with **)
# Example

def function2(param1, *tupleParams, param2, param3, **dictionaryParams):
    print("param1: " + param1)
    print("param2: " + param2)
    print("param3: " + param3)
    print("custom tuple params", "-" * 10)
    for p in tupleParams:
        print(str(p) + ",")
    print("custom named params", "-" * 10)
    for k, v in dictionaryParams.items():
        print(str(k) + ":" + str(v))


function2("arg1",
          "custom param1",
          "custom param2",
          "custom param3",
          param3="arg3",
          param2="arg2",
          customNamedParam1="val1",
          customNamedParam2="val2"
          )

# Output
#
# param1: arg1
# param2: arg2
# param3: arg3
# custom tuple params ----------
# custom param1,
# custom param2,
# custom param3,
# custom named params ----------
# customNamedParam2:val2
# customNamedParam1:val1
# Passing tuple and dict variables for custom args

# To finish it up, let me also note that we can pass

"formal parameter capturing arbitrary number of arguments" as tuple
variable and
"formal parameter capturing arbitrary number of named parameters" as dict
variable
# Thus the same above call can be made as follows:

tupleCustomArgs = ("custom param1", "custom param2", "custom param3")
dictCustomNamedArgs = {"customNamedParam1": "val1", "customNamedParam2": "val2"}

function2("arg1",
          *tupleCustomArgs,  # note *
          param3="arg3",
          param2="arg2",
          **dictCustomNamedArgs  # note **
          )
# Finally note * and ** in function calls above. If we omit them, we may get ill results.

# Omitting * in tuple args:

function2("arg1",
          tupleCustomArgs,  # omitting *
          param3="arg3",
          param2="arg2",
          **dictCustomNamedArgs
          )
# prints
#
# param1: arg1
# param2: arg2
# param3: arg3
# custom tuple params ----------
# ('custom param1', 'custom param2', 'custom param3'),
# custom named params ----------
# customNamedParam2:val2
# customNamedParam1:val1
# Above tuple ('custom param1', 'custom param2', 'custom param3') is printed as is.
#
# Omitting dict args:

function2("arg1",
          *tupleCustomArgs,
          param3="arg3",
          param2="arg2",
          dictCustomNamedArgs  # omitting **
          )
# gives
#
# dictCustomNamedArgs

# SyntaxError: non-keyword arg after keyword arg

