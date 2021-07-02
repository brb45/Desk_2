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
print("************************************************")
###

 








