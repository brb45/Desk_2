def maxNonOverlapping(self, nums: List[int], target: int) -> int:

    n = len(nums)
    sums = [0]*n
    res = [0] * n
    max_len = 0
    dic = {}

    for i in range(n):
        sums[i] = sums[i-1] + nums[i] if i > 0 else nums[i]

    for i, v in enumerate(nums):
        val = v - target
        if val in dic:
            res[i] = res[dic[val]] + 1
        elif val == 0:
            res[i] = 1

        dic[v] = i
        if i > 0:
            res[i] = max(res[i], res[i-1])

    return max(res)







