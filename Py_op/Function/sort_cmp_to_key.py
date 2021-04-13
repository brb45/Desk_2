import functools

def single_rising(x,y):
    if x < y: #
        return -1 # when return -1, put in x first, otherwise y first
    else:
        return 1

nums  = [ -1, 1 , 0, 3, 5, 9, 4]
nums.sort(key=functools.cmp_to_key(single_rising))
print(nums) # [-1, 0, 1, 3, 4, 5, 9]

def single_decrement(x,y):
    if x > y:
        return -1
    else:
        return 1

nums.sort(key=functools.cmp_to_key(single_decrement))
print(nums) # [9, 5, 4, 3, 1, 0, -1]

###
from functools import cmp_to_key
def largestNumber(nums):
    # 11:00 8/6/20
    # 9:32 4/7/21

    def sort_decrease(x, y):
        if x + y > y + x:
            return -1
        else:
            return 1
        # else:
        #     return 0

    nums_str = [str(num) for num in nums]
    nums_str.sort(key=cmp_to_key(sort_decrease))

    res = "-".join(nums_str)

    return res if res[0] != '0' else '0'

nums = ["93", "9", "873", "86", "50","45"]
print(largestNumber(nums)) # 9-93-873-86-50-45

def largestNumber1(nums):
    # 11:00 8/6/20
    # 9:32 4/7/21

    # def sort_decrease(x, y):
    #     if x + y > y + x:
    #         return -1
    #     else:
    #         return 1
    #     # else:
    #     #     return 0

    nums_str = [str(num) for num in nums]
    nums_str.sort(key=cmp_to_key(lambda x, y: -1 if x+y > y+x else 1))

    res = "-".join(nums_str)

    return res if res[0] != '0' else '0'

nums = ["93", "9", "873", "86", "50","45"]
print(largestNumber1(nums)) # 9-93-873-86-50-45

##
nums = [28, 50, 17, 12, 121]

nums.sort(key=cmp_to_key(lambda x, y: -1 if x > y else 1)) # Descending
print(nums)
# [121, 50, 28, 17, 12]
nums.sort(key=cmp_to_key(lambda x, y: -1 if x < y else 1)) # increasing
print(nums)
# [12, 17, 28, 50, 121]

##
