def upload_file(self, file_list):
    self.token = ""
    self.headers["Content-Type"] = "application/binary"
    for file in file_list:
        _filename = file.split("/")[-1]
        self.url = "https://{0}.zendesk.com/api/v2/uploads.json".format(self.baseurl)
        self.params = {"filename" : _filename, "token" : self.token}

        status = requests.post(self.url, headers=self.headers, data=open(file, 'rb').read(), params=self.params)
        self.logger.debug(pretty_print_POST(status.request))

        if status.status_code != 201:
            return False, status.text
        self.token = status.json()["upload"]["token"]
    return True, self.token


#!/usr/bin/python

import sys
import requests

user = 'email@example.com/token'
token = '{API_TOKEN}'
url = 'https://{SUBDOMAIN}.zendesk.com/api/v2/uploads.json?filename={foo}'
headers = {'Content-type': 'application/binary', 'Accept': 'text/plain'}

uploaddata = '{foo}'

s = requests.session()
s.auth = (user, token)
resp = s.post(url, headers = headers, data = uploaddata )

print(resp.content)