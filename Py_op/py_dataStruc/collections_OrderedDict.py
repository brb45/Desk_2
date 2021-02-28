# In an OrderedDict, the order the items are inserted is remembered and used when creating an iterator.
# OrderedDict only keeps track of insertion order; It does NOT sort the keys in order
from collections import OrderedDict
dic = OrderedDict([('d',50), ('e',30), ('c',40)])
print(list(dic.items()))
# tmp = dic.popitem()
# print(type(tmp))
# print(tmp, tmp[0],tmp[1])

for key in dic:
    print(key)

    # [('d', 50), ('e', 30), ('c', 40)]
    # d
    # e
    # c

dic['g'] =100
dic['a'] = 200

print(str(dic))
# OrderedDict([('d', 50), ('e', 30), ('c', 40), ('g', 100), ('a', 200)])

###
from collections import OrderedDict

dic = OrderedDict([('a', 1), ('h', 2), ('b', 3), ('f', 100)])

print(dic)
# OrderedDict([('a', 1), ('h', 2), ('b', 3), ('f', 100)])

dic.popitem()
# OrderedDict([('a', 1), ('h', 2), ('b', 3)])
print(dic)

a = dic.popitem(last=False)
# OrderedDict([('h', 2), ('b', 3)])
print(dic)


print(type(a))
# <class 'tuple'>
print(a)
# ('a', 1)

###