import heapq
from random import randint

# heap can only be created by a list or empty list; Not any other iterables

# nums = {1, 3, 5, 8, 0, 7, 100}
# heapq.heapify(nums) # TypeError: heap argument must be a list

# Build heapq from an empty list
arr = []
heapq.heapify(arr)

# Build heapq from a list
import heapq
nums = [3, 5, 1, 2, 6, 8, 7]
# heapq by default: minimum heap, smallest value pops out first
heapq.heapify(nums)
# nums becomes a heap
print(nums) # [1, 2, 3, 5, 6, 8, 7]

# add an elemet: heappush
heapq.heappush(nums, 1000)
print(nums) # [1, 2, 3, 5, 6, 8, 7, 1000]

# show the top element
print(nums[0])  # 1

# remove the top elemet, and return it
top_val = heapq.heappop(nums)
print(top_val)  # 1
print(nums)     # [2, 5, 3, 1000, 6, 8, 7]

# len
print(len(nums))  # 7
if nums:
    print(f"type of nums is {type(nums)}") # type of nums is <class 'list'>

# nlargest(k, iterable, key = fun)
# nsmallest(k, iterable, key = fun), return a list

k_small = heapq.nsmallest(3, nums) #
print(k_small, '\n', type(k_small))
# [2, 3, 5]
#  <class 'list'>

k_large = heapq.nlargest(3, nums)
print(k_large) # [1000, 8, 7]

# heapq.merge(*iterables, key=None, reverse=False)
# Merge multiple sorted inputs into a single sorted output
# Returns an iterator over the sorted values.

import heapq

# Create sorted sequences

sequence1 = [1, 2, 3]  # A list
sequence2 = (5, 7, 9)  # A tuple
sequence3 = [6, 8, 10]

# Merge the sequences
merged = heapq.merge(sequence1, sequence2, sequence3)
# Print the merged sequences
print(f"type of merged is {type(merged)}")
# type of merged is <class 'generator'>
# print(list(merged)) # [1, 2, 3, 5, 6, 7, 8, 9, 10]
for i in merged:
    print(i, end=", ")
# 1, 2, 3, 5, 6, 7, 8, 9, 10,








