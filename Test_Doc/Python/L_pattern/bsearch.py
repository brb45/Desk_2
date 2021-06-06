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

# find left most
def bs1(ar, tg):
    lt, rt  = 0, len(ar)
    while lt < rt:
        mid = lt + (rt - lt )//2
        if ar[mid] >= tg:
            rt = mid
        else:
            lt = mid + 1
    return lt

# find the right most one if more than one in the sorted
def bs2(ar, tg):
    lt, rt = 0, len(ar)
    while lt < rt:
        mid = lt + (rt - lt) // 2
        if ar[mid] > tg:
            rt = mid
        else:
            lt = mid + 1
    return lt - 1
print(ar) #                   [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5,  8,  8,  9,  15]
print(list(range(len(ar)))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(bs(ar,4)) # 3
print(bs1(ar,5)) # 4
print(bs2(ar,5)) # 10


print(bs(ar,40)) # -1
print(bs1(ar,40)) # 15
print(bs2(ar,40)) # 14

print(bs(ar,-40)) # -1
print(bs1(ar,-40)) # 0
print(bs2(ar,-40)) # -1

