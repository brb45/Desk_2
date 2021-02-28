#  nums = str(100).split('')
# ValueError: empty separator

#@@ 1. # chr vs ord
# str vs int

a = 'ab'
# print(chr(1)) # not working, 1 is not a valid int for a char.
# print(type(chr(1)) # not working

# print(ord('a')) # 97
# print(chr(97))  # a

#@@ 1.1
# Do Not support string math
a = 'a'
b = 'A'
# c = a - b
# TypeError: unsupported operand type(s) for -: 'str' and 'str'
print(ord(a) - ord(b)) # 32

#@@ 2. int(), float() , str(valid int or float number)
# str works on primitive
ab = 100
c = str(100) # str(int), turns an int to a string
# print(type(c), " and ", c) # <class 'str'>  and  100

# int(string) ==> int of base 10
# int(binary_string, base) == > int of base 10
c = "100"
cc = int(c)  
# print("type of cc is {} and cc is {}".format(type(cc), cc))
# type of cc is <class 'int'> and cc is 100

#
a = "111" # Binary string
print(int(a, 2))  # 7

a = "A"  # hex number
print(int(a, 16))   # 10

a = "101" # oct number
int(a, 8) # 65
#

# string = "123U"
# num = int(string) ValueError: invalid literal for int() with base 10: '123U'

# #
float_num=128.8
int(float_num) # 128

# int("128.8")
# ValueError: invalid literal for int() with base 10: '128.8'

str(128.8) # '128.8'
float('128.8') # 128.8
print(5/2.2)  # 2.2727272727272725

#@@ 3.
raw = r'this\t\n and that'
# print(raw)  # this\t\n and that

## 4. string operation

# reverse a string
myString = '1234567890'
# print(myString[::-1]) #0987654321

#------------------------------------------
## 4.1
# s is a string
s.isalpha()
s.isnumeric()
s.isdigit()
s.isalnum()
s.isspace()

s.islower()
s.isupper()
s.isdecimal()

# ignore non-alphabetic chars
# s.lower()
# s.upper()
# s.islower()
# s.isupper():

# -- returns the lowercase or uppercase version of the whole string
st = "Hope You Find It"
stt = st.lower() # convert the whole string to lower case
# print(stt) #  hope you find it
sttt = stt.upper() # convert the whole string to upper case
# print(sttt) #  HOPE YOU FIND IT

str_word = "this is # of day"
# print(str_word.islower())  True
# print(str_word.upper())    THIS IS # OF DAY

#@@ 5. count
s.count(substr, start, end)
# Does not count overlapping substrings.
cnt_count='foooo'
#
cnt_count.count('oo') # 2
cnt_count.count('o', 1) # 4
cnt_count.count('a')  # 0

## 6. find vs rfind
s.find(substr, start, end)
    # search substr in range[start_pos, end_pos), excluding end_pos
    # returns the first index where it begins or -1 if not found
s.rfind(substr, start, end)

ss='foo goo foo goo'
ss.find('foo') # 0

ss.rfind('foo') # 8
ss.rfind('foo', 5)  # 8

#@@ 6.
s.startswith('other')
s.endswith('other')
# -- tests if the string starts or ends with the given other string

##--------------------------------------------------------------
#@@ 7. strip() return a string
# strip(chars): remove all chars cumulatively from front and back
# strip(): remove all the white space from front and back
s.lstrip(chars)
s = "   foo goo   "
# Trims leading chars
# __________________________________________________________________
# s.rstrip(chars)
# trims trailing chars
#     In[29]: "   foo goo   ".rstrip(" o")
#     Out[29]: '   foo g'
#____________________________________________________________________
# s.strip(chars)
# strip both leading and trailing
s = "   foo goo   "
print([s.lstrip()]) # ['foo goo   ']

s = "  \n foo \n goo \n "
print([s.lstrip()]) # ['foo \n goo \n ']

# strip does not strip the pattern "fao"
# but strip any of the char in the sub-string
# Only strip from beginning, ending or both direction
s = "foogaoo hpp jkk ".lstrip("fao")
print([s])  # ['gaoo hpp jkk ']

s = "abc abc "
ss = s.strip('a b c')
print([ss]) # ['']

##--------------------------------------------------------##
#@@ 8.
# s.split(sep=None, maxsplit=-1) # return a list
#  -- returns a list of substrings separated by the delimiter.
 ##   it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc'].
 #   As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
 #  return a list of one element if no delim found in the string

ss = "a b c d"
print(ss.split(maxsplit=1))
# ['a', 'b c d']
print(ss.split(maxsplit=2))
# ['a', 'b', 'c d']

ltr_str = "abcd"
ltr_list = ltr_str.split()
print(ltr_list)  # ['abcd']

# ltr_list_error = ltr_str.split("") # ValueError: empty separator


word = "\nthis is first page\nthis is 2nd page\nthis is third page\n"
word.split("\n") #['', 'this is first page', 'this is 2nd page', 'this is third page', '']
word.splitlines()#['', 'this is first page', 'this is 2nd page', 'this is third page']

word = "\nthis is first page\n\nthis is 2nd page\n\nthis is third page\n"
wd = word.split("\n")       # ['', 'this is first page', '', 'this is 2nd page', '', 'this is third page', '']
wd_1 = word.splitlines()    # ['', 'this is first page', '', 'this is 2nd page', '', 'this is third page']

word1 = "    1  2  3  "
word1.split()  # ['1', '2', '3']
word2=" \n   1 \n 2  3 \n"
word2.split()  # ['1', '2', '3']
word2.split('\n')  # [' ', '   1 ', ' 2  3 ', '']
wd1 = "\n"
# print(wd1.split())  # []
wd2 = "aaaa"
# print(wd2.split('a')) # ['', '', '', '', '']
wd3 = "         "
# print(wd3.split())  # []
wd4 = "  \n   \n    "
# print(wd4.split())  # []

word3="this, is,a,book, "
word3.split(',')
# ['this', ' is', 'a', 'book', ' ']

word4="this, is,a,book,"
word4.split(',')
# ['this', ' is', 'a', 'book', '']

word4.split(',', maxsplit=2)
# ['this', ' is', 'a,book,']

word4.split(',', maxsplit=3)
# ['this', ' is', 'a', 'book,']

word4.split('8')
# ['this, is,a,book,']

ss = "aba"
s = ss.split('a')
# print(s, len(s))
# ['', 'b', ''] 3
#
#@@ 7.
# s.partition(< sep > )
# Return a tuple

# s.partition( < sep > ) splits s at the first occurrence of string < sep > .
# The return value is a three-part tuple consisting of:

# The portion of s preceding < sep >
# < sep > itself
# The portion of s following < sep >
#
'foo.bar'.partition('.')
# ('foo', '.', 'bar')
#
'foo.bar'.partition('..')
# ('foo.bar', '', '')

print("j#k".partition("u"))
# ('j#k', '', '')

word = 'foo.bar.candy'
wd = word.partition('.') # ('foo', '.', 'bar.candy')

#@@  8.
# #_______________________________________________________________
# s.join( < iterable > )
# iterable must ba an iterable of strings
# Concatenates strings from an iterable,
# returns a string
#
# #joins a list of strings with s
'---'.join(['aaa', 'bbb', 'ccc'])
# -> aaa---bbb---ccc
# s = ','
pp=s.join(["catch", "a", "cold"])
# 'catch,a,cold'

#
'---'.join(['foo', 23, 'bar'])
# TypeError: sequence item 1: expected str instance, int found

w1 = "---".join({'a','c','b'})
# print(w1)
# w1 is random: a---c---b, or a---b---c, c---a---b ...

w1 = "---".join({'a'})
print(w1) # 'a'

ss = '---'.join(['aaa'])
print(ss) # aaa
#@@  9.

# ____________________________________________________________________
# s.replace(old, new, count)
#  -- returns a string where all occurrences of 'old' have been replaced by 'new'

# count – the number of times you want to replace the old substring with the new substring. (Optional )
# if "old" is not found, no replacement happens

s = "  abc dkd "
old = " "
new = 'A'
count = 10
res = s.replace(old, new, count)
print(res)  #   AAabcAdkdA

# #_______________________________________________________________
# s[1:4] #is 'ell' #-- chars starting at index 1 and extending up to but not including index 4
# s[1:] #is 'ello' #-- omitting either index defaults to the start or end of the string
# s[:] #is 'Hello' -- omitting both always gives us a copy of the whole thing
#     #(this is the pythonic way to copy a sequence like a string or list)
# s[1:100] #is 'ello' -- an index that is too big is truncated down to the string length
#
# s[-1] # 'o' -- last char (1st from the end)
# s[-4] # 'e' -- 4th from the end
# s[:-3] # 'He' -- going up to but not including the last 3 chars.
# s[-3:] # 'llo' -- starting with the 3rd char from the end and extending to the end of the string.
#
# print("this is \x61 \ngood example")
# print(r"this is \x61 \ngood example")
# this is a
# good example
# this is \x61 \ngood example
#
# t_str = "automation test"
# t_enum = list(enumerate(t_str))
# print(type(t_enum)) #<class 'list'>
# print(t_enum) #[(0, 'a'), (1, 'u'), (2, 't'), (3, 'o'), (4, 'm'), (5, 'a'), (6, 't'), (7, 'i'), (8, 'o'), (9, 'n'), (10, ' '), (11
#
# print(":".join("abc")) #a:b:c

# str.strip([set of chars])
string = '   xoxo love xoxo    '
# print("string is {}, len is {}".format(string, len(string)))
# string is    xoxo love xoxo    , len is 21

str1 = string.strip()
#removed 3 leading spaces and 4 trailing spaces
# print("str1 is {}, len is {}".format(str1, len(str1)))
# str1 is xoxo love xoxo, len is 14

str2= string.strip('xoxo')
# # Nothing is removed
print("str2 is {}, len is {}".format(str2, len(str2)))
# # str2 is    xoxo love xoxo    , len is 21

str3= string.strip(' xoxo')
# #
print("str3 is {}, len is {}".format(str3, len(str3)))
# # str3 is love, len is 4

data = "wiiwnter"
print(data.strip("iw")) #nter

data1 ="appointment"
print(data1.strip("pa"))  #ointment

s = 'a'
ss = s.split('a')
print(ss) # ['', '']

rst = s.split('aa')
print(rst) # ['a']

s = 'aaaa'
rst = s.split('a')
print(rst) # ['', '', '', '', '']
# split of 'aaaa', type <class 'list'>, 5, ['', '', '', '', '']

ss = 'aaaa'
st = ss.split('aa')
print(st)

ss = ''
rst = ss.split()
# split of '', type <class 'list'>, 0, []

ss = ''
rst = ss.split(";")
print(rst) # ['']

ss = ' '
rst = ss.split(' ')
# split of ' ', type <class 'list'>, 2, ['', '']

ss = '  '
rst = ss.split()
print(rst) # []

ss = ' a   b   c \n '
rst = ss.split()
#  ['a', 'b', 'c']

test_dict = {'Gfg': 1, 'is': 2, 'best': 3, 'for': 4, 'CS': 5}

# initializing Remove keys
rem_list = ['is', 'for', 'CS']

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

rem_str = str(rem_list)
print(f"Type of rem_str is {type(rem_str)}")
print(rem_str)
# Type of rem_str is <class 'str'>
# ['is', 'for', 'CS']

dict_str = str(test_dict)
print(f"dict_str is {dict_str}") # {'Gfg': 1, 'is': 2, 'best': 3, 'for': 4, 'CS': 5}