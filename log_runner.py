from collections import Counter
dic = {}
dic1 = Counter()

nums = [('a', 11), ('b', 200)]
nums1 = ['a' , 'b', 'c']
dic1.update(nums1)
print(dic)
s = str(dic)
print(len(str(dic)))

# for i, v in enumerate(s):
#     print(i,f'[{v}]')
print(dic1)
dic1.update(('a', 10))
print(dic1)
# Counter({'a': 1, 'b': 1, 'c': 1})
# Counter({'a': 2, 'b': 1, 'c': 1, 10: 1})
