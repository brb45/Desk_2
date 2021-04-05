##1. read a csv file with basci file ops
# num of columns in csv is # of commas + 1
file_name =  "format.csv"
with open(file_name, 'r') as fin:
    res = []
    for ln in fin:
        ln = ln.rstrip("\n")
        ln = ln.split(",")
        res.append(ln)
from pprint import pprint
pprint(res)



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

with open('csv_data.csv', 'w') as fout:
    for line in res:
        line = ",".join(line)
        fout.write(line+"\n")

with open('csv_data.csv', 'r') as fin:
    result = []
    for line in fin:
        line = line.rstrip("\n")
        line = line.split(",")
        result.append(line)
pprint(result)
# [['1', '2', '3', '4'],
#  ['1', '2', '3', '9'],
#  ['', '2', '3', '4'],
#  ['1', '2', '3', ''],
#  ['1', '', '3', '4'],
#  ['1', '2', '', ''],
#  ['', '', '3', '4'],
#  ['1', '', '', '4']]
assert result == res