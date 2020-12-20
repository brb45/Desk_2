import requests
import json
import jsonpath

# 8/31/20
# 12/2/20

# An OpenAPI file allows you to describe your entire API, including:
#
# Available endpoints (/users) and operations on each endpoint (GET /users, POST /users)
# Operation parameters Input and output for each operation
# Authentication methods
# Contact information, license, terms of use and other information.

# requests inputs:
# 1.   query string:   params  = {}
# 2.   headers:        headers = {}
# 3.   form:           data    = {}
# 3.1  json            json
# 4.   Auth:           auth=("brb45","zh" )
# 5.   timeout         timeout=1
# 6.   upload file     files={'file', file_handle}
# 7.   download file   stream = True , r.iter_content

#@@ 1.
# https://api.github.com/search/repositories?q=requests%2Blanguage%3Apython
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

# response.content -> raw bytes
# response.text   --> json string, body only
# response.json()  --> python dict,
# json.loads(response.text) --> python dict

# response.encoding = "utf-8" , Unicode Transformation Format
# response.headers --> NOT python dict, <class 'requests.structures.CaseInsensitiveDict'>
# response.url
# response1.request.url
# response.status_code
#
# print(response.request)
# <PreparedRequest [GET]>
# response.request.headers #dictionary
# response.request.headers["content-type"]  #  applications/json


response = requests.post('https://httpbin.org/post', json={'key':'value'})
# response.request.headers['Content-Type']
# 'application/json'
# response.request.url   # 'https://httpbin.org/post'

# response.request.body
# b'{"key": "value"}'
# for GET: response.request.body returns None

# pass by the bytes
requests.get(
     'https://api.github.com/search/repositories',
     params=b'q=requests+language:python',
 )

# customize headers
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

# print(response.headers)
# for key in response.headers:
#     print(key)
# print(response.headers["Accept"])


#@@ 2.
## Basic Methords
response_post = requests.post('https://httpbin.org/post', data={'key':'value'})
response_put  = requests.put('https://httpbin.org/put', data={'key':'value'})

response_delete = requests.delete('https://httpbin.org/delete')

response_head = requests.head('https://httpbin.org/get')
# print(response_head)  <Response [200]>

response_patch = requests.patch('https://httpbin.org/patch', data={'key':'value'})

response_options =  requests.options('https://httpbin.org/get')


# data takes dict, list of tuples, bytes, and file.
# payload is passed in the message body for post, put, and patch

# get: can pass data in query string-- params


#@@ 3.
# Authentication

from getpass import getpass
res_auth = requests.get('https://api.github.com/user', auth=("brb45","zh" ), timeout=1)
res_auth = requests.get('https://api.github.com/user', auth=('username', getpass()))
# print(res_auth.status_code)

from requests.auth import HTTPBasicAuth
requests.get(
     'https://api.github.com/user',
     auth=HTTPBasicAuth('username', getpass())
 )
print(res_auth.status_code) # 200
print(res_auth.url)    # https://api.github.com/user
print(res_auth.encoding) # utf-8


import requests
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['X-TokenAuth'] = f'{self.token}'  # Python 3.6+
        return r


requests.get('https://httpbin.org/get', auth=TokenAuth('12345abcde-token'))


#Passing Parameters In URLs
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
# print(r.url) # https://httpbin.org/get?key1=value1&key2=value2

##
# Binary Response Content
# You can also access the response body as bytes, for non-text requests:
#
# >>> r.content
# b'[{"repository":{"open_issues":0,"url":"https://github.com/...


##
# There’s also a builtin JSON decoder, in case you’re dealing with JSON data:
#
# >>> import requests
#
# >>> r = requests.get('https://api.github.com/events')
# >>> r.json()
# [{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...
#

##
# print(f"r.cookies is {r.cookies}")  r.cookies is <RequestsCookieJar[]>
# print(f"r.cookies is {r.cookies["cookie_name"]}")

#@@ 4.
#@@ Upload a file
#!/usr/bin/env python3

import requests as req

url = 'http://localhost:5000/upload'

with open('sid.jpg', 'rb') as f:

    files = {'image': f}

    r = req.post(url, files=files)
    print(r.text)

# upload a file
response = requests.post("https://httpbin.org/post", files={'file': open('nasa_black_hole.png', 'rb')})


#@@ 5.
## Download a file ex1
url = "https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.0.7.tar.xz"
with requests.get(url, stream=True) as response:
    with open("latest-kernel.tar.xz", "wb") as tarball:
        for chunk in response.iter_content(16384):
            tarball.write(chunk)

#@@ Streaming the data as download
#!/usr/bin/env python3
import requests as req
url = "https://docs.oracle.com/javase/specs/jls/se8/jls8.pdf"

local_filename = url.split('/')[-1]

r = req.get(url, stream=True)

with open(local_filename, 'wb') as f:

    for chunk in r.iter_content(chunk_size=1024):

        f.write(chunk)

#@@ 6. Use api key
#
response = requests.get("https://api.nasa.gov/planetary/apod", params={"api_key": "DEMO_KEY", "date": "2019-04-11"})
# returns an instance of the requests.models.Response class.
# response.json() --> json-encoded content of the response
# response.reason --> 'OK'
# response.status_code
# response.headers


# Sessions
# The requests library allow us to use sessions: when requests are sent from a session context,
# cookies are preserved between one request and another. This is the recommended way of performing
# multiple requests to the same host, since even the same TCP connection will be reused.
session = requests.Session()
response = session.get("https://httpbin.org/cookies/set?lastname=skywalker")


# Performance
# When using requests, especially in a production application environment, it’s important to consider
# performance implications. Features like timeout control, sessions, and retry limits can
# help you keep your application running smoothly.
#
# Timeouts
# When you make an inline request to an external service, your system will need to wait upon the response before
# moving on. If your application waits too long for that response, requests to your service could back up,
# your user experience could suffer, or your background jobs could hang.

# By default, requests will wait indefinitely on the response, so you should almost always specify a timeout
# duration to prevent these things from happening. To set the request’s timeout, use the timeout parameter.
# timeout can be an integer or float representing the number of seconds to wait on a response before timing out:
#

requests.get('https://api.github.com', timeout=1) # timeout in sec.
# <Response[200] >
requests.get('https://api.github.com', timeout=3.05)
# <Response[200] >

# JSON only allows key names to be strings. Those strings can consist of numerical values.
with open("src1.json", "r") as fin:
    json_input_str = fin.read()
    # print(f"type: {type(json_input_str)}\n  {json_input_str}")
    # type: <class 'str'>
    # {
    #     "name": "morpheus",
    #     "job": "leader"
    # }
    req_json = json.loads(json_input_str)
    # print(f"type: {type(req_json)}\n  {req_json}")
    # type: <class 'dict'>
    # {'name': 'morpheus', 'job': 'leader'}
    response = requests.post(url, req_json)
    # print(response.status_code) # 201
    # print(response.content)
    # b'{"name":"morpheus","job":"leader","id":"530","createdAt":"2019-12-12T19:41:32.341Z"}'

    ##
    content_len = response.headers.get("Content-Length")
    response_json = json.loads(response.text)
    # print(f"\nresponse_json from POST is {response_json}\n")
    # response_json
    # from POST is {'name': 'BRCM_4389', 'job': '11AX on MW-7G', 'id': '598', 'createdAt': '2019-12-12T22:09:57.259Z'}

    id = jsonpath.jsonpath(response_json, 'id')
    # print(f"id is {id[0]}")  # id is 716
    createdAt= jsonpath.jsonpath(response_json,"createdAt")
    # print(f"createdAt is {createdAt[0]}")  # createdAt is 2019-12-13T22:37:08.370Z


##
# curl -H 'Accept: application/json' -H 'X-Api-Token: your-api-token' https://yoursubdomain.deploybot.com/api/v1/users
# curl -H 'Accept: application/json' https://yoursubdomain.deploybot.com/api/v1/users?token=your-api-token