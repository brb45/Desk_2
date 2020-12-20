import time
import sys
import os

# os.system("pause")
###################################################################################################
####
# zip, map, and filter all return an iterator
# zip takes tuple of iterables and return an iterable of tuples
dic1 = {'wi': 1, 'bt': 2, "HD":3}
dic2 = {'abg': 6, 'abx': 4, "adc": 5}
dic3 = {'k':7, 'u':8, 'X':9}
dic4 = {'k':7, 'u':8}


merg1 = zip(dic1, dic2, dic3 )
while True:
    try:
        print(next(merg1))
    except:
        break
#
# ('wi', 'abg', 'k')
# ('bt', 'abx', 'u')
# ('HD', 'adc', 'X')

merg1 = zip(dic1, dic2, dic4 )
while True:
    try:
        print(next(merg1))
    except:
        break
# ('wi', 'abg', 'k')
# ('bt', 'abx', 'u')

#
list1 = ['Alpha', 'Beta', 'Gamma', 'Sigma']
list2 = ['one', 'two', 'three', 'six']

iter_zip = zip(list1, list2)

a, b = zip(*iter_zip)
print(f"type(a) is {type(a)}, and a is {a}")
# type(a) is <class 'tuple'>, and a is ('Alpha', 'Beta', 'Gamma', 'Sigma')

a  = zip(*iter_zip)
print(type(a)) # <class 'zip'>
print(list(a)) # [('Alpha', 'Beta', 'Gamma', 'Sigma'), ('one', 'two', 'three', 'six')]

list1 = ['Alpha', 'Beta', 'Gamma', 'Sigma']
list2 = ['one', 'two', 'three', 'six']

iter_zip = zip(list1, list2)

# unzipping
a, b = zip(*iter_zip)
print(f"type(a) is {type(a)}, and a is {a}")
# type(a) is <class 'tuple'>, and a is ('Alpha', 'Beta', 'Gamma', 'Sigma')

list_zip = list(zip(list1, list2))
c, d = zip(*list_zip)
print(f"typeOf c is {type(c)}")
print(f"c is {c}")
# typeOf c is <class 'tuple'>
# c is ('Alpha', 'Beta', 'Gamma', 'Sigma')

##
list1 = ['Alpha', 'Beta', 'Gamma', 'Sigma']
# list is iterable, but not iterator
# iter(list) turn a list to an iterator
# print(next(list1))
list1 = iter(list1)
try:
    while True:
        item_a = next(list1)
        print(item_a, end=", ")
except:
    print("\ndone")
# Alpha, Beta, Gamma, Sigma,
# done

sorted(nums, key = len)
sorted(strs, key = str.lower)

####
x = lambda a : a + 10
print(x(5))

t = lambda a, b : a+ b
print(t(100, 1))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))

#@@
Input: ["23:59", "00:00"]

def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        tp = sorted(map(int, p.split(':')) for p in timePoints)
        tp += [[tp[0][0] + 24, tp[0][1]]]
        return min((tp[x+1][0] - tp[x][0]) * 60 + tp[x+1][1] - tp[x][1]
                   for x in range(len(tp) - 1))

#map returns an iterator
def multiply2(x):
    return x * 2

a = map(multiply2, [1, 2, 3, 4])  # Output [2, 4, 6, 8]
print(list(a))
# [2, 4, 6, 8]

def to_upper_case(s):
    return str(s).upper()

# map returns an map object, which is an iterator
map_iterator = map(to_upper_case, 'abc')
print(list(map_iterator))
# ['A', 'B', 'C']

#
list_numbers = [1, 2, 3, 4]
map_iterator = map(lambda x: x * 2, list_numbers)
print(list(map_iterator))
# [2, 4, 6, 8]
#
list_numbers = [1, 2, 3, 4]
tuple_numbers = (5, 6, 7, 8)
map_iterator = map(lambda x, y: x * y, list_numbers, tuple_numbers)
print(list(map_iterator))
# [5, 12, 21, 32]

list_of_dict = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

map(lambda x: x['name'], list_of_dict)  # Output: ['python', 'java']

map(lambda x: x['points'] * 10, list_of_dict)  # Output: [100, 80]

map(lambda x: x['name'] == "python", list_of_dict)  # Output: [True, False]


# filter returns an iterator
a = [1, 2, 3, 4, 5, 6]
b=filter(lambda x : x % 2 == 0, a) # Output: [2, 4, 6]

list_of_dict = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
b = filter(lambda x : x['name'] == 'python', list_of_dict)  # Output: [{'name': 'python', 'points': 10}]
