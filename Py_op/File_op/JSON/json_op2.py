# {
#    "location": "NewPath",
#    "Id": "0",
#    "resultDir": "",
#    "resultFile": "",
#    "mode": "replay",
#    "className":  "",
#    "method":  "METHOD"
# }
import json, os
from datetime import datetime

## 1.
with open("relayTest.json", "r+") as jsonFile:
    data = json.load(jsonFile)

    data["location"] = "OldPath"
    jsonFile.seek(0)  # rewind
    json.dump(data, jsonFile, indent=4, sort_keys=True)
    jsonFile.truncate() # in case, new data file size is smaller

## 2.
if os.path.exists('pre_database/playlist.json'):
    with open('pre_database/playlist.json', 'r+') as f:
         playlist = json.load(f)
         # update json here
         f.seek(0)
         f.truncate()
         json.dump(playlist, f)

## 3.
try:
    with open('pre_database/playlist.json', 'r') as f:
        playlist = json.load(f)
except IOError, ValueError:
    playlist = default_playlist

playlist[key] = value  # or whatever

with open('pre_database/playlist.json', 'w') as f:
    json.dump(playlist, f)

## 4.
change = {
  "username": "abc",
  "statistics": [
    {
      "followers": 1234,
      "date": "2018-02-06 02:00:00",
      "num_of_posts": 123,
      "following": 123
    },
    {
      "followers": 2345,
      "date": "2018-02-06 02:10:00",
      "num_of_posts": 234,
      "following": 234
    }
  ]
}

def append_statistics(filepath, num_of_posts, followers, following):
  with open(filepath, 'r') as fp:
    information = json.load(fp)

  information["statistics"].append({
    "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    "num_of_posts": num_of_posts,
    "followers": followers,
    "following": following
  })

  with open(filepath, 'w') as fp:
    json.dump(information, fp, indent=2)

## 5.
# json allows duplicate keys, but how server handles duplicate keys are implementation dependent

import json
import ng as ng
from jsonpath import jsonpath
import jsonpath-ng
import requests
# Python	        JSON
# dict	            object
# list, tuple	    array
# str	            string
# int, long, float	number
# True	            true
# False	            false
# None	            null

# json_str = json.dumps(dict_type)
# json.dump(dict_type, file_write)
data_dict = {
  "name": "Ken",
  "age": 45,
  "married": True,
  "children": ("Alice","Bob"),
  "pets": ['Dog'],
  "cars": [
    {"model": "Audi A1", "mpg": 15.1},
    {"model": "Zeep Compass", "mpg": 18.1}
  ]
}

#
# Repeated key in JSON String
# RFC specifies the key name should be unique in a JSON object, but it's not mandatory.
# Python JSON library does Not raise an exception of repeated objects in JSON.
# It ignores all repeated key-value pair and considers only last key-value pair among them.
repeat_pair = '{"a":  1, "a":  2, "a":  3}'
json.loads(repeat_pair)
# {'a': 3}

## 6.


