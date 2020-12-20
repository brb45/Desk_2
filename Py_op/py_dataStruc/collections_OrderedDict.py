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
