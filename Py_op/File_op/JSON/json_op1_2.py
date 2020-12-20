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
print(type(data))
##1. read/write data to json file
with open("json_op1.json", 'w') as fout:
    json.dump(data, fout, indent=5)

with open("json_op1.json") as fin:
    file_data = json.load(fin)

print("-------------------------")
print(type(file_data))
for item in file_data:
    print(item)