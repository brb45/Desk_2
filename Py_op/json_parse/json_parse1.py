
# I have been try to find the best way to search a particular value and extract the data.
"""
    {"family": {
    "name": "Mary",
    "age": "32",
    "sex": "female",
    "kids": [
      {
        "name": "jim",
        "age": "10",
        "sex": "male",
        "dob_year": "2007",
        "ssn": "123-23-1234"
      },
      {
        "name": "jill",
        "age": "6",
        "sex": "female",
        "dob_year": "2011",
        "ssn": "123-23-1235"
      }]}}
"""
# if i needed to search "ssn" containing "1234" and return the "name" "jim"
# what would be the best way to go about achieving this?
# 1.
import json
js = '''your json text data'''
j = json.loads(js)

for items in j['family']['kids']:
    if '1234' in items['ssn']:
        print(items['name'])
#2.
with open('data.json') as json_file:
    data = json.load(json_file)
    for kid in data['family']['kids']:
        if '1234' in kid['ssn']:
            print(kid['name'])
#3.