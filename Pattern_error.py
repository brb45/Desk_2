# 9/6/2020
# 10/20/20


#_____________________________________________________________________
from collections import OrderedDict
from collections import defaultdict
import queue
from bisect import bisect_left, bisect_right
from functools import cmp_to_key
# bisect.bisect
# bit mask
# Python, Union-find
import heapq

import math
math.ceil(x)
math.floor()
# 32-bit integer range -2**31 <= num <= 2**31 -1
# We have already many 2-pass or 3-pass problems, like 821. Shortest Distance to a Character.
# They have almost the same idea.
# One forward pass and one backward pass.


#### Pattern
#0) Algorithms
"""
0.0) Logrithm log(N), binary search
0.1) Linear: N : two pointer; Using stack or deque; fast/slow pointer; dict lookup
0.2) Linear with Binary optimization: N*Log(N) : sort + binary search
0.3) N**2
0.4) > N*2, N*3 or exponential 2^n: Need to consider
# Space helper: dict, lookup or DP
0.41) exponential 2^n
0.5) factorial: n!
"""

## find the total soln: DFS
## find the longest, most: DP
## find the least/shortest: BFS

#1) size of an array: n=10
#2) print((0-1)%10)  # 9
#3) print((1+10)%10)  # 1



#_________________________________________
nums.sort(reverse=True)
nums[::2], nums[1::2] = nums[N // 2:], nums[:N // 2]
####1. syntax error
m = {"a": 1, "b":2 }
# if "a" is not in m:
#     print(True)
#     if "a" is not in m:
#                    ^
# SyntaxError: invalid syntax

# correct
if "a" not in m:
    print(False)
else:
    print(True)

#5) list.reverse() dese NOT return
nums = [1,2,4,6,3]
for num in nums.reverse():
    print(num)
# TypeError: 'NoneType' object is not iterable
# correct
nums = [1,2,4,6,3]
for num in nums[::-1]:
    print(num)
print(f"{type(nums[::-1])}") # <class 'list'>
# nums[::-1] return a reversed list

#6) array operations

# array trick
s = [1,2,3,4,5]
print(s) # [1, 2, 3, 4, 5]
ss = s[:3]
print(ss) # [1, 2, 3]
ss[0] = 100
print(ss) # [100, 2, 3]
print(s) #  [1, 2, 3, 4, 5]

s = [1,2,3,4,5]
print(s) # [1, 2, 3, 4, 5]
ss = s[:3]
print(ss) # [1, 2, 3]
s[0] = 100
print(ss) # [1, 2, 3]

##
nums = [1,2]

print(nums[0:0],nums[2:])  # [] []

#7) nums[::-1] return a reversed list or string
nums = [1,2,3,4]

print(type(nums[::-1]) , nums[::-1])
# <class 'list'> [4, 3, 2, 1]

#7) list, set, collections.deque, collections.Counter need iterable
a = list([10])
print(a) # [10]

b = list(100) # TypeError: 'int' object is not iterable
print(b)

d = set([100])
print(d) #{100}
c = set(100)
print(c)  # TypeError: 'int' object is not iterable

##
res = [1,2,3]

while len(res) > 1:
    res = res[1:]

print(res) # [3]

## list.pop(index)
res = [1,2,3]

while len(res) > 1:
    res.pop(0)

print(res) # [3]

## Remove an element: list.remove(elemet)
res = [1,2,3]

if 1 in res:
    res.remove(1)

print(res) # [2, 3]

##

#8 iterables
a = {1, 2, 3}
for v in a:
    print(v)
# 1
# 2
# 3
from collections import Counter

cnt = Counter(["a", "a", 'b', 'c', 'b'])
for item in cnt:
    print(item, end=" ")

# a b c

#9. set doesn't do anything when adding an existing element
a_set = set([1,2,3])
a_set.add(3)
print(a_set) # {1, 2, 3}

#10. initiate dic with value = 0 of each key
dic = {ch : 0 for ch in "croak"}

#11 Array
nums = [1,2,3,4]
print(sum(nums[0:2]))
print(sum(nums[1:2]))
print(sum(nums[1:0]))
print(nums[:])
print(nums[::])
print(nums[::1])
print(nums[::-1])

# 3
# 2
# 0
# [1, 2, 3, 4]
# [1, 2, 3, 4]
# [1, 2, 3, 4]
# [4, 3, 2, 1]

#12 array generation: tricky
a = [[]*6]
print(a)
# [[]]

b = [[1]*6]
print(b)
[[1, 1, 1, 1, 1, 1]]

a = [[] for _ in range(6)]
print(a)
# [[], [], [], [], [], []]

#13
a = "12345678"
res = ""

# r = res + ch for ch in a
# error

res = [res + ch for ch in a]
print(res)
# ['1', '2', '3', '4', '5', '6', '7', '8']

#14
# collections.OrderedDict([items])
# 15 32 bit integer
# [−2^31, 2^31 − 1]
# abs(-2^{31}) = 2^{31}, which is outside the allowed range by 1.
# Instead of a = a * -1 for making numbers negative, use a = -a.
print(17 >> 1) # 8 , 17 >> 1 same as 17 // 2
# Instead of using a // 2 for dividing by 2, use the right shift operator; a >> 1.
# Instead of using a * 2 for doubling, use a = a + a, a += a, or even the left shift operator; a << 1.

## 14.1
arr = [1,2,3]
print(arr.index(2)) # 1
arr.pop(1) # pop(index)
print(arr) # [1, 3]
# remove(element)
arr.remove(3)
print(arr) # [1]

# 15. Determine Prime Number
def is_prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(2, int(x ** 0.5 + 1)):
        if x % i == 0:
            return False
    return True

# 16. Determine GCD: Greatest Common Divisor
def gcd(n1, n2):
    if n1 > n2: return gcd(n2, n1)
    if n1 == 0: return n2
    return gcd(n1, n2 % n1)


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

# 17 LCM = Least Common Multiple
def lcm(x, y):
    return x * y // gcd(x, y)


# 18
print(-5 % 2)  # 1
print( 5 % -2) # -1

mod = 10
print(pow(2, 4, mod)) # 6

m = 3
print(2**m)   # 8
print(1 << m) # 8


# 19 defaultdict
from collections import defaultdict

dic = defaultdict(int)
nums = [1,2,3,4,5,6]
for num in nums:
    if num % 2 == 0:
        dic[num] = 1

for k, v in dic.items():
    print(f"k : v --> ({k}:{v})")

print(len(dic))
print(dic[100])
# k : v --> (2:1)
# k : v --> (4:1)
# k : v --> (6:1)
# 3
# 0
##############################################################################################################
#####0. Tricky
# 1419. Minimum Number of Frogs Croaking
# 681	Next Closest Time

####2. set --> list
s = "abcc c de ed a"
print(set(s)) # {'b', ' ', 'c', 'e', 'd', 'a'}

lt = "a b c d a b"

cc = lt.split(" ")
print(cc) # ['a', 'b', 'c', 'd', 'a', 'b']

cc = set(cc)
print(cc) # {'c', 'b', 'a', 'd'}

cc = list(cc)
cc.sort()
print(cc) # ['a', 'b', 'c', 'd']

lt = "a b c d a b"
lt = set(lt)
print(lt) # {'a', 'c', 'd', ' ', 'b'}

lt = "abcdab"
lt = set(lt)
print(lt) # {'c', 'a', 'd', 'b'}

####3. string replace
s = "abade"

ss = s.replace('a', 'h')
print(ss) # hbhde

# No replacement done, return unchanged string
sss = s.replace('k','U')
print(sss) # abade

####3. boundry check
def cord(S, st, end, rst):
    if st == end:
        rst.append(S[st])
        return
    elif S[st] == '0' and S[end] != '0':
        # ERROR: rst.append(S[st] + '.' + S[st+1:])
        rst.append(S[st] + '.' + S[st + 1:end + 1])
    elif S[st] != '0':
        rst.append(S[st:end + 1])
        if S[end] != '0':
            for i in range(st + 1, end + 1):
                rst.append(S[st:i] + '.' + S[i:end + 1])

# 1. range(i,j) ==> [i,j-1] or [i, j)
# 2. Be careful: if i >= j, the for loop will be skipped.
for i in range(i,j):
    print("i <= j-1")
# 3. if the loop is skipped, i could be undefined and shows an error
for i in range(0,0):
    print("i <= j-1")
print(i)
#     print(i)
# NameError: name 'i' is not defined

# list slicing: a[i:j] returns a list or []
# str slicing: s[i:j]  returns a sub-string or empty string ""
# list_a[1:3]--> list_a[1] and list_a[2]
# a[i:j] does NOT include a[j]
s = "01234"
print(s[1:-1]) # [1,2,3]
print(s[0:3])  # [0,1,2]
print(s[4:-1]) # ""

a_list = [1,2 ,3]
print(a_list[2:-1]) # give an empty array: []
####4.
wd = ['ABc',"DDD", "CCCDd"]
ww = [ item.lower() for item in wd]

print(wd) # ['ABc', 'DDD', 'CCCDd']
print(ww) # ['abc', 'ddd', 'cccdd']

if 'ABc' in wd:
    i = wd.index('ABc')
    print(i)

####5. Use flag
## ___________________________________________________
wordlist = ['ABc',"DDD", "CCCDd"]
w = ['ABc',"DDD", "CCCDd"]
rst = []
w = [item.lower() for item in wordlist]
vowel = ['a', 'e', 'i', 'o', 'u']
print(w)
## 1.
for j, item in enumerate(w):
    flag = True
    if len(item) == len(wd):
        for i, v in enumerate(item):
            if item[i] != wd[i]:
                if item[i] in vowel and wd[i] in vowel:
                    continue
                else:
                    flag = False
                    break
        if flag:
            rst.append(wordlist[j])
            break
    else:
        flag = False
if not flag:
    rst.append("")

print(rst)

# 2
######
wordlist = ['ABc',"DDD", "CCCDd"]
w = ['ABc',"DDD", "CCCDd"]
rst = []
w = [item.lower() for item in wordlist]
vowel = ['a', 'e', 'i', 'o', 'u']
print(w)
wd = 'abc'
for j, item in enumerate(w):
    tmp = " "
    if len(item) == len(wd):
        for i, v in enumerate(item):
            if item[i] != wd[i]:
                if item[i] in vowel and wd[i] in vowel:
                    continue
                else:
                    break
        if i == len(item) - 1:
            if item[i] == wd[i] or (item[i] in vowel and wd[i] in vowel):
                tmp = wordlist[j]
        rst.append(tmp)

print(rst)
## ___________________________________________________________
wordlist = ['ABc',"DDD", "CCCDd"]
w = ['ABc',"DDD", "CCCDd"]
rst = []
w = [item.lower() for item in wordlist]
vowel = ['a', 'e', 'i', 'o', 'u']
wd = 'obc'
# 3
for item in w:
    n = len(item)
    if n == len(wd):
        for i in range(n):
            if item[i] == wd[i]:
                if i == n - 1:
                    rst.append(item)
            else:
                if item[i] in vowel and wd[i] in vowel:
                    if i == n-1:
                        rst.append(item)
                else:
                    break
if not rst:
    rst.append("")
print(rst)

# 4
n = len(wd)
rst = []
for item in w:
    if len(item) == n:
        for i in range(n):
            if item[i] != wd[i]:
                if item[i] not in vowel or wd[i] not in vowel:
                    break
        if i == n - 1 and (item[i] == wd[i] or (item[i] in vowel and wd[i] in vowel)):
            rst.append(item)
if not rst:
    rst.append("")

print(rst)

## ___________________________________________________________
####6.0 Usage of split
s = "abcd"
ss = s.split('.') # No splitting happening
print(ss) # ['abcd']

s = 'a.'
ss = s.split('.')
print(ss) # ['a', '']

s = '.a.'
ss = s.split('.')
print(ss) # ['', 'a', '']

####6.
    # wordlist: List[str]
    # queries: List[str]
def spellchecker(wordlist, queries):  # -> List[str]
    # 6:53 5/16/20 ==> 7:10
    words, first, vowdt = set(wordlist), {}, {}
    vowel, l = set(['a', 'e', 'i', 'o', 'u']), len(queries)
    genkey = lambda s: ''.join(['*' if i in vowel else i for i in s])
    for word in wordlist:
        word_low = word.lower()
        if word_low not in first:
            first[word_low] = word
        key = genkey(word_low)
        if key not in vowdt:
            vowdt[key] = word

    rst = [''] * l
    for i in range(l):
        query = queries[i]
        if query in words: rst[i] = query; continue
        query_low = query.lower()
        if query_low in first: rst[i] = first[query_low]; continue
        key = genkey(query_low)
        if key in vowdt: rst[i] = vowdt[key]
    return rst

def devowel(word):
    return "".join('*' if c in 'aeiou' else c for c in word)

####7.
# python strip() : return a string after removing both leading and trailing spaces.
string = '  xoxo love xoxo   '
s = string.strip()
print(s) # 'xoxo love xoxo'
print(string.strip(' xoe'))  # 'lov'

####8. Double Loop-> 8. String to Integer (atoi)
def myAtoi(str):
    i = 0
    n = len(str)
    res = 0

    while i < n:
        if str[i] == ' ':
            i += 1
        elif str[i].isdigit() or str[i] in ['-', '+']:
            sign = 1
            if str[i] in ['-', '+']:
                if str[i] == '-':
                    sign = -1
                i += 1
            start = i

            while i < n and str[i].isdigit():
                i += 1
            if i > start:
                res = int(str[start:i]) * sign
                if res > 2 ** 31 - 1:  # 2147483647:
                    res = 2 ** 31 - 1 # (pow(2,31)-1
                elif res < -2 ** 31:
                    res = -2 ** 31
                break
            else:
                break
        else:
            break
    return res

####9. Reverse words
def reverseWords(s: str) -> str:
    str_list = s.split()
    str_list.reverse()
    return " ".join(str_list)

####10.
class Solution:
    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == ' ':
            left += 1

        # remove trailing spaces
        while left <= right and s[right] == ' ':
            right -= 1

        # reduce multiple spaces to single one
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1

        return output

    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0

        while start < n:
            # go to the end of the word
            while end < n and l[end] != ' ':
                end += 1
            # reverse the word
            self.reverse(l, start, end - 1)
            # move to the next word
            start = end + 1
            end += 1

####11. 468. Validate IP Address
class Solution:
    def validIPAddress(self, IP: str) -> str:
        # 3:13, 4/17/20
        n = len(IP)
        if '.' in IP:
            cnt = 0
            st = 0
            for i in range(n):
                if IP[i] == '.':
                    cnt += 1
                    if cnt > 3:
                        return "Neither"
                elif not IP[i].isdigit():
                    return "Neither"

                if IP[i] == '.' or i == n - 1:
                    group = IP[st:i] if IP[i] == '.' else IP[st:i + 1]
                    m = len(group)
                    if m == 0 or int(group) > 255 or (m > 1 and IP[st] == '0'):
                        return "Neither"
                    st = i + 1

            if cnt == 3 and IP[-1] != '.':
                return "IPv4"

        elif ':' in IP:
            cnt = 0
            st = 0
            for i in range(n):
                if IP[i] == ':':
                    cnt += 1
                    if cnt > 7:
                        return "Neither"
                # elif (not 'a' <= IP[i] <= 'f') and (not 'A' <= IP[i] <= "F") and (not IP[i].isdigit()):
                elif (not IP[i].isdigit()) and (not 'a' <= IP[i].lower() <= 'f'):
                    return "Neither"

                if IP[i] == ':' or i == n - 1:
                    group = IP[st:i] if IP[i] == ':' else IP[st:i + 1]
                    m = len(group)
                    if m == 0 or m > 4:
                        return "Neither"
                    st = i + 1
            if cnt == 7 and IP[-1] != ':':
                return "IPv6"

        return "Neither"

class Solution:

    def v4(self, IP):
        nums = IP.split('.')
        for x in nums:
            if len(x) == 0 or len(x) > 3:
                return "Neither"
            if x[0] == '0' and len(x) > 1 or not x.isdigit() or int(x) > 255:
                return "Neither"
        return "IPv4"

    def v6(self, IP):
        nums = IP.split(":")
        hexdigits = '0123456789abcdefABCDEF'
        for x in nums:
            if len(x) == 0 or len(x) > 4 or not all(c in hexdigits for c in x):
                return "Neither"
        return "IPv6"

    def validIPAddress(self, IP: str) -> str:
        # 9:13, 6/03/20
        if IP.count('.') == 3:
            return self.v4(IP)
        elif IP.count(':') == 7:
            return self.v6(IP)
        else:
            return "Neither"


class Solution:

    def validIPAddress(self, IP: str) -> str:
        def isIPv4(s):
            try:
                return str(int(s)) == s and 0 <= int(s) <= 255
            except:
                return False

        def isIPv6(s):
            if len(s) > 4: return False
            try:
                return int(s, 16) >= 0 and s[0] != '-'
            except:
                return False

        if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
            return "IPv4"
        if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):
            return "IPv6"
        return "Neither"
####12. string count
s = "abcabca"
print(s.count('a')) # 3
# s.count("a",start, end) # exclude end
print(s.count('a', 0, 6)) # 2
print(s.count('h')) # 0

####13. int(str) throw an exception
s = "abcabca"
print(int(s))
# ValueError: invalid literal for int() with base 10: 'abcabca'
print(int(""))
# ValueError: invalid literal for int() with base 10: ''

####14. list insert
nums = [0,1,2,3,4]
loc = 1
nums.insert(loc, 100)
print(nums) # [0, 100, 1, 2, 3, 4]

####15. 91. Decode Ways

####16.
# 457 Circular Array Loop
# slow/fast pointer  slow == fast
i = -1

while i :
    print(i) # -1
    break

# Search in Rotated Sorted Array II
# 81. Binary Search
# 1191. K-Concatenation Maximum Sum

####15. dp 1
# 5. Longest Palindromic Substring
# 139. Word
# 3d DP , 562. Longest Line of Consecutive One in Matrix


#####17. Boundry check for loop
# At beginning , bypass loop
# and at the end, last element check
# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s):
        # 6/27/20 12:51

        n = len(s)
        if n == 0:
            return 0
        mx = 1
        str_dict = {}
        st = 0

        for i, v in enumerate(s):
            if v not in str_dict:
                str_dict[v] = i
            else:
                if st <= str_dict[v]:
                    tmp_size = i - 1 - st + 1
                    mx = max(tmp_size, mx)
                    st = str_dict[v] + 1
                    str_dict[v] = i
                else:
                    str_dict[v] = i

        if v not in str_dict:
            tmp_size = i - st + 1
        else:
            if st <= str_dict[v]:
                tmp_size = max(str_dict[v] - st, i - 1 - str_dict[v]) + 1
            else:
                tmp_size = i - st + 1

        return max(mx, tmp_size)


class Solution:
    def lengthOfLongestSubstring(self, s):
        # 6/27/20 12:51

        n = len(s)
        s_dict = {}
        st = 0
        cnt = 0

        for i, v in enumerate(s):
            if v in s_dict and s_dict[v] >= st:
                st = s_dict[v] + 1
            s_dict[v] = i
            cnt = max(cnt, i - st + 1)

        return cnt
#####18.0 Stack in increasing order
# 402. Remove K Digits
#####18.1 Parenthesis
# one or two stacks
# linear
# BackTracking with memorization
# 678. Valid Parenthesis String

#####19.
arr = [[1,2,3]]
arr += [4,5,6]
# arr is [[1, 2, 3], 4, 5, 6]

brr = [[1,2,3]]
brr += [[4,5,6]]
# brr is [[1, 2, 3], [4, 5, 6]]

## string join
# string.join(iterable)
s = ('a','b','c','d')

ss = ','.join(s)
print(type(ss), ss) # <class 'str'> a,b,c,d

sss = ''.join(s)
print(type(sss), sss) # <class 'str'> abcd

s = "abcd e "

ss = ','.join(s)
print(type(ss), ss) # <class 'str'> a,b,c,d, ,e,

sss = ''.join(s)
print(type(sss), sss)# <class 'str'> abcd e

#####20. Loop
# 556. Next Greater Element III
for k in range(1,1):
    print(k)
print(f"k is {k}")
#     print(f"k is {k}")
# NameError: name 'k' is not defined

for k in range(0,1):
    print(k)
print(f"k is {k}") # k is 0
# k will not be 1

for i in range(1, 3):
    print(i)
print(i)

# 1
# 2
# 2

nums = [ 7,6,5,4,3,2,1]
nums[4:].sort()
print(nums) # [7, 6, 5, 4, 3, 2, 1]

nums[4:] = sorted(nums[4:])
print(nums) # [7, 6, 5, 4, 1, 2, 3]
# 179. Largest Numbe

#####21. Sliding Window
# 1234. Replace the Substring for Balanced String
L, m, D, c, i, j = len(S), len(S), {k: v - len(S) // 4 for k, v in collections.Counter(S).items() if v > len(S) // 4}, {
    k: 0 for k in 'QWER'}, -1, 0
# if not D:
    # return 0
for j, s in enumerate(S):
    while i < L - 1 and any(c[k] < D[k] for k in D): i += 1; c[S[i]] += 1
    if i == L - 1 and any(c[k] < D[k] for k in D): break
    m = min(m, i - j + 1)
    c[s] -= 1
# return m


def balancedString(s):
    count = collections.Counter(s)
    res = n = len(s)
    i = 0
    for j, c in enumerate(s):
        count[c] -= 1
        while i < n and all(n / 4 >= count[c] for c in 'QWER'):
            res = min(res, j - i + 1)
            count[s[i]] += 1
            i += 1
    return res

def balancedString1(s):
    """
    :type s: str
    :rtype: int
    """
    ccs = collections.Counter(s)
    cc = {k: ccs[k] - len(s) / 4 for k in ccs if ccs[k] > len(s) / 4}
    if len(cc) == 0: return 0
    i = 0
    m = len(s)
    for j in range(len(s)):
        if s[j] in cc: cc[s[j]] -= 1
        while (all([cc[k] <= 0 for k in cc])):
            m = min(m, j - i + 1)
            if s[i] in cc: cc[s[i]] += 1
            i += 1
    return m

######22. Sub-sequence of a string

# Create all sub-sequence of a string
def sub_seq(s, i, tmp, res):
    if i == len(s):
        return
    for j in range(i, len(s)):
        tmp_res = tmp+s[j]
        if tmp_res not in res:
            res.append(tmp + s[j])
        sub_seq(s, j+1, tmp_res, res)

##
# 522. Longest Uncommon Subsequence II
# brute force , create all seb-sequence of all strings
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:

        # Create all sub-sequence of a string
        def sub_seq(s, i, tmp, res):
            if i == len(s):
                return
            for j in range(i, len(s)):
                tmp_res = tmp + s[j]
                if tmp_res not in res:
                    res.append(tmp + s[j])
                sub_seq(s, j + 1, tmp_res, res)

        res = []
        subseq_map = collections.Counter()
        for s in strs:
            sub_seq(s, 0, "", res)
            subseq_map.update(res)
            res.clear()

        max_len = -1
        for s in subseq_map:
            if subseq_map[s] == 1:
                max_len = max(max_len, len(s))
        return max_len
### Determine if a str is a commom sub-string of another one
def is_common(sub,t):
    i = 0
    for ch in t:
        if i == len(sub):
            break
        if ch == sub[i]:
            i += 1
            # continue
    return i == len(sub)

######23 DFS
# 79. Word Search
def exist(self, board, word):
    if not board:
        return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if self.dfs(board, i, j, word):
                return True
    return False

# check whether can find word, start at (i,j) position
def dfs(self, board, i, j, word):
    if len(word) == 0: # all the characters are checked
        return True
    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
        return False
    tmp = board[i][j]  # first character is found, check the remaining part
    board[i][j] = "#"  # avoid visit agian
    # check whether can find "word" along one direction
    res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
    or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
    board[i][j] = tmp
    return res

#####24 Binary Search
# 34. Find First and Last Position of Element in Sorted Array
# 162. Find Peak Element

#####25 Two pointers
# 80. Remove Duplicates from Sorted Array II

#####26 cumulative subsequence/sub-array sum or product
# 560. Subarray Sum Equals K
# 75. Sort Colors


#####27 Bad Strategy
# Don't nest loops : NO while loop within anther loop
# 809. Expressive Words
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        # 3:24 7/16/20
        # 9:05 7/17/20
        # Tricky to hell

        res = 0

        for wd in words:
            i, j = 0, 0
            while i < len(S):
                if j < len(wd) and S[i] == wd[j]:
                    i += 1
                    j += 1
                elif 0 < i < len(S) - 1 and S[i] == S[i - 1] == S[i + 1]:
                    while 0 < i < len(S) and S[i] == S[i - 1]:  ### BAD practices
                        i += 1
                # elif (i > 1 and S[i] == S[i-1] == S[i-2]):
                #     i += 1
                else:
                    break

            if i == len(S) and j == len(wd):
                res += 1

        return res

# greatest common divisor
def gcd(x,y):
    return x if y == 0 else gcd(y, x % y)

s = set(range(7))
for i in range(7):
    if i < 6:
        s.remove(i)
        print(i, end=" ")
# 0 1 2 3 4 5

s = set(range(7))
s -= {2,3}
print(s)  # {0, 1, 4, 5, 6}
s += {100}
print(s)
# RuntimeError: Set changed size during ite


# 8/26/20
# Strategy: transformation the answer in a different way
# 777. Swap Adjacent in LR String

from functools import cmp_to_key
nums = [28, 50, 17, 12, 121]

nums.sort(key=cmp_to_key(lambda x, y: 1 if x < y else -1)) # Descending
print(nums)
# [121, 50, 28, 17, 12]
nums.sort(key=cmp_to_key(lambda x, y: -1 if x < y else 1)) # increasing
print(nums)
# [12, 17, 28, 50, 121]

from functools import cmp_to_key

# function to sort according to last character
def cmp_fun(a, b):
    if a[-1] < b[-1]:
        return -1  # Low to high: incremental
    elif a[-1] > b[-1]:
        return 1
    else:
        return 0

from collections import defaultdict

dic = defaultdict(list)
dic.update([('a', 100), ('b', 200), ('c', 300)])

for key, val in dic.items():
    print(key, val , end=", ")

if 'd' in dic:
    print(True)

if dic['d'] == []:
    print("key not present, showing default value")
    # key not present, showing default value

from pprint import pprint
grid = [list(range(5)) for _ in range(5)]
pprint(grid)

print()

flat = [num for row in grid for num in row]
pprint(flat)

# [[0, 1, 2, 3, 4],
#  [0, 1, 2, 3, 4],
#  [0, 1, 2, 3, 4],
#  [0, 1, 2, 3, 4],
#  [0, 1, 2, 3, 4]]
#
# [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]


def isMagicSquare(grid):
    '''
    Check whether the given grid is a magic square
    '''
    # Check the elements
    flat = [num for row in grid for num in row]
    if sorted(flat) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return False

    # Check the row, column and diagnal sums
    row_sums = [sum(row) for row in grid]
    col_sums = [sum([row[i] for row in grid]) for i in range(3)]

    diag_sums = [sum([grid[i][i] for i in range(3)]), (grid[0][2] + grid[1][1] + grid[2][0])]
    row_sums.extend(col_sums)
    row_sums.extend(diag_sums)
    return len(set(row_sums)) == 1


grid = []
row1= [1,2,3,4]
row2 = [10,20,30,40]
row3 = [100,200,300,400]

grid.append(row1)
grid.append(row2)
grid.append(row3)

from pprint import pprint
pprint(grid)
# [[1, 2, 3, 4], [10, 20, 30, 40], [100, 200, 300, 400]]
row_sum = [sum(row) for row in grid]
print(row_sum)
# [10, 100, 1000]
col_sum = [sum(row[j] for row in grid)  for j in range(3)]
print(col_sum)
# [111, 222, 333]


def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
    # 9:37 --> 9:52 --> 10:31 9/14/20
    cnt = 0
    # Construct the 3x3 square
    for i in range(len(grid) - 2):
        for j in range(len(grid) - 2):
            temp_grid = [grid[i + k][j:j + 3] for k in range(3)]
            if self.isMagicSquare(temp_grid):
                cnt += 1

    return cnt


# sorted list : ['for', 'geeks', 'geekw']


board = [ [1,2,3,4], [5,6,7,8],[9,10,11,12]]

for i, row in enumerate(board):
    print(i,"-->", row)
# 0 --> [1, 2, 3, 4]
# 1 --> [5, 6, 7, 8]
# 2 --> [9, 10, 11, 12]

board = [ [1,2,3,4], [5,6,7,8],[9,10,11,12]]

for i, row in enumerate(board[::-1]):
    print(i,"-->", row)
# 0 --> [9, 10, 11, 12]
# 1 --> [5, 6, 7, 8]
# 2 --> [1, 2, 3, 4]
