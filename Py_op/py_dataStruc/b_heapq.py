from random import randint
import heapq

# heap can only be created by a list or empty list; Not any other iterables
# nums = {1, 3, 5, 8, 0, 7, 100}
# heapq.heapify(nums) # TypeError: heap argument must be a list

# heapq is min heap by default;
# heapq by default: minimum heap, smallest value pops out first
# Create a max heap by negating your values when you store them in the heap

# heapq.heapify(arr)
# heapq.heappush(nums, 1000)
# top_val = heapq.heappop(nums)

# nlargest(k, iterable, key = fun)
# nsmallest(k, iterable, key = fun), return a list
# b_list = heapq.nsmallest(3, nums) # return a list

#---------------------------------------------------------------------------
# Build heapq from an empty list
arr = []
heapq.heapify(arr)

# Build heapq from a list
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
print(nums[-1]) # 1000
print(nums[1])  # 2

# remove the top elemet, which is smallest for min Heap, and return it
top_val = heapq.heappop(nums)
print(top_val)  # 1
print(nums)     # [2, 5, 3, 1000, 6, 8, 7]


# len
print(len(nums))  # 7
if nums:
    print(f"type of nums is {type(nums)}")
    # type of nums is <class 'list'>

#
b_list = heapq.nsmallest(3, nums) # return a list
print(b_list) # [2, 3, 5]
print(type(b_list)) # <class 'list'>


print(nums) # [2, 5, 3, 1000, 6, 8, 7]
a_list = heapq.nlargest(3, nums)
print(a_list) # [1000, 8, 7]
#----------------------------------------------------------
import heapq

arr = [(3,1,2), (4,2,2), (4,3,1), (4,1,3), (5, 2,3), (6, 5,1)]
heapq.heapify(arr)

b = heapq.nsmallest(4,arr)
print(b)
# [(3, 1, 2), (4, 1, 3), (4, 2, 2), (4, 3, 1)]
#----------------------------------------------------------
# heapq.merge(*iterables, key=None, reverse=False)
# Merge multiple sorted inputs into a single sorted output
# Returns an iterator over the sorted values.

# Create sorted sequences
sequence1 = [1, 2, 3]  # A list
sequence2 = (5, 7, 9)  # A tuple
sequence3 = [6, 8, 10]
import heapq
# Merge the sequences
merged = (heapq.merge(sequence1, sequence2, sequence3))
# type of merged is <class 'generator'>
merged = list(merged)
heapq.heappush(merged, 0) # merged needs to be a list
print((merged))
# [0, 1, 3, 5, 2, 7, 8, 9, 10, 6]

# Print the merged sequences
print(f"type of merged is {type(merged)}")

# push then pop
print(nums) # [3, 5, 7, 1000, 6, 8]
pop_val = heapq.heappushpop(nums, 999)
print(pop_val) # 3
print(nums) # [5, 6, 7, 1000, 999, 8]

# Push item on the heap, then pop and return the smallest item from the heap.
# The combined action runs more efficiently than heappush() followed by a separate call to heappop().

# pop then push
pop_val = heapq.heapreplace(nums, 555)
print(pop_val) # 5
print(nums) #  [6, 555, 7, 1000, 999, 8]

# Pop and return the smallest item from the heap,
# and also push the new item. The heap size doesn’t change.
# If the heap is empty, IndexError is raised.

# This one step operation is more efficient than a heappop() followed
# by heappush() and can be more appropriate when using a fixed-size heap.
# The pop/push combination always returns an element from the heap and replaces it with item