import json
# Parse json to an object (dict data)
# Define JSON data
JSONData = '{"Java": "3 Credits", "PHP": "2 Credits", "C++": "3 Credits"}'

# Declare class to store JSON data into a python dictionary
class read_data:
  def __init__(self, jdata):
    self.__dict__ = json.loads(jdata)

# Assign object of the class
p_object = read_data(JSONData)

# Print the value of specific property
print(p_object.PHP) # 2 Credits
print(p_object.Java) # 3 Credits


json_string = """{"menu": {
  "id": "file",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}}"""
json_dict = json.loads(json_string)


# Save non-ASCII or Unicode data as-is not as \u escape sequence in JSON
# unicode
import json

unicodeData= {
    "string1": "明彦",
    "string2": u"\u00f8"
}
print("unicode Data is ", unicodeData)
encodedUnicode = json.dumps(unicodeData, ensure_ascii=False) # use dump() method to write it in file
print("JSON character encoding by setting ensure_ascii=False", encodedUnicode)
print("Decoding JSON", json.loads(encodedUnicode))
# unicode Data is  {'string1': '明彦', 'string2': 'ø'}
# JSON character encoding by setting ensure_ascii=False {"string1": "明彦", "string2": "ø"}
# Decoding JSON {'string1': '明彦', 'string2': 'ø'}

print("unicode Data is ", unicodeData)
encodedUnicode = json.dumps(unicodeData) # use dump() method to write it in file
print("JSON character encoding by setting ensure_ascii=False", encodedUnicode)
print("Decoding JSON", json.loads(encodedUnicode))
# unicode Data is  {'string1': '明彦', 'string2': 'ø'}
# JSON character encoding by setting ensure_ascii=False {"string1": "\u660e\u5f66", "string2": "\u00f8"}
# Decoding JSON {'string1': '明彦', 'string2': 'ø'}

# JSON Serialize Unicode Data and Write it into a file.
import json

sampleDict= {
    "string1": "明彦",
    "string2": u"\u00f8"
}
with open("unicodeFile.json", "w", encoding='utf-8') as write_file:
    json.dump(sampleDict, write_file, ensure_ascii=False)
print("Done writing JSON serialized Unicode Data as-is into file")

with open("unicodeFile.json", "r", encoding='utf-8') as read_file:
    print("Reading JSON serialized Unicode data from file")
    sampleData = json.load(read_file)
print("Decoded JSON serialized Unicode data")
print(sampleData["string1"], sampleData["string1"])

#
# Serialize Unicode objects into UTF-8 JSON strings instead of \u escape sequence
import json

# encoding in UTF-8
unicodeData= {
    "string1": "明彦",
    "string2": u"\u00f8"
}
print("unicode Data is ", unicodeData)

print("Unicode JSON Data encoding using utf-8")
encodedUnicode = json.dumps(unicodeData, ensure_ascii=False).encode('utf-8')
print("JSON character encoding by setting ensure_ascii=False", encodedUnicode)

print("Decoding JSON", json.loads(encodedUnicode))

##
# Python Escape non-ASCII characters while encoding it into JSON
import json

unicodeData= {
    "string1": "明彦",
    "string2": u"\u00f8"
}
print("unicode Data is ", unicodeData)

# set ensure_ascii=True
encodedUnicode = json.dumps(unicodeData, ensure_ascii=True)
print("JSON character encoding by setting ensure_ascii=True")
print(encodedUnicode)

print("Decoding JSON")
print(json.loads(encodedUnicode))
##
import requests
from requests.exceptions import HTTPError

try:
    response = requests.get('https://httpbin.org/get')
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    print("Entire JSON response")
    print(jsonResponse)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
