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