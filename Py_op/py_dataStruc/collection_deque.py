# 12/12/20
# 2/23/21, 6/4/21, 6/16/21
from collections import deque

# 1. input : iterable or empty deque
dq = deque("iterable")
dq = deque()

# newdq = deque(100) TypeError: 'int' object is not iterable
dq = deque([200])
print(dq[0], dq[-1]) # 200 200

# 2. basic functions
s = "a"
dq.append(s)
dq.appendleft(s)

dq.pop()
dq.popleft()

dq.clear() # remove all elements

dq.count(s)
# return # of s , 0 is there is no s.

## dq.extend("iterable")
dq.extend("abcd")
print(dq) # deque([200, 'a', 'b', 'c', 'd'])

dq.extendleft("1234")
print(dq) #   deque(['4', '3', '2', '1', 200, 'a', 'b', 'c', 'd'])

dq_new = dq.copy()
# Create a shallow copy of the deque.
print(dq_new) # deque(['4', '3', '2', '1', 200, 'a', 'b', 'c', 'd'])


# index(x, start, end); seearch x in [start, end)
# Return the position of x in the deque (at or after index start and before index stop).
# Returns the first match or raises ValueError if not found.
loc_3 = dq.index(3, 0, -1)
print(loc_3)

# loc_d = dq.index('d', 0, -1)
# ValueError: 'd' is not in deque

loc_d = dq.index('d', 0)
print(loc_d) # 8

#
from collections import deque
dq = deque([1,2,3,4,5])
dq_cpy = dq.copy()
print(dq_cpy)
dq_deepCopy = copy.deepcopy(dq)
print(dq_deepCopy)
# deque([1, 2, 3, 4, 5])
# deque([1, 2, 3, 4, 5])

for i in range(len(dq)):
    print(dq[i], end=', ')
print()

#
# insert(i, x)
# Insert x into the deque at position i.
# If the insertion would cause a bounded deque to grow beyond maxlen, an IndexError is raise
dq.insert(1,100)
for i in range(len(dq)):
    print(dq[i], end=', ')
# 1, 100, 2, 3, 4, 5,
print()
#
# remove(value)
# Remove the first occurrence of value. If not found, raises a ValueError.
#
dq.remove(100)
for i in range(len(dq)):
    print(dq[i], end=', ')
# 1, 2, 3, 4, 5,
print()

# del dq[index]
del dq[1]
print(dq)
del dq[1]
print(dq)
# deque(['4', '2', '1', 200, 'a', 'b', 'c', 'd'])

##
reverse()
# Reverse the elements of the deque in-place and then return None.

##
rotate(n=1)
# Rotate the deque n steps to the right. If n is negative, rotate to the left.

# deque(['4', '2', '1', 200, 'a', 'b', 'c', 'd'])
dq.rotate(2)
print(dq)
# deque(['c', 'd', '4', '2', '1', 200, 'a', 'b'])

dq.rotate(-2)
print(dq)
deque(['4', '2', '1', 200, 'a', 'b', 'c', 'd'])

# access to the first and last element
dq[0]
dq[-1]



# iterate through dq
for i in range(len(dq)):
    print(dq[i], end=", ")
# c, d, 4, 2, 1, 200, a, b,

# with maxlen
# dq(iterable, max_len=4)
dq = deque("abcdefg", 4)
print(dq)
# deque(['d', 'e', 'f', 'g'], maxlen=4)
dq.append(100)
print(dq)
# deque(['e', 'f', 'g', 100], maxlen=4)
dq.appendleft(99)
print(dq)
deque([99, 'e', 'f', 'g'], maxlen=4)

dq = deque(maxlen=4)
print(dq)
deque([], maxlen=4)
dq.append(100)
print(dq)
deque([100], maxlen=4)
dq.appendleft(99)
print(dq)
deque([99, 100], maxlen=4)






#### deque
from collections import deque
# deque take a list as argument
list = ["wifi","bt","ax", "ac",'ac', 'ac']
deq = deque(list)
# add to the tail
deq.append("abgn")
# add to head
deq.appendleft("brcm")
# print(f"type(deq) is {type(deq)},  deq is {deq}")
# type(deq) is <class 'collections.deque'>,
# deq is deque(['brcm', 'wifi', 'bt', 'ax', 'ac', 'ac', 'ac', 'abgn'])

# remove from the end
print("deq.pop() ", deq.pop()) # deq.pop()  abgn
print(deq) #deque(['brcm', 'wifi', 'bt', 'ax', 'ac', 'ac', 'ac'])
# remove from the beginning
deq.popleft()
print(deq) # deque(['wifi', 'bt', 'ax', 'ac', 'ac', 'ac'])
#
# deq.clear()
# count()
print(deq.count('ac')) # 3

#access deque
for i in range(4):
    print(deq[i], end=", ")
print() # wifi, bt, ax, ac,


# deq[0] beginning item, deq[-1] ending item
print("deq[-1] ", deq[-1]) # ac

# time.sleep(1000)

d = deque('12345')
# print(type(d[0]), d[0], d[1], sep=", ") # <class 'str'>, 1, 2

# d = deque(maxlen=30)
# d = deque([1,2,3,4,5])
# d.extendleft([0])   deque([0, '1', '2', '3', '4', '5'])
# print(d)
d.extend([6,7,8])
# print(d) # deque(['1', '2', '3', '4', '5', 6, 7, 8])

# class collections.deque([iterable[, maxlen]])
#
# Returns a new deque object initialized left-to-right (using append())
# with data from iterable. If iterable is not specified, the new deque is empty.
#
# In your example , buff = collections.deque([], 100),
#
# creates a new empty deque object buff, specified by the first argument, with maxlen 100.
# It means the deque object is bounded to a maximum length of 100.