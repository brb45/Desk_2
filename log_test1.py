def findNumberOfLIS(nums):
    # 10:43 --> 11:00 -->  11;16  9/1/20 Num of longest increasing subsequence

    dp = [[1, 1] for i in range(len(nums))]
    max_for_all = 0
    maxlen = 0
    for i, num in enumerate(nums):
        max_len, count = 1, 0
        for j in range(i):
            if nums[j] < num:
                if dp[j][0] + 1 > max_len:
                    max_len = dp[j][0] + 1
                    count = 0
                if dp[j][0] + 1 == max_len:
                    count += dp[j][1]
        dp[i] = [max_len, max(count, dp[i][1])]

        if max_for_all == dp[i][0]:
            maxlen += dp[i][1]
        if max_for_all < dp[i][0]:
            max_for_all = dp[i][0]
            maxlen = dp[i][1]
    return maxlen

nums = [2,2,2,2,2]

print(findNumberOfLIS(nums))

# def findNumberOfLIS(self, nums: List[int]) -> int:
#     # 10:43 --> 11:00 -->  11;16  9/1/20 Num of longest increasing subsequence
#
#     dp = [[1, 1] for i in range(len(nums))]
#     max_for_all = 1
#     cnt_max = 1
#     for i, num in enumerate(nums):
#         # max_len, count = 1, 0
#         for j in range(i):
#             if nums[j] < num:
#                 new_len = dp[j][0] + 1
#                 if new_len > dp[i][0]:
#                     dp[i][0] = new_len
#                     dp[i][1] = dp[j][1]
#                 elif new_len == dp[i][0]:
#                     dp[i][1] += 1
#
#             if dp[i][0] > max_for_all:
#                 max_for_all = dp[i][0]
#                 cnt_max = dp[i][1]
#             elif dp[i][0] == max_for_all:
#                 cnt_max += 1
#
#     return cnt_max