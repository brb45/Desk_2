import requests, json


url = 'https://api.github.com/search/repositories'
parameters = {'q': 'requests+language:python'}
headers={'Accept': 'application/vnd.github.v3.text-match+json'}

# get
response = requests.get(url, params=parameters, headers=headers)
res_dict = response.json()

res_text = response.text
jsonstr_to_dict = json.loads(res_text)

encodeing = (response.encoding)
response_headers = response.headers
url = response.url
res = response.status_code

# post
url = 'https://httpbin.org/post'
json_data = {'key':'value'}
response = requests.post(url, json=json_data)

req_url =     response.request.url
req_body =    response.request.body
req_headers = response.request.headers


##
response_post =  requests.post('https://httpbin.org/post',   data={'key':'value'})
response_put  =  requests.put('https://httpbin.org/put',     data={'key':'value'})
response_patch = requests.patch('https://httpbin.org/patch', data={'key':'value'})

response_delete = requests.delete('https://httpbin.org/delete')
response_head = requests.head('https://httpbin.org/get')
# print(response_head)  <Response [200]>
response_options =  requests.options('https://httpbin.org/get')


##
# Authentication

res_auth = requests.get('https://api.github.com/user', auth=("brb45", "zh" ), timeout=1)
# print(res_auth.status_code)
response = res_auth.json()
response_headers= response.headers

req_headers = response.request.headers


## Upload file
url = 'http://localhost:5000/upload'
with open('sid.jpg', 'rb') as f:

    files = {'image': f}

    r = requests.post(url, files=files)
    print(r.text)

url = "https:// ../analytics/upload_file"
headers = {'Username': 'abc@gmail.com', 'apikey':'123-456'}
with open("abc.zip","rb") as fin:
    files = {"file": ("abc.zip", fin)}
    response = requests.post(url, files=files, headers=headers)
file_id = response.json()['file_ids']

print()

#
import requests
import json
from creds import username
from creds import password

base_url = "https://examplejira.com/rest/api/2/"
headers = {'Content-Type': 'application/json'}
userdata = {
  'username': 'bro',
  'name': 'Bro',
  'password': '32456456',
  'email': 'bro@broiest.com',
  "notification" : "true"
}

req = requests.post(base_url + 'user/', data=json.dumps(userdata), headers=headers, auth=(username, password))

print(req.content)

#
import requests
import json
from creds import username
from creds import password

base_url = 'https://examplejira.com/rest/api/2/'
headers = {'Content-Type': 'application/json'}
params = {
    'jql': 'project = EXM AND resolution is not EMPTY',
    'expand': 'changelog',
}

req = requests.get(base_url + 'search/', headers=headers, params=params, auth=(username, password))

print(req.content)

#
# JIRA User Import

import pandas as pd
import requests
import secrets
import json

# store credentials
from creds import username
from creds import password

# dataframe from csv
user_df = pd.read_csv('users.csv')

# store results of import
rows_list = []

headers = {'Content-Type': 'application/json'}
base_url = "https://examplejira.com/rest/api/2/"

# generate 20-character password
def generate_password():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(20))
    return password

# iterate and create users
for index, row in user_df.iterrows():
    userdata = {
        "name": row['email'].split('@')[0],
        "password": generate_password(),
        "emailAddress": row['email'],
        "displayName": row['name'],
        "notification" : "true"
    }
    req = requests.post(base_url + 'user/', data=json.dumps(userdata), headers=headers, auth=(jirauser, password))
    rows_list.append(userdata) # adds row to array to be tracked
    # create & export results to a csv
    users_imported_df = pd.DataFrame(rows_list)
    users_imported_df.to_csv('users_created.csv')

session = requests.Session()
response= session.get("https://httpbin.org/cookies/set?lastname=skywalker")
# print(session.cookies) <RequestsCookieJar[<Cookie lastname=skywalker for httpbin.org/>]>
# print(session.cookies.keys()) ['lastname']
# print(session.cookies.values()) ['skywalker']

session.cookies.iterkeys()
session.cookies.itervalues()
session.cookies.clear()
# session.cookies

response = requests.post('https://httpbin.org/get')
# response.raise_for_status()

# Versioned URL	/api/now/{version}/awa/agents/{agent_sys_id}
# 'Content-Type': 'multipart/form-data; '

