dic = {}
a = {'a': 100}
b = {'b': 200}

dic.update(a, b)
print(dic)
#     dic.update(a, b)
# TypeError: update expected at most 1 arguments, got 2

# dictionary not sorted by default

cnt_dict = {'a':4, 'b':8, 'c':10, 'd':4, 'e':10, 'f':5, 'h':5, 'g':5}
len(cnt_dict)  # 8

chr_key = cnt_dict.keys()
print(f"{type(chr_key)}") # <class 'dict_keys'>
print(list(chr_key)) # ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'g']

num_values = cnt_dict.values()
# print(list(num_values)) [4, 8, 10, 4, 10, 5, 5, 5]
# type(num_values) is # <class 'dict_values'>

item_tuple = cnt_dict.items()
# print(list(item_tuple)) [('a', 4), ('b', 8), ('c', 10), ('d', 4), ('e', 10), ('f', 5), ('h', 5), ('g', 5)]
# type(item_tuple) is <class 'dict_items'>

# create a dict
# 1. a list of tuples
my_dic = dict([("ID", 1),("Test", "wifi")])
#print(my_dic.get("Test")) # "wifi" , "return None if key is wrong"

#Some tuples can be used as dictionary keys (specifically, tuples that contain immutable values
#like strings, numbers, and other tuples). Lists can never be used as dictionary keys,
#because lists are not immutable

#Tuples can be used as values in sets whereas lists can not
wi = {"mimo", "rsdb",("a","b"),["c","d"]} #TypeError: unhashable type: 'list'

#Iterate over keys

#Iterate over (key, value) tuples
for key, value in my_dictionary.items(): #key, value is just variables
for a, b in my_dictionary.items() # same results, a is key, b is its corresponding value

# Iterate over values
for value in my_dic.values():

# Iterate over keys
for key in my_dic:

# Check for existence
haystack = {}
# ...
if 'needle' in haystack:

b = d.items()
print("type b is {}".format(b))  # dict_items
# ([('MPS', 0), ('MPS_AC', 1), ('11AX', 2)])
# c = b[0] #TypeError: 'dict_items' object does not support indexing
# print("type c is {}".format(c))

#######################################################################

# size of the dict
len(test)

# Add or modify a key
test["MIMO"] = 10

#remove, pop("MIMO") returns the value
test.pop("MIMO")

# rmv last item
test.popitem()

# Update Dict
test.update({"MU-MIMO": 6})

#
test = dict([('wifi', 2),("bt",3),('AC',4)])
print(test)
# {'wifi': 2, 'bt': 3, 'AC': 4}
test_1 = [("mu",5),("wifi",6),("su", 7)]
test.update(test_1) # list of tuple

print(test)
# {'wifi': 6, 'bt': 3, 'AC': 4, 'mu': 5, 'su': 7}

# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
mumu = dict(('mumu','TXTX')) #wrong

# test_list.update(('new_item', 100)) ValueError: dictionary update sequence element #0 has length 8; 2 is required
test_list.update([('new_item', 100)])

#
del test["MIMO"]
test.clear() # empty dic
#
ss = {'a':1, 'b':4, 'c':9}
# this only iterates through keys.
for i,s in enumerate(ss):
    print(i,s)
# 0 a
# 1 b
# 2 c

# get() returns None if key non-existent
# returns value if key found
ss = {'a':1, 'b':4, 'c':9}
print(ss.get('a')) # 1
print(ss.get('g')) # None
print(ss.get('g', "Not Found")) # Not Found

test_list = {1:["wifi","ax"]}
for key, value in test_list.items():
    print(key, value)
# 1 ['wifi', 'ax']

# important
dic = {"a" : {1,2,3}}
set_2 = dic["a"]

set_2.add(5)
set_2.update([6,7,9])
print(dic['a'])
print(set_2)
# {1, 2, 3, 5, 6, 7, 9}
# {1, 2, 3, 5, 6, 7, 9}

dic = {"a" : [1,2,3]}
set_2 = dic["a"]

set_2.append(10)
set_2.append(11)
print(dic['a'])
# [1, 2, 3, 10, 11]
print(set_2)
# [1, 2, 3, 10, 11]

#
dic = {"a" : [1,2,3]}
set_2 = dic["a"]

def pass_fun(set_2):
    set_2.append(10)
    set_2.append(11)

pass_fun(set_2)
print(set_2)
# [1, 2, 3, 10, 11]
print(dic['a'])
# [1, 2, 3, 10, 11]


dic = {"a" : [1,2,3]}
set_2 = dic["a"]

def pass_fun(set_2):
    set_2.append(10)
    set_2.append(11)


pass_fun(dic['a'][:])
print(dic['a'])
# [1, 2, 3]


##
from collections import Counter
dic = {}
dic1 = Counter()

nums = [('a', 11), ('b', 200)]
nums1 = ['a' , 'b', 'c']
dic1.update(nums1)
print(dic)
s = str(dic)
print(len(str(dic)))

# for i, v in enumerate(s):
#     print(i,f'[{v}]')
print(dic1)
dic1.update(('a', 10))
print(dic1)
# Counter({'a': 1, 'b': 1, 'c': 1})
# Counter({'a': 2, 'b': 1, 'c': 1, 10: 1})
