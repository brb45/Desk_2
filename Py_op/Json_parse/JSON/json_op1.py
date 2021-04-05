import json
from pprint import pprint

# The JSON data structure is essentially based on a key-value pair format.

# The keys must be string data type and
# the values data types must be in JSON data type.

# JSON supports the following data types :
# string
# number
# boolean
# null
# object
# array

# At the same time, a JSON object can contain two different data structures:
#
# An object type can contain multiple key-value pairs inside the JSON text
# An array can contain single or multiple values

# The following JSON represents some attributes of a car brand.
# The color attribute represents an array and the Model attribute represents an object in this JSON object.
"""
{
"owner": null,
"brand": "BMW",
"year": 2020,
"status": false,
"color": [
    "red",
    "white",
    "yellow"
],
"Model": {
    "name": "BMW M4",
    "Fuel Type": "Petrol",
    "TransmissionType": "Automatic",
    "Turbo Charger": "true",
    "Number of Cylinder": 4
}
}
"""
data = [{
    'wifi': 0,
    'bt': 1,
    '11ac': "Legacy",
    '11ax': {
        '11abgnac': 4
    }
},
{
    '11ax': 0,
    '11ac': 1,
    '11abgn': "Legacy",
    '11ad': {
        '11abgnac': 4
    }
}
    ]


json_string = json.dumps(data)
print(type(json_string))#string
print(json_string)
# <class 'str'>
# [{"wifi": 0, "bt": 1, "11ac": "Legacy", "11ax": {"11abgnac": 4}}, {"11ax": 0, "11ac": 1, "11abgn": "Legacy", "11ad": {"11abgnac": 4}}]
json_list = json_string.split(",")

for item in json_list:
    print(item)

print(len(json_string)) # 134

dic_data = json.loads(json_string)
print(type(dic_data)) #dict


##1. read/write data to json file
with open("dut.json", 'w') as fout:
    json.dump(data, fout, indent=5)

fname = 'dut.json'
import os
if os.path.isfile(fname):
    with open(fname, 'r') as fin:
        file_data = json.load(fin)

print(file_data)

# with open("dut.json") as fin:
#     file_data = json.load(fin)

print("-------------------------")
print(type(file_data))
for item in file_data:
    print(item)

##
# json_string = json.dumps(data_dict, indent=4, sort_keys=True)
# json.dump(data_dict, file_handle, indent=4, sort_keys=True)
# json.dump() returns None

str_formatted = json.dumps(file_data, indent=5, sort_keys=True)
print(str_formatted)
"""
[
     {
          "11ac": "Legacy",
          "11ax": {
               "11abgnac": 4
          },
          "bt": 1,
          "wifi": 0
     },
     {
          "11abgn": "Legacy",
          "11ac": 1,
          "11ad": {
               "11abgnac": 4
          },
          "11ax": 0
     }
]
"""
str_raw = json.dumps(file_data)
print(str_raw)
# [{"11ac": "Legacy", "11ax": {"11abgnac": 4}, "bt": 1, "wifi": 0}, {"11abgn": "Legacy", "11ac": 1, "11ad": {"11abgnac": 4}, "11ax": 0}]

## 2. read/write
import json
data_dict = {
  "N": "Ken",
  "A": 45,
  "Q": True,
  "C": ("Alice","Bob"),
  "CA": [
    {"M": "A", "MP": 5.1},
    {"M": "Z", "MP": 8.1}
  ]
}

with open("jsonData.json", "w") as fout:
    json.dump(data_dict, fout)
    # json.dump() returns None

with open("jsonData.json") as fin:
    a =[]
    a.append(fin.readline())
print(a)
# ['{"N": "Ken", "A": 45, "Q": true, "C": ["Alice", "Bob"], "CA": [{"M": "A", "MP": 5.1}, {"M": "Z", "MP": 8.1}]}']

with open("jsonData1.json", "w") as fout:
    json.dump(data_dict, fout, indent = 2)

with open("jsonData1.json") as fin:
    a = fin.readlines()
print(a)
# ['{\n', '  "N": "Ken",\n', '  "A": 45,\n', '  "Q": true,\n', '  "C": [\n', '    "Alice",\n', '    "Bob"\n', '  ],\n', '  "CA": [\n', '    {\n', '      "M": "A",\n', '      "MP": 5.1\n