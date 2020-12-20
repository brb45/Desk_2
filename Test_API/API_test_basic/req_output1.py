import requests
import json
# https://api.github.com/search/repositories?q=requests%2Blanguage%3Apython

headers = {"content-type": "application/json"}
r = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers= headers
)

print(json.dumps(dict(r.request.headers), indent=3))
# {
#    "User-Agent": "python-requests/2.25.0",
#    "Accept-Encoding": "gzip, deflate",
#    "Accept": "*/*",
#    "Connection": "keep-alive",
#    "content-type": "application/json"
# }

headers = {"content-type": "application/json"}
r = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    # headers= headers
)

print(json.dumps(dict(r.request.headers), indent=3))
# {
#    "User-Agent": "python-requests/2.25.0",
#    "Accept-Encoding": "gzip, deflate",
#    "Accept": "*/*",
#    "Connection": "keep-alive"
# }
# print(r.request.headers["content-type"]) KeyError: 'content-type'

print(requests.head)