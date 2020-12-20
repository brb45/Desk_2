
n = 100

def add_spam1(menu = None):
    if menu is None:
        menu = []
    menu.append("spam")
    return menu

def add_spam(menu=[]):
    menu.append("spam")
    return menu
print(add_spam())
print(add_spam())
for _ in range(4):
    print(add_spam())

import sys
def convert(s):
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error {}".format((e)))
        return -1

convert("fail")

def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")
iterable = ['first','snd','third']
#print(first(iterable))
#print(first(iterable))
#print(first(iterable))
#print(first(iterable))

def gen123():
    yield 100
    #yield 2
    yield 3

g = gen123()

for i in g:
    print(i)
#The first stateful generator take()

def take(count, iterable):
    counter = 0
    for i in iterable:
        if counter == count:
            return
        counter += 1
        yield i

def run_take():
    items = [ 2,4,6,8,10]
    for item in take(3,items):
        print(item)

run_take()

print("distinct")
def distinct(iterable):
    seen = set()
    for i in iterable:
        if i in seen:
            continue
        yield i
        seen.add(i)

d_i = [5,7,7,6,5,5]
for i in distinct(d_i):
    print(i)


class Temperature:
  

    def __init__(self, ftmp=32.0):
        self.ftmp = ftmp

    @property  # ctmp   "getter" method
    def ctmp(self):
        return (self.ftmp - 32.0) / 1.8

    @ctmp.setter  # ctmp "setter" method
    def ctmp(self, ctmp):
        self.ftmp = ctmp * 1.8 + 32.0


my_tmp = Temperature()

my_tmp.ctmp = 0

#print('0 C. is', my_tmp.ftmp, 'F.')


my_tmp.ctmp = 100

#print('100C. is', my_tmp.ftmp, 'F.')


my_tmp.ctmp = 50

#print('50C. is', my_tmp.ftmp, 'F.')


my_tmp.ftmp = 86

#print('86F. is', my_tmp.ctmp, 'C.')

def outer(bt_fun, n=1):

    print('bt in test.')
    bt_fun()
    print("exit bt test")

@outer
def bt_fun():
    print("BT doesn't work")
#bt_fun()

from time import time

def diagnostics(f):

    def wrapper(*args, **kwargs):

        print('Executed', f.__name__, 'at', time())

        value = f(*args, **kwargs)

        print('Exited  ', f.__name__, 'at', time())

        print('Arguments:', args)

        print('Value returned:', value, '\n')

        return value

    return wrapper

@diagnostics
def print_nums():
     for i in range(4):
         print(i, end='\t')
     print()



@diagnostics
def calc_hypotenuse(a, b):

    return ((a*a + b*b) ** 0.5)



print_nums()

print (calc_hypotenuse(3, 4))

















