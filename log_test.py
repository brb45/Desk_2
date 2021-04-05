class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # 4:14, 4/4/21

        n = len(nums)
        min_v = nums[0]

        for i in range(n):
            if nums[i] == min_v:
                continue
            elif nums[i] < min_v:
                min_v = nums[i]
                continue
            else:  # nums[i] > min_v
                for j in range(i + 1, n):
                    if min_v < nums[j] < nums[i]:
                        return True
        return False