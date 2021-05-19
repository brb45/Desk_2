#1. ******************************* getpass *********************************
# getpass.getpass(prompt='Password: ', stream=None)
# Prompt the user for a password without echoing. The user is prompted using the string prompt, which defaults to 'Password: '.
# On Unix, the prompt is written to the file-like object stream using the replace error handler if needed.
# stream defaults to the controlling terminal (/dev/tty) or if that is unavailable to sys.stderr (this argument is ignored on Windows)
# getpass()
# from getpass import getpass

# try:
#     passwd = getpass()
#     print(passwd)
# except Exception as er:
#     print(f'er is {er}')
#
# else:
#     print(f"passwd is {passwd}")

import getpass
# pwd = getpass.getpass(prompt = 'What is your favorite colour?')
# if pwd == 'Crimson':
#    print('You are in!')
# else:
#    print('Try Again')

pwd = getpass.getpass(prompt='Password: ', stream=None)
print(pwd)

getpass.getpass(prompt='passwd ', stream=None)
# Warning: Password input may be echoed.
# passwd >? kdkd
# Out[7]: 'kdkd'
username = getpass.getuser()
print(username)
# return user login name
# Out[8]: 'jsun'

www = input("wwww is  ")
print(www)

#2. ******************************* configparser *********************************
from configparser import ConfigParser

#3. ******************************* yield *********************************
# The yield statement returns a generator object
# to the one who calls the function which contains yield, instead of simply returning a value

# if you want to get the values stored inside the generator object, you need to iterate over it
# When you use a function with a return value, every time you call the function,
# it starts with a new set of variables. In contrast, if you use a generator function
# instead of a normal function, the execution will start right from where it left last.

# In Python, generator functions are those functions that, instead of returning a single value,
# return an iterable generator object. You can access or read the values returned
# from the generator function stored inside a generator
# object one-by-one using a simple loop or using next() or list() methods.

# On the whole, yield is a fairly simple statement. Its primary job is to control the flow of a generator
# function in a way that’s similar to return statements. As briefly mentioned above, though,
# the Python yield statement has a few tricks up its sleeve.
#
# When you call a generator function or use a generator expression, you return a special iterator called a generator.
# You can assign this generator to a variable in order to use it. When you call special methods on the generator,
# such as next(), the code within the function is executed up to yield.
#
# When the Python yield statement is hit, the program suspends function execution and returns the yielded value
# to the caller. (In contrast, return stops function execution completely.) When a function is suspended,
# the state of that function is saved. This includes any variable bindings local to the generator,
# the instruction pointer, the internal stack, and any exception handling.



# def gen():
#     print("wht")
#     yield "First item"
#     print('after first')
#     yield "second item"
#     print("after Second")
#     yield "Third Item"
#
# gen_obj = gen()
# print(type(gen_obj))
#
# lst = list(gen_obj)
# # print(lst)
# for v in gen_obj:
#     print(v)

def my_filter(num):
    for v in range(num):
        if v % 2:
            yield v


# for v in my_filter(10):
#     print(v)

res = my_filter(10)
for v in res:
    print(v)


#3. ******************************* profile *********************************
import cProfile
cProfile.run('sum([i * 2 for i in range(10000)])')

# C:\Users\jsun\Documents\Desk_2\venv_3.7.2\Scripts\python.exe C:/Users/jsun/Documents/Desk_2/log_test.py
#          5 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.001    0.001 <string>:1(<listcomp>)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

import sys
nums_squared_lc = [i * 2 for i in range(10000)]
print(sys.getsizeof(nums_squared_lc))
# 43816
nums_squared_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))
# 64

##
# 
# Profile to Optimize Performance
# So, which approach is faster? Should you use list comprehensions or one of their alternatives? 
# Rather than adhere to a single rule that’s true in all cases, it’s more useful to ask yourself whether 
# or not performance matters in your specific circumstance. If not, then it’s usually best to choose 
# whatever approach leads to the cleanest code!
# 
# If you’re in a scenario where performance is important, then it’s typically best to profile 
# different approaches and listen to the data. timeit is a useful library for timing how long it 
# takes chunks of code to run. You can use timeit to compare the runtime of map(), for loops, and list comprehensions:
# 
# import random
# import timeit
# TAX_RATE = .08
# txns = [random.randrange(100) for _ in range(100000)]
# def get_price(txn):
#      return txn * (1 + TAX_RATE)
# 
# def get_prices_with_map():
#      return list(map(get_price, txns))
# 
# def get_prices_with_comprehension():
#      return [get_price(txn) for txn in txns]
# 
# def get_prices_with_loop():
#      prices = []
#      for txn in txns:
#          prices.append(get_price(txn))
#      return prices
# 
# timeit.timeit(get_prices_with_map, number=100)
# 2.0554370979998566
# timeit.timeit(get_prices_with_comprehension, number=100)
# 2.3982384680002724
# timeit.timeit(get_prices_with_loop, number=100)
# 3.0531821520007725
# Here, you define three methods that each use a different approach for creating a list. Then, you tell
# timeit to run each of those functions 100 times each. timeit returns the total time it
# took to run those 100 executions.

##


##

#4. ******************************* list comprehension *********************************
# Using Conditional Logic
# Earlier, you saw this formula for how to create list comprehensions:

# new_list = [expression for member in iterable]

# While this formula is accurate, it’s also a bit incomplete. A more complete description of the comprehension
# formula adds support for optional conditionals. The most common way to add conditional logic
# to a list comprehension is to add a conditional to the end of the expression:

# new_list = [expression for member in iterable (if conditional)]

# Conditionals are important because they allow list comprehensions to filter out unwanted values.

sentence = 'the rocket came back from mars'
vowels = [i for i in sentence if i in 'aeiou']

# You can place the conditional at the end of the statement for simple filtering,
# but what if you want to change a member value instead of filtering it out? In this case,
# it’s useful to place the conditional near the beginning of the expression:

# new_list = [expression (if conditional) for member in iterable]
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]

matrix = [
     [0, 0, 0],
     [1, 1, 1],
     [2, 2, 2],
 ]
flat = [num for row in matrix for num in row]
# [0, 0, 0, 1, 1, 1, 2, 2, 2]

# Nested IF with List Comprehension
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# Transpose of Matrix using Nested Loops
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)
# [[1, 4], [2, 5], [3, 6], [4, 8]]

# Transpose of a Matrix using List Comprehension
matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)
# [[1, 3, 5, 7], [2, 4, 6, 8]]

matrix = [[1, 3, 5, 7], [2, 4, 6, 8]]
transpose = [[row[i] for  row in matrix] for i in range(2)]
print (transpose) # [[1, 2], [3, 4]]

#
my_list = [x * y for x in [20, 40, 60] for y in [2, 4, 6]]
print(my_list)
# [40, 80, 120, 80, 160, 240, 120, 240, 360]
