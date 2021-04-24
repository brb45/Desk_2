class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 11:14 4/23/21

        def b_search(nums, lt, rt, target):
            while lt <= rt:
                mid = lt + (rt - lt) // 2
                if nums[mid] > target:
                    rt = mid - 1
                elif nums[mid] < target:
                    lt = mid + 1
                else:
                    return mid
            return -1

        n = len(nums)
        lt, rt = 0, n - 1
        while lt <= rt:
            mid = lt + (rt - lt) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[rt]:
                if nums[mid] < target <= nums[rt]:
                    return b_search(nums, mid, rt, target)
                else:
                    rt = mid - 1
            else:
                if nums[lt] <= target < nums[mid]:
                    return b_search(nums, lt, mid - 1, target)
                else:
                    lt = mid + 1
        return -1