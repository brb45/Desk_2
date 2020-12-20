from urllib.request import urlopen
response = urlopen("http://www.litepoint.com")
print(response)
#for line in response.readlines():
    #print(line)
    #pass
#print(response.readline())
#http.client.HTTPResponse
print(response.url)
print(response.status)

import urllib.error
try:
    urlopen("http://www.ietf.orfg")
except urllib.error.HTTPError as e:
    print("status", e.code)
    print("reason", e.reason)
    print("url", e.url)
except urllib.error.URLError as e:
    #print("status", e.code)
    print("reason", e.reason)
    #print("url", e.url)


