# 12/12/20
# 12/14/20
# 12/21/20
from collections import deque

dq = deque()
dq.append(100)
dq.appendleft(200)

for i in range(len(dq)):
    print(dq[i])
# 200
# 100
print(dq.count(100), dq.count(1000)) # 1 0

dq.pop()
dq.append(99)
dq.popleft()
print(dq) # deque([99])

dq.extend("abcd")
dq.extendleft("ABCD")
print(dq) # deque(['D', 'C', 'B', 'A', 99, 'a', 'b', 'c', 'd'])

start, end = 0, 4
loc = dq.index("B", start, end)
print(loc) # 2

val_add = 888
insert_loc = 1
dq.insert(insert_loc, val_add)
print(dq)
# deque(['D', 888, 'C', 'B', 'A', 99, 'a', 'b', 'c', 'd'])

val_remove = 888
dq.remove(val_remove)
print(dq)
# deque(['D', 'C', 'B', 'A', 99, 'a', 'b', 'c', 'd'])

del dq[0]
print(dq)
# deque(['C', 'B', 'A', 99, 'a', 'b', 'c', 'd'])

dq.reverse()
print(dq)
# deque(['d', 'c', 'b', 'a', 99, 'A', 'B', 'C'])

n = 2
dq.rotate(n)
print(dq)
# deque(['B', 'C', 'd', 'c', 'b', 'a', 99, 'A'])

n = -2
dq.rotate(n)
print(dq)
# deque(['d', 'c', 'b', 'a', 99, 'A', 'B', 'C'])

# with maxlen
# dq(iterable, maxlen=4)
dq = deque("abcdefg", maxlen=4)
print(dq)
# deque(['d', 'e', 'f', 'g'], maxlen=4)
dq.append(100)
print(dq)
# deque(['e', 'f', 'g', 100], maxlen=4)
dq.appendleft(99)
print(dq)
# deque([99, 'e', 'f', 'g'], maxlen=4)

from collections import deque as dq
d = dq(maxlen=4)
print(d)
# deque([], maxlen=4)

d.insert(0, 1)
d.insert(0, 2)
d.insert(1,3)
d.insert(2,4)
print(d)
# deque([2, 3, 4, 1], maxlen=4)


# d.insert(3,5)
# print(d)
# insert gives an error, if maxlen is reached.
# IndexError: deque already at its maximum size
# deque([], maxlen=4)

d.append(100)
print(d)
# deque([3, 4, 1, 100], maxlen=4)

d.appendleft(99)
print(d)
# deque([99, 3, 4, 1], maxlen=4)


