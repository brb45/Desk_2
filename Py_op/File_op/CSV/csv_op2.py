import csv
#
from pprint import pprint
file_name = "C:\\Users\jsun\Documents\Desk_1\Py_op\File_op\CSV\data_set1.csv"
with open(file_name, "r") as infile:
    csvReader = csv.reader(infile) #<type '_csv.reader'>
    #title_line = next(csvReader) # ['Test_ID', 'Val']
    content = []
    for row in csvReader:
        #print(type(row)) # list, each line does not end with "\n"
        content.append(row)
    pprint(content)
    print(f"Total no. of rows: {csvReader.line_num}")
"""
[['Test_ID', 'Val', '', '', '', '', ''],
 ['1', '100', '100', '100', '100', '100', '100'],
 ['2', '200', '200', '200', '200', '200', '200'],
 ['3', '300', '300', '300', '300', '300', '300']]

"""