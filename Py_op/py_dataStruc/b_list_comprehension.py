from pprint import pprint
# 1.
l = [1,2,3,4,5]
l_1 = [ x+1 for x in l]
# print(l_1) # [2, 3, 4, 5, 6]

#2.
vec = [[1,2,3], [4,5,6], [7,8,9]]
flattened = [ num for row in vec for num in row]
# print(flattened)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

#3. filtering
a = [1,2,3,4,5,6,7,8]
evens = [v for v in a if v %2 == 0]
print(evens)

# 4
res = [ (x,y) for x in [1,2,3] for y in [4,5,6]]
# pprint(res)
# [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]

# 5.
matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
res = [[ row[i] ]  for row in matrix for i in range(4)]
# pprint(res)
# [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]]

matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]] # 3 x 4
res = [ [row[i] for row in matrix] for i in range(4)]
# pprint(res)
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

#
import math
prime_nums = [ p for p in range(2,100) if 0 not in [p%d for d in range(2, math.ceil(math.sqrt(p)))] ]
# print(prime_nums)
# [2, 3, 4, 5, 7, 9, 11, 13, 17, 19, 23, 25, 29, 31, 37, 41, 43, 47, 49, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]