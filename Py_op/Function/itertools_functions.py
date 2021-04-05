from itertools import accumulate

# accumulate
nums = [1,2,3,4,5,6]
pre_sum = list(accumulate(nums))
print(pre_sum)
# [1, 3, 6, 10, 15, 21]
