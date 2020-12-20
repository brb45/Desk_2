# iterator:
# output from zip, map, collections.Counter().elements(), iter(list), iter(set)

from collections import deque

dic = {'a': 1, "b":2, "c":3}
# for key in dic:
#     if key == "b":
#         dic.pop(key)
# RuntimeError: dictionary changed size during iteration

int_set = set([1,2,3,45,9])
for num in int_set:
    print(num, end=", ")
print()
# for num in int_set:
#     if num == 3:
#         int_set.remove(num)
# RuntimeError: Set changed size during iteration

nums = [1,2,3,4,5]
for num in nums:
    if num == 3:
        nums.pop(2) # pop(index)

print(nums) # [1, 2, 4, 5]

dq = deque([1,2,3,45,6])
for i in range(len(dq)):
    print(i, dq[i], end=", ") # 0 1, 1 2, 2 3, 3 45, 4 6,
print()
# for num in dq:
#     if num == 3:
#         dq.pop()
# RuntimeError: deque mutated during iteration
print(list(dq))
# The original dictionary is : {'Gfg': 1, 'is': 2, 'best': 3, 'for': 4, 'CS': 5}
# Dictionary after removal of keys : {'Gfg': 1, 'best': 3}