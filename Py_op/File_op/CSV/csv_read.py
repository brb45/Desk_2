import csv
from pprint import pprint
file_name = "csv_data1.csv"

with open(file_name) as fin:
    res = []
    csvReader = csv.reader(fin)
    for line in csvReader:
        print(line)
        res.append(line)

    print(csvReader.line_num)

# ['Test_ID', 'Val', '', '', '', '', '']
# ['1', '100', '100', '100', '100', '100', '100']
# ['2', '200', '200', '200', '200', '200', '200']
# ['3', '300', '300', '300', '300', '300', '300']
# 4
print("--------------------------------------")
pprint(res)

"""
[['Test_ID', 'Val', '', '', '', '', ''],
 ['1', '100', '100', '100', '100', '100', '100'],
 ['2', '200', '200', '200', '200', '200', '200'],
 ['3', '300', '300', '300', '300', '300', '300']]
"""

print("--------------------------------------")
with open(file_name) as fin:
    res = fin.readlines()

print(res)
# ['Test_ID,Val,,,,,\n', '1,100,100,100,100,100,100\n', '2,200,200,200,200,200,200\n', '3,300,300,300,300,300,300\n']
