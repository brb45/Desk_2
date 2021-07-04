6/29/21
def int_to_binary_str(num):
    res = ""
    while num > 0:
        res = str(num % 2) + res
        num //= 2

    if len(res) < 8:
        to_add = '0' * (8 - len(res))
        res = to_add + res

    elif len(res) > 8:
        res = res[len(res) - 8:]
    return res

num = 145
print(int_to_binary_str(num))

bin_rep = format(num, '#010b')[-8:]
print(bin_rep)


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # 8:49 9/26/20; 7/3/21 --> 12:28

        def b_search1(d_p, target):
            if target < d_p[0][0]:
                return 0
            elif target >= d_p[-1][0]:
                return d_p[-1][1]
            lt, rt = 0, len(d_p)
            while lt < rt:
                mid = lt + (rt - lt) // 2
                if target <= d_p[mid][0]:
                    rt = mid
                else:
                    lt = mid + 1  # >
            return d_p[rt][1]
        def b_search(d, d_worker):

            lt, rt = 0, len(d)
            while lt < rt:
                mid = lt + (rt - lt) // 2
                if d[mid] < d_worker:
                    lt = mid + 1
                elif d[mid] > d_worker:
                    rt = mid
                else:
                    return mid
            return rt - 1

        d_p = sorted(zip(difficulty, profit))
        import heapq
        hq = []
        mx_profit = []
        for d, p in d_p:
            heapq.heappush(hq, -p)
            mx_profit.append((d, -hq[0]))

        total = 0
        for w in worker:
            total += b_search(mx_profit, w)
        return total