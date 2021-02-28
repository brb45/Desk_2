
# 1.
s = '123'
a = s.split()
# ['123']

b = list(s)
# ['1', '2', '3']

# c = s.split('') # ValueError: empty separator
#
s = '123'
a = s.split()

print(a) # ['123']

b = list(a)
c = ''.join(b)
print(b) # ['123']
print(c, type(c)) # 123 <class 'str'>

# 1.1
s = " \n\nabc  dd  d\n\n "
ss = s.split() #       ['abc', 'dd', 'd']
sss = s.split(" ") #   ['', '\n\nabc', '', 'dd', '', 'd\n\n', '']
ssss = s.split("\n") # [' ', '', 'abc  dd  d', '', ' ']
print(ss)
print(sss)
print(ssss)

s = '  '
print(s.split(" ")) # ['', '', '']
s = "a  "
print(s.split(" ")) # ['a', '', '']

# 2.
a = [3, 2, 0, 6, 1, 4, 5]
# Does Not work
a[0:4].sort()  # a[0:4] is copy of the first 4 elements of a
# after calling a[0:4].sort(), doesNOT change the order of first 4 elements
print(a) # [3, 2, 0, 6, 1, 4, 5]

# works
a[0:4] = sorted(a[0:4])
# [0, 2, 3, 6, 1, 4, 5]
print(a)

# Error
# .sort() does NOT return a list
# a[0:4] = a[0:4].sort() TypeError: can only assign an iterable

# 3.
# string to list: use list() or string split function
s = "abc"
s_list = list(s)
s_list = [ch for ch in s]

# list to string
# Using .join(), make sure each element in list is a string
# otherwise, type error
ss = "".join(s_list)

s_lst = ['a', 'b',10, 'c']
# s_str = "".join(s_lst)
# TypeError: sequence item 2: expected str instance, int found

# DO NOT use str to combine list elements, It does NOT work
s_lst = ['a', 'b',10, 'c']
print(str(s_lst)) # ['a', 'b', 10, 'c']

# 4.
# Maximal positive 32-bit number is 0x7FFFFFFF = (1<<31) - 1 =2147483647
(1 << 31) -1 # the parenthesis is IMPORTANT
# The minimal number in two's complement notation is 0x80000000 = -2147483648
print(2**31-1, (1<<31) - 1, -1<<31)
print(float('inf'))
# 2147483647 2147483647 -2147483648
# inf

# max: \
float('inf')
# min: \
float('-inf')

# strs1_st = sorted(strs1, key=len)

res = []
def mod(res):
    res = [1,2,3]
mod(res)
# print(res) []
# a) pass a local list
# mod(res)
# res: reference to a local list
# # b) pass a copy of a local list or part of a local list
# Not intent to change res, but to create a tmp list with res as a base list
# mod(res[1:4]) or mod(res + [100])


#
res = []
print(id(res)) # 23479760
def mod(res):
    print(id(res)) # 23479760
    res += [1, 2, 3]
    print(id(res)) # 23479760

mod(res)
print(res)  # [1, 2, 3]

#
res = []
print(id(res)) # 17253840
def mod(res):
    print(id(res)) # 17253840
    res = [1, 2, 3]
    print(id(res)) # 17255000

mod(res)
print(res)  # []
#
res = []
def mod(res):
    c = [1,2,3]
    res += c

mod(res)
print(res)  # [1, 2, 3]

# 842. Split Array into Fibonacci Sequence
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        # 5:33 4/22

        def splitArray(S, ind, ans, res):
            if ind == len(S) and len(ans) > 2:
                res += ans
                return
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
                splitArray(S, i + 1, ans, res)
                if res:
                    break
                ans.pop()

        res = []
        splitArray(S, 0, [], res)
        return res

arr = [0,1,2,3,4,5]

for i in range(len(arr)):
    print(i)
    if arr[i] > 1:
        i = 4

    print("----", i)

# 0
# ---- 0
# 1
# ---- 1
# 2
# ---- 4
# 3
# ---- 4
# 4
# ---- 4
# 5
# ---- 4

#
s = "a b c"
ls = list(s)
['a', ' ', 'b', ' ', 'c']
print(ls)

#
from collections import Counter

arr = [1,2]  * 5
print(arr) # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
brr = [[1,2] * 5]
print(brr) # [[1, 2, 1, 2, 1, 2, 1, 2, 1, 2]]

crr = [(1,2) * 5]
print(crr) # [(1, 2, 1, 2, 1, 2, 1, 2, 1, 2)]

crr = [{'a':1, 'b':2} * 5]
print(crr) # TypeError: unsupported operand type(s) for *: 'dict' and 'int'
crr = [{'a':1} for _ in range(5)]
print(crr) # [{'a': 1}, {'a': 1}, {'a': 1}, {'a': 1}, {'a': 1}]

#
for a in arr:
    if a == 1:
        arr.remove(a)
    if a == 5:
        arr.remove(a)
# [2, 3, 4, 6]
print(arr)

#
arr = [1,2,3,4,5,6]

for i in range(len(arr)):
    if i & 1:
        print(f"len(arr) is {len(arr)} --> {arr}")
        arr.pop(i) # IndexError: pop index out of range
print(arr)

# len(arr) is 6 --> [1, 2, 3, 4, 5, 6]
# len(arr) is 5 --> [1, 3, 4, 5, 6]
# len(arr) is 4 --> [1, 3, 4, 6]
# Traceback (most recent call last):
#   File "C:/Users/jsun/Documents/Desk_1/log_test.py", line 6, in <module>
#     arr.pop(i) # IndexError: pop index out of range
# IndexError: pop index out of range

##
dic = dict(a=1, b= 2, c=3)

for key in dic:
    dic.pop(key)

print(str(dic))
# Traceback (most recent call last):
#   File "C:/Users/jsun/Documents/Desk_1/log_test.py", line 3, in <module>
#     for key in dic:
# RuntimeError: dictionary changed size during iteration



