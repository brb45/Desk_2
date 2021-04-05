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
filename = "csv_data3.csv"

with open(filename, "w") as fout:
    csvWriter = csv.writer(fout)
    csvWriter.writerow(fields)
    csvWriter.writerows(rows1)

