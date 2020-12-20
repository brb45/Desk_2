# This example uses the Python Requests Library and you will need to install requests package for python
# Documentation can be found at http://docs.python-requests.org/en/master/user/quickstart/
import requests
import pprint
import json

# Specify the Endpoint URL replacing {servicenow_instance_name} with your ServiceNow Instance Name
url = 'https://{servicenow_instance_name}.service-now.com/api/now/attachment/upload'

# Specify Parameters for File Being Uploaded, the table_name and table_sys_id should be replaced with values that make
# sense for your use case
payload = {'table_name':'incident', 'table_sys_id':'81f8915bdb6ba20028927416bf961971'}

# Specify Files To Send and Content Type. When specifying fles to send make sure you specify the path to the file, in
# this example the file was located in the same directory as the python script being executed.
# it is important to specify the correct file type
files = {'file': ('issue_screenshot.JPG', open('issue_screenshot.JPG', 'rb'), 'image/jpg', {'Expires': '0'})}

# Eg. User name="admin", Password="admin" for this code sample. This will be sent across as basic authentication
user = 'admin'
pwd = 'admin'

# Set proper headers
headers = {"Accept":"*/*"}

# Send the HTTP request
response = requests.post(url, auth=(user, pwd), headers=headers, files=files, data=payload)

# Check for HTTP codes other than 201
if response.status_code != 201:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Print Resopnse Details
print('Response Status Code:', response.status_code)
print('')
print('Reponse Payload:')
print(json.dumps(response.json(), indent=4))