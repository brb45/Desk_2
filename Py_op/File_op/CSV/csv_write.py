import csv
# Write to csv file
# field names
fields = ["TECHNOLOGY", "FREQ_MHZ", "DATA_RATE*", "TEST*", "TX_POWER_DBM*", "ANTENNA"]

# data rows of csv file
rows1 = [['11AC',     2422,   'DSSS-1',    'E,M,P',     15.0, (1,0,0,0)],
        [  ""      ,     2457,   'CCK_5-5',    'E,M,P,S',   ""      ,"" ],
        [   ""     ,     2484,   ""      ,    "L,H,S",      ""   , ""    ]
    ]
rows2 = [['11AX',     2422,   'DSSS-1',    'E,M,P',     15.0, (1,0,0,0)],
        [            2457,   'CCK_5-5',    'E,M,P,S',   ""      ,"" ],
        [             2484,   ""      ,    "L,H,S",      ""   , ""    ]
    ]
# name of csv file
filename = "csv_data2.csv"
# writing to csv file
with open(filename, 'w') as fout:
    csvWriter = csv.writer(fout)
    # writerow(single_list)
    csvWriter.writerow(fields)

    # writerows(a list of lists)
    csvWriter.writerows(rows1)
    csvWriter.writerows(rows2)


#
# with open(filename,"r") as fin_in:
#     csv_reader = csv.reader(fin_in)
#     for line in csv_reader:
#         print(line)
#         #print(type(line))
#         for wd in line:
#             if wd == "":
#                 print('quote', end=" ")
#             else:
#                 print(wd, end=" ")
#         print()

