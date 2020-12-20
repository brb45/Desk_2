# ch05/example1.py

import requests

url = 'https://www.yahoo.com'

res = requests.get(url)

print(res.status_code)
print(res.headers)
#print(res.text)

with open('google.html', 'w', encoding='utf-8') as f:
    f.write(res.text)

print('Done.')
