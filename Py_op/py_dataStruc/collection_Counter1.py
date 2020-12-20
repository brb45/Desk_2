
#____________________________________________________________________________________
from collections import Counter
from collections import deque

dq = deque("thisisaqueue")
print(dq)
# deque(['t', 'h', 'i', 's', 'i', 's', 'a', 'q', 'u', 'e', 'u', 'e'])

cnter = Counter(dq)
print(cnter)
# Counter({'i': 2, 's': 2, 'u': 2, 'e': 2, 't': 1, 'h': 1, 'a': 1, 'q': 1})

# elements() --> iterable, Not a list
cnt_elements = cnter.elements()
print(cnt_elements)
# <itertools.chain object at 0x018806F0>
cnt_list = list(cnt_elements)
print(cnt_list)
# ['t', 'h', 'i', 'i', 's', 's', 'a', 'q', 'u', 'u', 'e', 'e']

# most_common(n)
# returns list of tuples of (key, cnt) in decreasing order of cnt
tuple_list = cnter.most_common()
print(tuple_list)
# [('i', 2), ('s', 2), ('u', 2), ('e', 2), ('t', 1), ('h', 1), ('a', 1), ('q', 1)]
tuple_list = cnter.most_common(2)
print(tuple_list)
# [('i', 2), ('s', 2)]

# update()
new_data = 'octupusisinjailornot'
cnter.update(new_data)
print(cnter.most_common())
# [('i', 5), ('s', 4), ('u', 4), ('t', 3), ('o', 3), ('a', 2), ('e', 2), ('n', 2), ('h', 1), ('q', 1), ('c', 1), ('p', 1), ('j', 1), ('l', 1), ('r', 1)]

# remove
cnter.pop('i')
print(cnter.most_common())
# [('s', 4), ('u', 4), ('t', 3), ('o', 3), ('a', 2), ('e', 2), ('n', 2), ('h', 1), ('q', 1), ('c', 1), ('p', 1), ('j', 1), ('l', 1), ('r', 1)]
del cnter['s']
print(cnter.most_common())
# [('u', 4), ('t', 3), ('o', 3), ('a', 2), ('e', 2), ('n', 2), ('h', 1), ('q', 1), ('c', 1), ('p', 1), ('j', 1), ('l', 1), ('r', 1)]