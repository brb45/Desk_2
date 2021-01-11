import heapq

arr = []

hq = heapq.heapify(arr)
print(hq) # None
print(type(hq)) # <class 'NoneType'>
print(arr) # []
print(type(arr)) # <class 'list'>

nums = [3, 5, 1, 2, 6, 8, 7]
# heapq by default: minimum heap, smallest value pops out first
heapq.heapify(nums)
# nums becomes a heap
print(nums) # [1, 2, 3, 5, 6, 8, 7]
print(type(nums)) # <class 'list'>

# add an elemet: heappush
heapq.heappush(nums, 1000)
print(nums) # [1, 2, 3, 5, 6, 8, 7, 1000]

# show the top element
print(nums[0])  # 1
print(nums[-1]) # 1000
print(nums[1])  # 2

top_val = heapq.heappop(nums)
print(top_val)  # 1
print(nums)     # [2, 5, 3, 1000, 6, 8, 7]

b_list = heapq.nsmallest(3, nums)
print(b_list) # [2, 3, 5]
print(type(b_list)) # <class 'list'>

print(nums) # [2, 5, 3, 1000, 6, 8, 7]
a_list = heapq.nlargest(3, nums)
print(a_list) # [1000, 8, 7]

print("ex 2")
brr = []
to_insert = [(1,'b'), (1,'c'), (1,'d'), (1,'a'), (2,'a')]
for val in to_insert:
    heapq.heappush(brr, val)
while brr:
    print(heapq.heappop(brr))
# (1, 'a')
# (1, 'b')
# (1, 'c')
# (1, 'd')
# (2, 'a')

