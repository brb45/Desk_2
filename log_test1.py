class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 11:31 4/28/21

        n = len(coins)
        coins.sort()

        dp = [-1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for j in range(n):
                if coins[j] <= i and dp[i - coins[j]] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[i - coins[j]] + 1
                    else:
                        dp[i] = min(dp[i - coins[j]] + 1, dp[i])

        return dp[amount]