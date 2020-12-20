import requests
import json
# https://api.github.com/search/repositories?q=requests%2Blanguage%3Apython
url = "https://api.nasa.gov/planetary/apod"
param={"api_key": "DEMO_KEY", "date": "2019-04-11"}
# headers = {"content-type": "application/json"}
response = requests.get(
    url,
    params=param,
    # headers= headers
)


print(response.request.url)
# https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=2019-04-11

print(response.encoding)
# utf-8

print(response.url)
# https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=2019-04-11

print(response.status_code)
# 200

print(response.request.headers)
# {'User-Agent': 'python-requests/2.25.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

with open('headers1.json', 'w') as fout:
    json.dump(dict(response.headers), fout, indent=4)
# print(type(response.headers))
# <class 'requests.structures.CaseInsensitiveDict'>

with open('body3.json', 'w') as fout:
    # json.dump(response.text, fout, indent = 3) # NOT good
    text_string = response.text
    python_dict = json.loads(text_string)
    json.dump(python_dict, fout, indent = 3)
# print(response.json())
with open('body_4.json', 'w') as fout:
    json.dump(response.json(), fout, indent = 3)

with open('body5.txt', 'w', encoding='utf-8') as fout:
    fout.write(response.text)