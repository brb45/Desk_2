import csv
#
from pprint import pprint
file_name = "csv_data1.csv"
with open(file_name, "r") as infile:
    csvReader = csv.reader(infile) #<type '_csv.reader'>
    #title_line = next(csvReader) # ['Test_ID', 'Val']
    content = []
    for row in csvReader:
        #print(type(row)) # list, each line does not end with "\n"
        print(row)
        content.append(row)
    # ['Test_ID', 'Val', '', '', '', '', '']
    # ['1', '100', '100', '100', '100', '100', '100']
    # ['2', '200', '200', '200', '200', '200', '200']
    # ['3', '300', '300', '300', '300', '300', '300']


    # pprint(content)
    print(f"Total no. of rows: {csvReader.line_num}")





"""
[['Test_ID', 'Val', '', '', '', '', ''],
 ['1', '100', '100', '100', '100', '100', '100'],
 ['2', '200', '200', '200', '200', '200', '200'],
 ['3', '300', '300', '300', '300', '300', '300']]

"""