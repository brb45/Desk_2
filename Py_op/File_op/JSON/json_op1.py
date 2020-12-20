import json
from pprint import pprint
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

with open("dut.json") as fin:
    file_data = json.load(fin)

print("-------------------------")
print(type(file_data))
for item in file_data:
    print(item)

##
# json_string = json.dumps(data_dict, indent=4, sort_keys=True)
# json.dump(data_dict, file_handle, indent=4, sort_keys=True)
# json.dump() returns None

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