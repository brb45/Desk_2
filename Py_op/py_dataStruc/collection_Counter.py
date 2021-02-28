
#____________________________________________________________________________________
from collections import Counter

# 1. Counter takes input as an iterables
from collections import Counter as CNT

# return a zero count for missing items instead of raising a KeyError:
# Setting a count to zero does not remove an element from a counter
# use pop(key) to remove

# initiate Counter with iterable
# ss = CNT(10)
# TypeError: 'int' object is not iterable
#

b = Counter("")
print(len(b)) # 0

cnt_d = Counter("")
print(cnt_d[""])  # 0

from collections import Counter

s = ['a','b','c','c','b','a','d']
s = 'abccbad'
cnt = Counter(s)


res = cnt.elements()
print(type(res)) # <class 'itertools.chain'>
print(list(res)) # ['a', 'a', 'b', 'b', 'c', 'c', 'd']

res = cnt.most_common()
print(type(res)) # <class 'list'>
print(res) # [('a', 2), ('b', 2), ('c', 2), ('d', 1)]

res = cnt.most_common(2)
print(res) # [('a', 2), ('b', 2)]


# 2. elements() --> returns an iterable
a = Counter({'d': 2, 'b': 1, "c": 3, 'a': 3})
# print(type(a)) <class 'collections.Counter'>
# res = a.elements() <class 'itertools.chain'>
# print(list(res))
# ['d', 'd', 'b', 'c', 'c', 'c', 'a', 'a', 'a']
# list(res) is not sorted.

# 2.1 elements() returns --> an iterator

# what to do with iterator
# 2.2 convert to a list
toList = list(a_elements)
# print(f"toList is {toList}")
# toList is ['d', 'd', 'b', 'c', 'c', 'c', 'a', 'a', 'a']

# 2.3 convert to a set
toSet = set(a_elements_1)
# print(f"toSet is {toSet}")
# toSet is {'b', 'a', 'c', 'd'}

# 2.4 convert to a string
toString = "".join(a_elements_str)
# print(f"type(toString) is {type(toString)}")
# type(toString) is <class 'str'>
# print(f"toString is {toString}")
# toString is ddbcccaaa

#3. .most_common(), returns a list of ordered tuples
# It can be used as a priority Queue
# .most_common(num)

rst = a.most_common()
# Returns a list of tuples
# print(f"type(rst) is {type(rst)}")
# type(rst) is <class 'list'>
# print(f"rst is {rst}")
# rst is [('c', 3), ('a', 3), ('d', 2), ('b', 1)]

b = Counter({'a':3, 'd': 7, 'e': 3, 'd':5,  'b': 1, "c": 3, 'f': 3})
# rst = b.most_common()
# print(rst)
# [('d', 5), ('a', 3), ('e', 3), ('c', 3), ('f', 3), ('b', 1)]

# rst = b.most_common(1)
# print(rst)
# [('d', 5)]

# rst = b.most_common(3)
# print(rst)
# [('d', 5), ('a', 3), ('e', 3)]


# if there is duplicate key, the latter key is taken
c = Counter({'a':3, 'd': 7, 'e': 3, 'd':5,  'b': 1, "c": 3, 'f': 3})
c['a']=0
# print(c['a']) # 0
rst = c.most_common() # [('d', 5), ('e', 3), ('c', 3), ('f', 3), ('b', 1), ('a', 0)]
# print(rst)

d = Counter({'a':3, 'd': 7, 'e': 3, 'd':5,  'b': 1, "c": 3, 'f': 3})
d['a']=0
# print(d['a']) # 0
rst = d.most_common() # [('d', 5), ('e', 3), ('c', 3), ('f', 3), ('b', 1), ('a', 0)]
# print(rst)
d.pop('a')
rst = d.most_common() #  [('d', 5), ('e', 3), ('c', 3), ('f', 3), ('b', 1)]
# print(rst)
#4.
# Setting a count to zero does not remove an element from a counter. Use del to remove it entirely:
rst.pop('d')
del rst['e']

# 5.
# Counter intialized with strings
from collections import Counter
str_dict = Counter("mumltlmee reum")
rst_lst = str_dict.most_common()
# [('m', 4), ('e', 3), ('u', 2), ('l', 2), ('t', 1), (' ', 1), ('r', 1)]

# Counter intialized with list
chr_lst = ['e','a','b','g','e','b','e','g','b']
chr_cnter =  Counter(chr_lst)
rst_lst = chr_cnter.most_common()
print(rst_lst)

#____________________________________________________________
from collections import Counter
arr = [0,0,1,2,4,8, -1,-2,-4,-8]
dic = Counter(arr)
nums = sorted(dic, key=abs)
print(nums) # # [0, 1, -1, 2, -2, 4, -4, 8, -8]
print(dic[100]) # missing key will return value as 0; not rasing an error
# 0

def canReorderDoubled(A):
    c = collections.Counter(A)
    for x in sorted(c, key=abs):
        if c[x] > c[2 * x]:
            return False
        c[2 * x] -= c[x]
    return True

#__________________________________________________________________________________________
from collections import Counter
# Counter is a sub-class of dict, has all dict's interfaces, val is freq of key
# Take a list as input
# elements() returns an iterator
# most_common() returns a list of tuple of key and value


import collections

print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))

print(collections.Counter({'a': 2, 'b': 3, 'c': 1}))

print(collections.Counter(a=2, b=3, c=1))

import collections

c = collections.Counter()
c.update("abcdaab")
print("*****", c, sep="    ")
c.update({"a": 10, "d": 5})
print(c)
c.update(["a", "e"])
print(c)





