from collections import defaultdict, deque


# x = defaultdict(lambda: defaultdict(dict))
xx = defaultdict(lambda: list)
xxx = defaultdict(list)
xxxx = defaultdict(dict)
yy   = defaultdict(set)
zz   = defaultdict(deque)
print(xx[0]) # <class 'list'>
print(xxx[0]) # []
print(xxxx[0]) # {}
print(yy[0]) # set()
print(zz[0]) # deque([])


# dic3 = defaultdict(defaultdict(list))
# TypeError: first argument must be callable or None

dic3 = defaultdict(lambda: defaultdict(list))

s = "avcdladjlajfdlajadlsjfdalf"
for ss in s:
    dic3[ss][ss].append("True")

print(str(dic3))

# ex 1: default value is int 99
cnt = defaultdict(lambda: 99)
print(len(cnt)) # 0
for i in range(5):
    if i < 4:
        print(cnt[i], end=', ')
    elif i == 4:
        print(cnt[i])
# 99, 99, 99, 99, 99
print(len(cnt)) # 5
print(list(cnt.keys()))
# [0, 1, 2, 3, 4]

# ex 2, default value is empty string
cnt = defaultdict(lambda: "")
cnt['a'] += 'a'
print(cnt['a']) # a
#

# y = defaultdict(lambda: defaultdict(lambda: 0))
#
# # I think the first line means that when I call x[k] for
# a nonexistent key k (such as a statement like v=x[k]),
# the key-value pair (k,0) will be automatically added to
# the dictionary, as if the statement x[k]=0 is first executed.

# # That's right. This is more idiomatically written
# #
# # x = defaultdict(int)
# # In the case of y, when you do y["ham"]["spam"],
# the key "ham" is inserted in y if it does not exist.
#
# The value associated with it becomes a defaultdict in which "spam" is automatically inserted with a value of 0.
# # I.e., y is a kind of "two-tiered" defaultdict. If "ham" not in y, then evaluating y["ham"]["spam"] is like doing
# #
# # y["ham"] = {}
# # y["ham"]["spam"] = 0
# # in terms of ordinary dict.
#
# #
# cnt = defaultdict(lambda: [1])
# cnt['a'] += [100]
# print(cnt['a']) # [1, 100]
#

from functools import cmp_to_key

arr = [1,3 ,7,9, 3,5]

arr.sort(key= cmp_to_key(lambda x, y: -1 if x < y else 1))  # ascending

print(arr) # [1, 3, 3, 5, 7, 9]

arr.sort(key = cmp_to_key(lambda x, y: -1 if x > y else 1)) # Descending
print(arr) # [9, 7, 5, 3, 3, 1]

# from functools import cmp_to_key
# nums = [28, 50, 17, 12, 121]
# # nums.sort(key=cmp_to_key(lambda x, y: 1 if x < y else -1)) # Descending
# # print(nums)

# # # [121, 50, 28, 17, 12]
# # nums.sort(key=cmp_to_key(lambda x, y: -1 if x < y else 1)) # increasing
# # print(nums)
# # # [12, 17, 28, 50, 121]
# #
# #
# # from functools import cmp_to_key
# # nums.sort(key = cmp_to_key(lambda x, y: -1 if x < y else 1 ))
# # print(nums)
#
from collections import defaultdict, OrderedDict, Counter
cnt = defaultdict(lambda: [1])
cnt['a'] += [100]
print(cnt['a']) # [1, 100]
#
# dic = {"a":100, "b":200, "c":300}
# # set_a = {100,200,300}
# # print(dic)
# # print(set_a)
{'a': 100, 'b': 200, 'c': 300}
{200, 100, 300}

#
# y = defaultdict(lambda: defaultdict(lambda: 0))
# # print(y['k1']['k2'] )  # 0
# # print((y['k1']) )  # {'k2': 0}
# # print(y)
#
# x = defaultdict(lambda: defaultdict(dict))
xx = defaultdict(lambda: list)
xxx = defaultdict(list)
xxxx = defaultdict(dict)
yy   = defaultdict(set)
zz   = defaultdict(deque)
print(xx[0]) # <class 'list'>
print(xxx[0]) # []
print(xxxx[0]) # {}
print(yy[0]) # set()
print(zz[0]) # deque([])

#
foo = lambda: 100
print(foo()) # 100
#
goo = lambda: list
print(goo) # <function <lambda> at 0x036196F0>
print(goo()) # <class 'list'>
print(goo()()) # []
#
# ##
d = defaultdict(int)
# d['one']
# 0
d = defaultdict(list)
# d['one']
# []
d = defaultdict(lambda: None)
# d['one'] is None
# True
# # As you can see, using a default dict will give every key you try to access a default value.
# # That default value is taken by calling the function you pass to the constructor.
# # So passing int will set int() as the default value (which is 0);
# # passing list will set list() as the default value (which is an empty list []);
# # and passing lambda: None will set (lambda: None)() as the default value (which is None).