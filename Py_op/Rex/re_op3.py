import re

# 1 re.match; the pattern must start from the beginning
# return None if not found
s = "food is on the food table"
pat1 = "foo"
res = re.match(pat1, s)
# print(type(res)) # <class 're.Match'>

res = res.group()
# print(type(res)) # <class 'str'>
# print(res) # foo

# 1.1
s = "seafood is on the food table"
pat1 = "foo"
res = re.match(pat1, s)
# print(type(res)) # <class 'NoneType'>
# print(f"res is {res}") #res is None
# res = res.group() Not working

# 1.2
m = re.match('[cr][23][dp][o2]','c3po')
# print(m.group()) #c3po




# 2. re.search: search any substring matching the pattern;
# if multiple found, return matching substring only once
s = "seafood is on the food table"
pat1 = "foo"
res = re.search(pat1, s)
# print(type(res)) # <class 're.Match'>

res = res.group()
# print(type(res)) # <class 'str'>
# print(res) # foo

# 2.1
#一个括号代表一个组
#groups返回一个元祖
s = 'abc-123-456sjls789'
pat = '(\w\w\w)-(\d\d\d)'
res = re.match(pat, s)
print(res.group()) # abc-123
print(res.group(1)) # abc
print(res.group(0)) # abc-123
print(res.group(2)) # 123

print(type(res.groups())) # <class 'tuple'>
print(res.groups()) # ('abc', '123')

pattern = "1[35678]\d{9}"
phoneStr = "1823009222300000"

result = re.match(pattern, phoneStr)
print(result.group()) # 18230092223

#
s = "\\abc"
p = r'\\abc'
res = re.match(p, s)
print(res.group()) # \abc
#
s = "\\abc"
p = '\\\\abc'
res = re.match(p, s)
print(res.group()) # \abc

#
# 定义规则匹配str="ho ve r"
# 1. 以字母开始
# 2. 中间有空字符
# 3. ve两边分别限定匹配单词边界

pattern = r"^\w+\s\bve\b\sr"
str = "ho ve r"
result = re.match(pattern, str)
print(result.group()) #ho ve r

#
pattern = r"^\w+\sve\sr"
str = "ho ve r"
result = re.match(pattern, str)
print(result.group()) #ho ve r
#
# 匹配出0-100之间的数字
# 首先:正则是从左往又开始匹配
# 经过分析: 可以将0-100分为三部分
# 1. 0        "0$"
# 2. 100      "100$"
# 3. 1-99     "[1-9]\d{0,1}$"
# 所以整合如下

pattern = r"0$|100$|[1-9]\d{0,1}$"
pattern= r"100$|[1-9]?\d{0,1}$"
pattern= r"100$|[1-9]?\d"
# 测试数据为0,3,27,100,123
for s in [str(i) for i in [0,3,27,100,123]]:
    result = re.match(pattern, s)
    try:
        print(result.group()) #
    except AttributeError as e:
        print(e)

# 0
# 3
# 27
# 100
# 'NoneType' object has no attribute 'group'

#





#
#2.2
# findall
#re.I忽略大小写，r是使用原生字符
res = re.findall(r'(th\w+)','This and that',re.I)
print(type(res)) # <class 'list'>
print(res) # ['This', 'that']

#3.1
#re.sub, re.subn
res = re.sub('X','Mr.Smith','attn:X')
print(type(res)) # <class 'str'>
print(res) # attn:Mr.Smith

res = re.sub('X','Mr.Smith','attn:X and X')
print(res) # attn:Mr.Smith and Mr.Smith

res = re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})',r'\2/\1/\3','2/20/91')
print(res) # 20/2/91