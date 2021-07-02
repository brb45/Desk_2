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