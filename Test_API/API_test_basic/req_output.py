import requests
import json
# https://api.github.com/search/repositories?q=requests%2Blanguage%3Apython
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)


print(response.request.url)
# https://api.github.com/search/repositories?q=requests%2Blanguage%3Apython

print(response.encoding)
# utf-8

print(response.url)
# https://api.github.com/search/repositories?q=requests%2Blanguage%3Apython

print(response.status_code)
# 200

print(response.request.headers)
# {'User-Agent': 'python-requests/2.25.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

with open('headers.json', 'w') as fout:
    json.dump(dict(response.headers), fout, indent=4)
# print(type(response.headers))
# <class 'requests.structures.CaseInsensitiveDict'>

with open('body.json', 'w') as fout:
    # json.dump(response.text, fout, indent = 3) # NOT good
    text_string = response.text
    python_dict = json.loads(text_string)
    json.dump(python_dict, fout, indent = 3)
# print(response.json())
with open('body_1.json', 'w') as fout:
    json.dump(response.json(), fout, indent = 3)

with open('body2.txt', 'w', encoding='utf-8') as fout:
    fout.write(response.text)