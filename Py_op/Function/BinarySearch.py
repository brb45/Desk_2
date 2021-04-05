# Binary Search

# 第一类： 需查找和目标值完全相等的数
# type 1: look for the target in an array

nums = [-1,0,3,5,9,12]
target = 9
n = len(nums)

def b_search(nums, st, end, target): # 0, n
    while st < end:
        mid = (st + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid
        else:
            st = mid + 1
    return -1

print(b_search(nums, 0, n, target))

# class Solution {
# public:
#     int search(vector<int>& nums, int target) {
#         int left = 0, right = nums.size();
#         while (left < right) {
#             int mid = left + (right - left) / 2;
#             if (nums[mid] == target) return mid;
#             else if (nums[mid] < target) left = mid + 1;
#             else right = mid;
#         }
#         return -1;
#     }
# };
def b_search1(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right-left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return -1

print(b_search1(nums, target))

# Type 2
# 第二类： 查找第一个 >= 目标值的数
# int find(vector<int>& nums, int target) {
#     int left = 0, right = nums.size();
#     while (left < right) {
#         int mid = left + (right - left) / 2;
#         if (nums[mid] < target) left = mid + 1;
#         else right = mid;
#     }
#     return right;
# }

def b_search2(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return right
print(len(nums))
res = b_search2(nums, 12)
if res == len(nums):
    print("NOT FOUND")
else:
    print(res)

# Type 3
# 第三类： 查找第一个大于目标值的数
# int find(vector<int>& nums, int target) {
#     int left = 0, right = nums.size();
#     while (left < right) {
#         int mid = left + (right - left) / 2;
#         if (nums[mid] <= target) left = mid + 1;
#         else right = mid;
#     }
#     return right;
# }
def b_search3(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return right

# Type 4
# 第四类： 查找最后一个<= 目标值
def b_search4(nums, target):
    lt, rt = 0, len(nums)
    while lt < rt:
        mid = lt + (rt - lt) // 2
        if nums[mid] > target:
            rt = mid
        else:
            lt = mid + 1
    return lt - 1





