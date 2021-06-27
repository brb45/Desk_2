class Solution:
    def splitIntoFibonacci(self, S):
        # 5:33 4/22

        def splitArray(S, ind, ans, res):
            if ind == len(S) and len(ans) > 2:
                res += ans
                # res = ans
                return True
            for i in range(ind, len(S)):
                p = S[ind:i + 1]
                if int(p) > (1 << 31) - 1:
                    break
                elif len(p) > 1 and p[0] == "0":
                    break;
                if len(ans) >= 2:
                    if int(ans[-2]) + int(ans[-1]) > int(p):
                        continue
                    elif int(ans[-2]) + int(ans[-1]) < int(p):
                        break
                ans.append(p)
                if splitArray(S, i + 1, ans, res):
                    return True
                # if res:
                #     break
                ans.pop()
            return False

        res = []
        ans = []
        splitArray(S, 0, ans, res)
        return (ans, res)

S= "123456579"
(ans, res) = Solution().splitIntoFibonacci(S)
print(f"res is {res}")   # res is ['123', '456', '579']
print(f"ans is  {ans}")  # ans is  ['123', '456', '579']

###


class Solution:

    def __init__(self):
        pass

    def coinChange(self, coins: List[int], amount: int) -> int:
        # 11:31 4/28/21
        # 3:12 6/25/21
        # DFS

        def helper(coins, i, cnt, amount):  # coins, i=0, cnt = [0], amount
            if amount == 0:
                return True
            for i, v in enumerate(coins):
                if amount - v >= 0:
                    cnt[0] += 1
                    # if helper(coins[i:], 0, cnt, amount-v ):
                    if helper(coins, 0, cnt, amount - v):
                        return True
                    cnt[0] -= 1
                # else:
                #     break
            return False

        coins.sort(reverse=True)
        cnt = [0]
        if helper(coins, 0, cnt, amount):
            return cnt[0]
        return -1

