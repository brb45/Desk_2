import io

stream  = io.StringIO()

stream.write("QA automation test runs Jenkins.\n")
print("Automation runs on daily build", file=stream)

contents = stream.getvalue()
print(contents)
stream.close()

##
with io.StringIO() as stream:
    stream.write("QA automation starts with daily build test.\n")
    print("Use mysql database", file=stream)
    contents = stream.getvalue()
    print(contents)

import requests

urls = {
    'get': 'https://httpbin.org/get?title=learn+python+programming',
    'headers': 'https://httpbin.org/headers',
    'ip': 'https://httpbin.org/ip',
    'now': 'https://now.httpbin.org/',
    'user-agent': 'https://httpbin.org/user-agent',
    'UUID': 'https://httpbin.org/uuid',
}

# def get_content(title, url):
#     resp = requests.get(url)
#     print(f'Response for {title}')
#     print(resp.json())
#
# for title, url in urls.items():
#     get_content(title, url)
#     print('-' * 40)

from pprint import pprint
url = 'https://httpbin.org/post'
data = dict(title='Learn Python Programming')

resp = requests.post(url, data=data)
print('Response for POST')
pprint(resp.json())