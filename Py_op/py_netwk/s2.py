#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 1 - search3.py

import httplib
try:
   import json
except ImportError:  # for Python 2.5
   import simplejson as json

path = ('/maps/place/157+Beacon+Dr,+Milpitas,+CA+95035/@37.4347988,-121.87844,17z/data=!3m1!4b1!4m5!3m4!1s0x808fcee0d56d0779:0xf374dd6c54102161!8m2!3d37.4347988!4d-121.8762513''&output=json&oe=utf8')


connection = httplib.HTTPConnection('maps.google.com')
connection.request('GET', path)
rawreply = connection.getresponse().read()
#reply = json.loads(rawreply)
#print(reply['Placemark'][0]['Point']['coordinates'][:-1])
print(rawreply)