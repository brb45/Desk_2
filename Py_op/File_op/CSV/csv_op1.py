##1. read a csv file with basci file ops
# num of columns in csv is # of commas + 1
file_name =  "C:\\Users\jsun\Documents\Desk_1\Py_op\File_op\\format.csv"
with open(file_name) as fin:
    res = []
    for line in fin:
        line = line.rstrip("\n")
        line = line.split(",")
        res.append(line)
        print(line)

# ['1', '2', '3', '4']
# ['1', '2', '3', '4']
# ['', '2', '3', '4']
# ['1', '2', '3', '']
# ['1', '', '3', '4']
# ['1', '2', '', '']
# ['',  '', '3', '4']
# ['1', '', '',  '4']

# 1,2,3,4
# 1,2,3,4
#  ,2,3,4
# 1,2,3,
# 1, ,3,4
# 1,2, ,
#  , ,3,4
# 1, , ,4

res[1][3] = '9'
from pprint import pprint
pprint(res)
# [['1', '2', '3', '4'],
#  ['1', '2', '3', '9'],
#  ['', '2', '3', '4'],
#  ['1', '2', '3', ''],
#  ['1', '', '3', '4'],
#  ['1', '2', '', ''],
#  ['', '', '3', '4'],
#  ['1', '', '', '4']]