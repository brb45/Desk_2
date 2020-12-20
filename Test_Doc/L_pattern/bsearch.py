ar = [1,9,5,4,5,5,5,5,5, 5,8,8,3,2, 15]
ar.sort()

def bs(ar, tgt):
    lt, rt = 0, len(ar)

    while lt < rt:
        mid = lt + (rt-lt)//2
        if ar[mid] == tgt:
            return mid
        elif ar[mid] > tgt:
            rt = mid
        else:
            lt = mid + 1

    return -1

def bs1(ar, tg):
    lt, rt  = 0, len(ar)
    while lt < rt:
        mid = lt + (rt - lt )//2
        if ar[mid] >= tg:
            rt = mid
        else:
            lt = mid + 1
    return lt

def bs2(ar, tg):
    lt, rt = 0, len(ar)
    while lt < rt:
        mid = lt + (rt - lt) // 2
        if ar[mid] > tg:
            rt = mid
        else:
            lt = mid + 1
    return lt - 1
print(ar)
print(list(range(len(ar))))
print(bs(ar,5))
print(bs1(ar,5))
print(bs2(ar,5))
# [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 8, 8, 9, 15]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# 7
# 4
# 10

