from bisect import bisect_left, bisect,  bisect_right, insort, insort_left, insort_right
# import bisect
# bisect work on sorted list

# 1.
# bisect (nums, x[, lo[, hi]])
# return index of x in nums with optional range [lo, hi)

nums=[33,36,40,43,44,48,50]
x = 42
print(bisect(nums, x))  # 3

nums=[33,36,40,42,44,48,50]
x = 42
# if x exists, return the index after x
print(bisect(nums, x))  # 4

nums=[33,36,40,42, 42, 44,48,50]
x = 42
# if x exists, return the index after x
print(bisect(nums, x))  # 5

## 2.
# bisect_right(nums, x[, lo[, hi]])
# same as bisect

## 3.
# bisect_left(nums, x[, lo[, hi]])
# return index of x in nums with optional range [lo, hi)
# if x exists, return the index before x

nums=[33,36,40,43,44,48,50]
x = 42
print(bisect_left(nums, x))  # 3

nums=[33,36,40,42,44,48,50]
x = 42
# if x exists, return the index after x
print(bisect_left(nums, x))  # 3

nums=[33,36,40,42, 42, 44,48,50]
x = 42
# if x exists, return the index after x
print(bisect_left(nums, x))  # 3

## insort(nums,x) # insert before
nums=[33,36,40,43,44,48,50]
x = 42

insort(nums, x)
print(nums)
# [33, 36, 40, 42, 43, 44, 48, 50]

##
nums=[33,36,40,43,44,48,50]
x = 42

insort_right(nums, x)
print(nums)
# [33, 36, 40, 42, 43, 44, 48, 50]

##
nums=[33,36,40,43,44,48,50]
x = 42

insort_left(nums, x)
print(nums)
# [33, 36, 40, 42, 43, 44, 48, 50]