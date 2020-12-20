# Upload Files
# Upload one or more files to the server.

# cURL
# Single File
# curl -X POST -F file=@file.xml --user {username}:{password} https://{server}:{port}/api/upload
# Multiple Files
# curl -X POST -F file=@file1.xml -F file=@file2.xml --user {username}:{password} https://{server}:{port}/api/upload
# python


# Single File
url = 'https://{server}:{port}/api/upload'
auth_data = ('{username}', '{password}')
import requests
with open('file.xml', 'rb') as xml:
    r = requests.post(url, auth=auth_data, files=('file',xml))
    print(r.text)
# Multiple Files
import requests
filelist = [('file', open('file1.xml', 'rb')), ('file', open('file2.xml', 'rb'))]
r = requests.post(url, auth=auth_data, files=filelist)
print(r.text)


