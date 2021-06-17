# In an OrderedDict, the order the items are inserted is remembered and used when creating an iterator.
# OrderedDict only keeps track of insertion order; It does NOT sort the keys in order
###
from collections import OrderedDict
# You can create an ordered dictionary by passing keyword arguments to the class constructor:
numbers = OrderedDict(one=1, two=2, three=3)

dic = OrderedDict([('a', 1), ('h', 2), ('b', 3), ('f', 100)])
print(dic)
# OrderedDict([('a', 1), ('h', 2), ('b', 3), ('f', 100)])

dic = OrderedDict({'a':1, 'b': 2})
print(dic)
OrderedDict([('a', 1), ('b', 2)])

k = ['a', 'b', 'c']
v = [1, 2, 3]

pre_dic = zip(k,v)
dic = OrderedDict(pre_dic)
print(dic)
OrderedDict([('a', 1), ('b', 2), ('c', 3)])

pre_dic = zip(k,v)
dic = dict(pre_dic)
print(dic)
{'a': 1, 'b': 2, 'c': 3}

# Finally, OrderedDict also provides .fromkeys(), which creates a new dictionary
# from an iterable of keys and sets all its values to a common value:

# fromkeys()
keys = ["one", "two", "three"]
dic = OrderedDict.fromkeys(keys, 0)
print(dic)
# OrderedDict([('one', 0), ('two', 0), ('three', 0)])

###
# If you delete an item from an existing ordered dictionary and insert that same item again,
# then the new instance of the item is placed at the end of the dictionary:

# If you update the value of an existing key-value pair in an OrderedDict object,
# the key maintains its position but gets a new value:

# Another important feature that OrderedDict has provided since Python 3.5 is that its items, keys,
# and values support reverse iteration using reversed().
# This feature was added to regular dictionaries in Python 3.8.
# reversed()

for key in reversed(dic):
    print(key)
# three
# two
# one

# .move_to_end()
# move an existing item either to the end or to the beginning of the dictionary.
# last holds a Boolean value that defines to which end of the dictionary you want to move the item at hand.

# last defaults to True, which means that the item will be moved to the end, or right side, of the dictionary.
# False means that the item will be moved to the front, or left side, of the ordered dictionary
print(dic)
# OrderedDict([('one', 0), ('two', 0), ('three', 0)])
dic.move_to_end('two')
print(dic)
# OrderedDict([('one', 0), ('three', 0), ('two', 0)])

dic.move_to_end('two', last=False) # move key='two' to the front
print(dic)
# OrderedDict([('two', 0), ('one', 0), ('three', 0)])


# .popitem()
# is an enhanced variation of its dict.popitem() counterpart that
# allows you to remove and return an item from either the end or the beginning of the underlying ordered dictionary.
# By default, it removes the last one
# In OrderedDict, however, .popitem() also accepts a Boolean argument called last, which defaults to True.
# If you set last to False, then .popitem() removes the items from the beginning of the dictionary.

print(dic)
# OrderedDict([('two', 0), ('one', 0), ('three', 0)])
remove = dic.popitem()
print(dic) # OrderedDict([('two', 0), ('one', 0)])
print(remove)
# ('three', 0)

remove = dic.popitem(last=False)
print(remove) # ('two', 0)
print(dic) #  OrderedDict([('one', 0)])

