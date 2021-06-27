nums = [1,3,4,5,0, -1 , -5]
# sort incremental
nums.sort()
print(nums)
# [-5, -1, 0, 1, 3, 4, 5]
# sort decremental
nums.sort(key=lambda x: -x)
print(nums)
# [5, 4, 3, 1, 0, -1, -5]

def my_arr(arr):
    arr[0] = 199

arr = list(range(5))

# print(arr)

# my_arr(arr)
# print(arr)

def y_arr(arr):
    def change_arr(arr):
        arr[0] = 100

print(arr)

y_arr(arr)

print(arr)

[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]



import operator
import copy


arr = []

# b = "abc"
# arr += b
# print(arr)

def helper(arr):
    b = [1,2,3]
    arr = b

helper(arr)
print(arr)  # []



# reverse() vs reversed()
# sort() vs sorted()
# nums.reverse()

# Not working
# word = sorted(word, key=(len), key=str.lower)
# word = sorted(word, key=(len,str.lower))

# working
# s_sorted = sorted(s_arr, key= lambda x: (len(x), x.lower()))
# s_sorted = sorted(s_arr, key = len)
# s_sorted = sorted(s_arr, key = str.lower)
# (sorted(strs, key=str.upper)

n = 5


dp1 = [[1, 1] for i in range(n)]
dp = [[1, 1]] * n  # [max_len, cnt]

dp1[0][0] = 100
dp[0][0] = 100
print(dp1) # [[100, 1], [1, 1], [1, 1], [1, 1], [1, 1]]
print(dp) # [[100, 1], [100, 1], [100, 1], [100, 1], [100, 1]]

#-----------------------------------------
arr = [0,0,1,2,4,8, -1,-2,-4,-8]

nums = sorted(arr, key=abs)
print(nums) # [0, 0, 1, -1, 2, -2, 4, -4, 8, -8]

arr = [0,0,1,2,4,8, -1,-2,-4,-8]

s = 'abcd'
arr.extend(s)

print(arr) #[0, 0, 1, 2, 4, 8, -1, -2, -4, -8, 'a', 'b', 'c', 'd']

import copy
dic = {'a': 0, 'b': 1}
dic_copy = dic.copy()
print(dic_copy)
dic_deepCopy = copy.deepcopy(dic)
print(dic_deepCopy)
# {'a': 0, 'b': 1}
# {'a': 0, 'b': 1}

from collections import deque
dq = deque([1,2,3,4,5])
dq_cpy = dq.copy()
print(dq_cpy)
dq_deepCopy = copy.deepcopy(dq)
print(dq_deepCopy)
# deque([1, 2, 3, 4, 5])
# deque([1, 2, 3, 4, 5])

a = (1,2)
b = (3,4)

c = a + b
print(c)
# (1, 2, 3, 4)


d = list(range(10))
print(d) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
##

arr = ['a']
arr += 'b'

arr += ['c', ['d']]
# arr = arr + "M" # TypeError: can only concatenate list (not "str") to list
arr += "M" # OK

#
n = 3
arr = [[[-1, 0]] for _ in range(n)]

from pprint import pprint

pprint(arr)
[[[-1, 0]], [[-1, 0]], [[-1, 0]]]
#
arr = [1,2,3]

def change_arr(arr):
    arr = [4,5,6]

change_arr((arr))
print(arr)
# [1, 2, 3]

def change_arr_1(arr):
    arr[:] = [4,5,6,6]

change_arr_1(arr)
print(arr)
# [4, 5, 6, 6]
#ADD
#list.append(elem) -- adds a single element to the end of the list.
# does not return the new list, just modifies the original.

# list += [elem] same as list.append(elem)

#list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
#list.extend(list2)--list2 must be a list or iterable; adds the elements in list2 to the end of the list.


#search
#list.index(elem) -- searches the given element and returns its index.
#list.index(elem,start_pos, end_pos)
#Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
#i = somelist.index(x) if x in somelist else None

#sort
#list.sort() -- sorts the list in place (does not return it). (The sorted() function shown below is preferred.)
#list.reverse() -- reverses the list in place (does not return it)

##
#list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError)
##list.pop(index) -- removes and returns the element at the given index.
#list.pop() -- remove the last element, and return the element being removed
# del list[index]

a = list(10)
# TypeError: 'int' object is not iterable

# -----------------------------------------------------------------------------
from functools import cmp_to_key
nums = [28, 50, 17, 12, 121]

nums.sort(key=cmp_to_key(lambda x, y: -1 if x > y else 1)) # Descending
print(nums)
# [121, 50, 28, 17, 12]
nums.sort(key=cmp_to_key(lambda x, y: -1 if x < y else 1)) # increasing
print(nums)
# [12, 17, 28, 50, 121]


# 1.
# list slicing returns a list or empty list
word = ["Abd",'abc','aBc','abC',"ABCD",'ABCDE','ac']

print(word[0:0])      # []
print(word[4:-1:-1])  # []
print(word[0:1])      # ["Abd"]
print(word[:2])       # ['Abd', 'abc']
print(word[4:])       # ['ABCD', 'ABCDE', 'ac']
print(word[4:-1])     # ['ABCD', 'ABCDE'])

a = [1,2,3]
b = a[::]
c = a[:]
b[0] = 100

print(a)    # [1, 2, 3]
print(b)    # [100, 2, 3]
print(c)    # [1, 2, 3]

# 2.
a = [1,2,3,4,5,6]
print(a[: 4]) # [1, 2, 3, 4]
# same as
print(a[0:4]) # [1, 2, 3, 4]

print(a[1:]) # [2, 3, 4, 5, 6]
print(a[1:-1:2]) # [2, 4]

## 3.
# max, min
a = [1,2,3,4,5,6]
print(max(a)) # 6
print(max(1,2,3,8,4,5,6)) # 8
print(max(*a)) # 6

# sum
squares = [1, 4, 9, 16]
##
ss = sum(squares) # 30
ss = sum(*squares) # Error
# TypeError: sum expected at most 2 arguments, got 4

# sum(iterable, int)  at most two arguments
squares = [1, 4, 9, 16]
print(sum(squares))         #   30
print(sum(squares, 1000))   #   1030

## 4.
a_tuple = ([1,2],3)
print(type(a_tuple), a_tuple) # <class 'tuple'> ([1, 2], 3)

a_tuple[0].append(100)
print(a_tuple) #    ([1, 2, 100], 3)

# a_set = {[1,2],3}  TypeError: unhashable type: 'list'
# print(type(a_set), a_set)

## 5. List Sorting with lambda
s_arr = ['ab', 'abc', 'Cba', 'ddf', 'Dh', 'Ag']

s_sorted = sorted(s_arr, key=lambda x: (len(x), x.lower()))
# print(s_sorted)  ['ab', 'Ag', 'Dh', 'abc', 'Cba', 'ddf']

ss_sorted = sorted(s_arr, key=len)
# print(ss_sorted) ['ab', 'Dh', 'Ag', 'abc', 'Cba', 'ddf']
sss_sorted = sorted(s_arr, key=str.lower)
# print(sss_sorted) ['ab', 'abc', 'Ag', 'Cba', 'ddf', 'Dh']

## 5.1
cnt_dict = {'a':4, 'b':8, 'c':10, 'd':4, 'e':10, 'f':5, 'h':5, 'g':5}
cnt_list = []

for letter in cnt_dict.items():  # letter is of type tuple
    print(letter, end=", ")
    cnt_list.append(letter)

cnt_order_list = sorted(cnt_list, key=lambda x: (x[1],x[0]), reverse=True)
# reverse=True apply to both x[1] and x[0]
print(type(letter))                     # < class 'tuple' >
print(f"cnt_list is {cnt_list}")
# cnt_list is [('a', 4), ('b', 8), ('c', 10), ('d', 4),
#              ('e', 10), ('f', 5), ('h', 5), ('g', 5)]
print(f"cnt_order_list is {cnt_order_list}")
# cnt_order_list is [('e', 10), ('c', 10), ('b', 8), ('h', 5),
#                    ('g', 5), ('f', 5), ('d', 4), ('a', 4)]
print()

## 5.2
wd_cnt_lst = [('a', 10), ('b', 5), ('a', 5), ('a', 7), ('c', 15), ('b', 3), ('c', 12)]

print(sorted(wd_cnt_lst))
# [('a', 5), ('a', 7), ('a', 10), ('b', 3), ('b', 5), ('c', 12), ('c', 15)]

print(sorted(wd_cnt_lst, key=lambda x: x[0]))
# [('a', 10), ('a', 5), ('a', 7), ('b', 5), ('b', 3), ('c', 15), ('c', 12)]

print(sorted(wd_cnt_lst, key=lambda x: x[1]))
# [('b', 3), ('b', 5), ('a', 5), ('a', 7), ('a', 10), ('c', 12), ('c', 15)]

print(sorted(wd_cnt_lst, key=lambda x: x[0], reverse=True))
# [('c', 15), ('c', 12), ('b', 5), ('b', 3), ('a', 10), ('a', 5), ('a', 7)]

##5.3
str_lst = [("abc", 4),  ("cd", 4), ("avdk", 10),
           ("ab", 5), ("helf", 12), ("aaaa", 8)]
print(sorted(str_lst, key=lambda x: (len(x[0]))))
# [('cd', 4), ('ab', 5), ('abc', 4), ('avdk', 10), ('helf', 12), ('aaaa', 8)]

# print(sorted(str_lst, key=lambda x: (len(x[0]), x[0])))
[('ab', 5), ('cd', 4), ('abc', 4), ('aaaa', 8), ('avdk', 10), ('helf', 12)]

print(sorted(str_lst, key=lambda x: (len(x[0]), x[0]), reverse=True))
# [('helf', 12), ('avdk', 10), ('aaaa', 8), ('abc', 4), ('cd', 4), ('ab', 5)]

str_list = ["abc", "aaa", "def", "ab", "ba", "cd", "fhef", "kdfj", "efgh"]

# print(sorted(str_list, key=len))
# ['ab', 'ba', 'cd', 'abc', 'aaa', 'def', 'fhef', 'kdfj', 'efgh']

# print(sorted(str_list, key=lambda x: (len(x))))
# ['ab', 'ba', 'cd', 'abc', 'aaa', 'def', 'fhef', 'kdfj', 'efgh']

print(sorted(str_list, key=(len, lambda x: x[0]))) # TypeError: 'tuple' object is not callable

print(sorted(str_list, key=lambda x: (len(x), x)))
['ab', 'ba', 'cd', 'aaa', 'abc', 'def', 'efgh', 'fhef', 'kdfj']

str1_list = ["abc", "Aaa", "def", "ab", "Ba", "cd", "fhef", "Kdfj", "efgh"]
print(sorted(str1_list, key=len))
# ['ab', 'Ba', 'cd', 'abc', 'Aaa', 'def', 'fhef', 'Kdfj', 'efgh']
print(sorted(str1_list, key=str.lower))
# ['Aaa', 'ab', 'abc', 'Ba', 'cd', 'def', 'efgh', 'fhef', 'Kdfj']
print(sorted(str1_list, key=lambda x: x.lower()))
# ['Aaa', 'ab', 'abc', 'Ba', 'cd', 'def', 'efgh', 'fhef', 'Kdfj']
print(sorted(str1_list, key=lambda x: [len(x), x.lower()]))
# ['ab', 'Ba', 'cd', 'Aaa', 'abc', 'def', 'efgh', 'fhef', 'Kdfj']


## 6. _________________________________________
p = [10,3,0,5,3]
sp = [2,10,1,1,3,100, 99]
p_s = list(zip(p,sp))
print(p_s)
# [(10, 2), (3, 10), (0, 1), (5, 1), (3, 3)]

# convert list of tuple to dict
p_s1 = dict(p_s)  # {10: 2, 3: 3, 0: 1, 5: 1}

#@@ 6
a = [1,2]
v = 3
print(a + [v])#[1, 2, 3]
print(a) #[1, 2]

#@@ 7. empty array
rs = []
a = list()
a.append(100)

#@@ 8.
maxh = [0 for __ in range(5)]
print(maxh) #[0, 0, 0, 0, 0]
#4.
arr = [0]*5
print(arr) #[0, 0, 0, 0, 0]

arr = [1,2,3]
arr_copy = arr*4
print(arr_copy)
# [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

#@@ 9.
#range(start, stop, step), is iterable, but not iterator
for i in range(4,1,-1):
    print(i," ", end="") #4  3  2  , exclude end = 1
print()

for i in range(5, -1, -1): #won't work range(5,-1)
    print(i," ", end="") #5 4  3  2  1  0 exclude end = -1
print()

#@@ 10.
from pprint import pprint
a = [ [0]*5 for __ in range(5)]
a[0][0] = 99
a[4][4] = 88
pprint(a)
#Create 2-D array
# [[99, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 88]]

from pprint import pprint
row = 4
col = 10
dp = [[1 for __ in range(col)] for __ in range(row)]
pprint(dp)
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

#@@ 11.
rs = []
rs = [[8]+ [4] for r in range(5)]
#[[8, 4], [8, 4], [8, 4], [8, 4], [8, 4]]

#@@ 11.1
result = [[]]
print(len(result))  # 1
print(len(result[0])) # 0

#@@ 12.
a = (n*n for n in range(5))
print(type(a)) #<class 'generator'>
b = []
b.extend(a)
print(b) #[0, 1, 4, 9, 16]

#@@ 13.
case = ["wifi"]
case1 = ['wifi']
print(case==case1) #True
print(case is case1) #False

case = "wifi"
case1 = 'wifi'
print(case==case1) #True
print(case is case1) #True

spam = ('hello', )
eggs = ('hello', )
print(spam is eggs) # True

#@@ 14.
my_tuple = ("hello")
print(type(my_tuple)) #str

my_tuple = ("hello",)
print(type(my_tuple))#tuple
tuple = (1, 2, 'hi')  # (1, 2, 'hi')
len(tuple)  # 3
tuple[2]  # hi

# tuple[2] = 'bye'  # NO, tuples cannot be changed

#@@ 15
def all_indices(value, qlist):
    indices = []
    idx = -1
    while True:
        try:
            idx = qlist.index(value, idx+1)
            indices.append(idx)
        except ValueError:
            break
    return indices

all_indices("testID", ["testID","testr","station","testID"])


#@@ 17
#Shallow copy
ls = [[1,2,3],"wifi","bt","tk"]
cp = ls.copy()

ls[0][0]=[1,23]
print("cp is ", cp)
print("ls is ",ls)
print(id(cp), ", ", id(ls))
# cp is  [[[1, 23], 2, 3], 'wifi', 'bt', 'tk']
# ls is  [[[1, 23], 2, 3], 'wifi', 'bt', 'tk']
# 2924848129544 ,  2924846536456
#
nums = [[1, 2], 1, 100]
new_nums = nums.copy() # shallow copy
new_new = copy.deepcopy(nums)

nums[0][0] = 1000
print("nums is {}".format(nums))
print("new_nums is {}".format(new_nums))
print("new_new is {}".format(new_new))
nums is [[1000, 2], 1, 100]
new_nums is [[1000, 2], 1, 100]
new_new is [[1, 2], 1, 100]

#@@ 18
a = ["foo","bar","baz",'bar','any','much']
indexes = [index for index in range(len(a)) if a[index] == 'bar']

rst = [i for i,j in enumerate(a) if j == 'bar']
print(rst)

#@@ 20
# list.extend(1)  #TypeError: 'int' object is not iterable
test = ["wifi", "bt",'ac',"11ax","ad"]
test[1:-1]       #['bt', 'ac', '11ax'], skip the first one and the last one
a[:-2]   # a list of everything except the last two items

#@@ 21 
print(range(10)) #range(0, 10)
print(list(range(2, 20, 3))) # Output: [2, 5, 8, 11, 14, 17]

t_str = "autom"
print(list(enumerate(t_str))) # return a list of tuples
# [(0, 'a'), (1, 'u'), (2, 't'), (3, 'o'), (4, 'm')]

print(ord('a')-ord('A')) # 32
print(chr(32)) #

#
a = list((1,))
print(type(a), a) # [1]

#
a = list(1)
# print(a)
# TypeError: 'int' object is not iterable

#@@ 23
arr = []
if not arr:  # True
    print("arr is empty")
if arr == []: # True
    print("arr == []")
if len(arr) == 0: # True
    print("len(arr) == 0")
if arr == None: # False
    print("arr == None")

#@@ 24
matrix = [[]] # matrix is NOT empty
if not matrix: # False
    print("empty row")
else: # num of row in matrix len(matrix) is  1
    print("num of row in matrix len(matrix) is ", len(matrix))

if not matrix[0]: # True
    print("empty column")  # empty column
    print(len(matrix[0]))  # 0
    

arr2 = [[1]*3 for _ in range(5)]
print(" num of row: {}\n num of column: {}".format(len(arr2), len(arr2[0])))
# num of row    len(arr2:     5
# num of column len(arr2[0]): 3

#@@ 25
matrix = []
print(len(matrix)) # 0
matrix.append([])
print(len(matrix)) # 1
matrix.append([])

print(len(matrix), len(matrix[0])) # 2, 0
matrix[0].append(2)
matrix[1].append(3)

##
matrix = [[]]
print("len of matrix ", len(matrix)) # 1
matrix.append([])
print("len of matrix ", len(matrix))  #2
matrix.append([])
print("len of matrix ", len(matrix))  # 3

##
mm = [[] for _ in range(5)]

print(len(mm), len(mm[0]))  # 5 0

#@@ 26
#

#@@ 27
ltr_str = "abcd"
ltr_list = ltr_str.split("") # ValueError: empty separator

#@@ 28
ss = "this is a test"
list_from_str = list(ss)
back_to_str = "".join(list_from_str)
print(f"list_from_str is {list_from_str}")
print(f"back_to_str is {back_to_str}")
# list_from_str is ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 't', 'e', 's', 't']
# back_to_str is this is a test

# _______________________________
# convert string to a list or a tuple
tuple("Test")
# ('T', 'e', 's', 't')

list("Station")
# ['S', 't', 'a', 't', 'i', 'o', 'n']

tuple(50,)
# TypeError: 'int' object is not iterable
list(50)
# TypeError: 'int' object is not iterable


## passing a list _________________________________________________________________________________________
wd = " "
res = wd.split(" ")
print(type(res), res)
# <class 'list'>
# ['', '']

res = wd.split()
print(type(res), res)
# <class 'list'>
# []

str = "  this is  a good book  "
str_list_1 = str.split(" ") #   ['', '', 'this', 'is', '', 'a', 'good', 'book', '', '']
str_list_2 = str.split()     #  ['this', 'is', 'a', 'good', 'book']


## 4.
# arr is a list
# func(arr): pass arr as an argument, it is like pass a reference arr, any changes to arr in func, will actually change arr.
# func(arr[1:5]): complete different!. arr[1:5] is a new list, which is a shallow copy of arr's 2nd through 6th elements
##
arr = [[1, 2, 3], [4, 5, 6], 10]
# new_list_1 is shallow copy of arr, Not completely independent of new_list
new_list_1 = arr[1:3]
# new_list_2 is an extension of shallow copy of arr
new_list_2 = arr + [8] # arr + [8] does Not modify arr

arr = [[1, 2, 3], [4, 5, 6], 10]
new_list_1 = arr + [99]
# print(f"new_list_1 is {new_list_1}") # new_list_1 is [[1, 2, 3], [4, 5, 6], 10, 99]
# print(f"arr is {arr}") # arr is [[1, 2, 3], [4, 5, 6], 10]

new_list_1[0][0] = 999
# new_list_1 is [[999, 2, 3], [4, 5, 6], 10, 99]
print(f"new_list_1 is {new_list_1}")
print(f"arr is {arr}")  # arr is [[999, 2, 3], [4, 5, 6], 10]
## 6.
#shallow copy: shifts[:] is same as copy.copy(shifts)
import copy

shifts = [3,5,9]
tmp = shifts[:]
# tmp = copy.copy(shifts)

tmp[0] = 100
# print(shifts) [3, 5, 9]

#@@1.0
# shallow copy of list
nums_lt =       [3,  [11,11,11],   [22,  22, 22],2,1]
nums_sublt = nums_lt[:3]
nums_sublt[0] = 30
nums_sublt[1] = 111
nums_sublt[2][0] = 333

# nums_sublt is [30, 111,          [333, 22, 22]]
# nums_lt is    [3,  [11, 11, 11], [333, 22, 22], 2, 1]

# shallow copy in functions
def listShallowCpy(listCpy):
    listCpy[0] =  30
    listCpy[1] = 111
    listCpy[2][0] = 333

num_lt =      [3,   [11,11,11],   [22,  22, 22],2,1]
listCpy = num_lt[:3]

listShallowCpy(listCpy)
# num_lt   is [3,   [11, 11, 11], [333, 22, 22], 2, 1]
# listCpy  is [30,  111,          [333, 22, 22]]

#@@ 1.1 list passed as an argument
arr = [[100,200],2,3,4,5]

def change_list(arr):
    arr[0][0]= 20000
    arr[1] = 999

change_list(arr[0:2]) # arr[0:2] is shallow copy of arr[0:2]; it is a new list of size 2.
print(f"arr is {arr}") # arr is [[20000, 200], 2, 3, 4, 5]

change_list(arr)  #  arr is  arr, not  a shallow copy of arr
print(f"arr is {arr}") # arr is [[20000, 200], 999, 3, 4, 5]

#-----------------------------------------------------------------------------------------
# python list

# Slicing?
a = []
len_a = len(a)
print(f"len a is {len_a}")
b = 1

a += [b]
print(a)

a.append(10)
print(a)

a.insert(1,5) # insert at loc=1
print(a)

# search
res = a.index(5)
print(res)
res = a.index(10,1)
print(res)

# sort
a.sort(reverse=True)
print(a)

#
a[1:2] = [3, 9, 6]
print(a)

#
a.pop()
print(a)
a.remove(10)
print(a)
del a[1]
print(a)

#
print(type(a[:-1]))
print(a[:-1])