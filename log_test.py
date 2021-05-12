class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # 5:33 --> 5:37 -->  3/3/21 Num of longest increasing subsequence

        n = len(nums)
        if n < 1:
            return 0
        dp = [[1, 1] for i in range(len(nums))]

        max_len = 0
        max_cnt = 0



        for i in range(n):
            max_len1 = dp[i][0]
            for j in range(i):
                if nums[j] < nums[i]:
                    # max_len = dp[i][0]
                    if dp[j][0] + 1 > max_len1:
                        max_len1 = dp[j][0] + 1
                        dp[i][0], dp[i][1] = max_len1, dp[j][1]
                    elif dp[j][0] + 1 == max_len1:
                        dp[i][1] += dp[j][1]

            if max_len == dp[i][0]:
                max_cnt += dp[i][1]
            if max_len < dp[i][0]:
                max_len = dp[i][0]
                max_cnt = dp[i][1]

        return max_cnt