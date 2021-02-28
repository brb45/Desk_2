# In an OrderedDict, the order the items are inserted is remembered and used when creating an iterator.
# OrderedDict only keeps track of insertion order; It does NOT sort the keys in order
from collections import OrderedDict
dic = OrderedDict([('d',50), ('e',30), ('c',40), ('h', 100), ('k', 50)])

print(list(dic.items()))
# [('d', 50), ('e', 30), ('c', 40), ('h', 100), ('k', 50)]

# popitem(last=True)
# The popitem() method for ordered dictionaries returns and removes a (key, value) pair.
# The pairs are returned in LIFO order if last is true or FIFO order if false.

pop_last_item = dic.popitem()
print(list(dic.items()))
# [('d', 50), ('e', 30), ('c', 40), ('h', 100)]
print(pop_last_item)
# ('k', 50)

pop_first_item = dic.popitem(last=False)
print(pop_first_item)
# ('d', 50)
print(list(dic.items()))
# [('e', 30), ('c', 40), ('h', 100)]


for key in dic:
    print(key)
    # e
    # c
    # h

# move_to_end(key, last=True)
# Move an existing key to either end of an ordered dictionary.
# The item is moved to the right end if last is true (the default) or to the beginning
# if last is false. Raises KeyError if the key does not exist:

