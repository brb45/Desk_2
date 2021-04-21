import requests

loginurl = 'https://jira01.devtools.mycompany.com/rest/auth/1/session'

filepath = 'C:\Path\To\My\JIRA.pem'

loginArgs = {'username': 'myusername', 'password': 'mypassword'}

resp = requests.post(loginurl, json=loginArgs, verify=filepath)

print(resp.status_code, resp.reason)