print((lambda : 100)())

from collections import defaultdict

dic = defaultdict(lambda: defaultdict(int))

print(dic["key"]["2nd_key"]) # 0

dic1 = defaultdict(lambda: defaultdict(list))
print(dic1["key"]["2nd_key"])  # []