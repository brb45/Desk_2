import requests
import pprint, json

resp = requests.get("http://www.google.com")

print(type(resp))
print("response content: ")
print(resp.text, "\n")

print(resp.ok)           # => True
print(resp.status_code)  # => 200
print(resp.headers['content-type'])

python_data = resp.json()
json_string = json.dumps(python_data)
print(json_string)

###
django.http.request.HttpRequest
request.method




