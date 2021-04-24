import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")

response_in_dict = response.json()
print(type(response_in_dict)) # <class 'dict'>

response_in_text = response.text
print(type(response_in_text)) # <class 'str'>
print(response_in_text)

response_in_dict_1 = json.loads(response_in_text)
print(type(response_in_dict_1)) # <class 'dict'>

response_in_raw_byte = response.content
print(type(response_in_raw_byte))  # <class 'bytes'>
print(response_in_raw_byte)

# Making a HEAD request
r = requests.head('https://httpbin.org/', data={'key': 'value'})

# check status code for response recieved
# success code - 200
print(r)

# print headers of request
print(r.headers)

# checking if request contains any content
print(r.content)