import heapq
arr = [ 1,20,4,5,90,10,220,33,500,0]
hq = []
for v in arr:
    heapq.heappush(hq, -v)
    print(-hq[0], end=", ")


# 1, 20, 20, 20, 90, 90, 220, 220, 500, 500,
