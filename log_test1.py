
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 7/4/2020

        n = len(nums)
        lt, rt = 0, n- 1
        while lt <= rt:
            mid = lt + (rt - lt) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[rt]:
                if nums[mid] < target <= nums[rt]:
                    lt = mid + 1
                else:
                    rt = mid - 1
            elif nums[mid] >= nums[rt]:
                if nums[lt] <= target < nums[mid]:
                    rt = mid - 1
                else:
                    lt = mid + 1

        return -1