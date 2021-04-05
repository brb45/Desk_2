import csv

# my data rows as dictionary objects
test_1 = [{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil',  'year': '2'},
          {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
          {'branch': 'IT',  'cgpa': '9.3', 'name': 'Aditya',  'year': '2'},
          {'branch': 'SE',  'cgpa': '9.5', 'name': 'Sagar',   'year': '1'},
          {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
          {'branch': 'EP',  'cgpa': '9.1', 'name': 'Sahil',   'year': '2'}]

test_v = []
dict_1 = dict([("Tech", ["wifi", "wifi_mps", "AX_mps", "RSDB"]), ("API", ["EVM", "TX_Power", "PER", "RX_Sens", "Mask",])])
dict_4 = dict([("API", ["EVM", "TX_Power", "PER", "RX_Sens", "Mask",]), ("RU", [5, 10, 15,25,40,80])])
dict_2 = dict([("Freq", [2412, 2437, 2482, 5180])])
dict_3 = dict([("Data_rate", [6, 9 , 48, 54, 216])])
dict_5 = dict([("RU", [0, 37, 53,61,65,67])])


test_v.append(dict_1)
test_v.append(dict_2)
test_v.append(dict_3)
test_v.append(dict_4)
test_v.append(dict_5)
# test_v.append(dict_1)
# print(test_v)

# field names
fields = ['Tech', 'API', 'Freq', 'Data_rate', "RU"]
# name of csv file
filename = "dict_write.csv"

with open(filename, "w") as fin:
    # csv_writer = csv.writer(fin)
    # csv_writer.writerow(fields)

    csv_writer = csv.DictWriter(fin, fieldnames=fields)
    csv_writer.writeheader()
    csv_writer.writerows(test_v)

# Tech,API,Freq,Data_rate,RU
#
# "['wifi', 'wifi_mps', 'AX_mps', 'RSDB']","['EVM', 'TX_Power', 'PER', 'RX_Sens', 'Mask']",,,
#
# ,,"[2412, 2437, 2482, 5180]",,
#
# ,,,"[6, 9, 48, 54, 216]",
#
# ,"['EVM', 'TX_Power', 'PER', 'RX_Sens', 'Mask']",,,"[5, 10, 15, 25, 40, 80]"
#
# ,,,,"[0, 37, 53, 61, 65, 67]"

# dict_1 = dict([("Tech", ["wifi", "wifi_mps", "AX_mps", "RSDB"])])
# dict_4 = dict([("API", ["EVM", "TX_Power", "PER", "RX_Sens", "Mask",])])
# dict_2 = dict([("Freq", [2412, 2437, 2482, 5180])])
# dict_3 = dict([("Data_rate", [6, 9 , 48, 54, 216])])
# dict_5 = dict([("RU", [0, 37, 53,61,65,67])])