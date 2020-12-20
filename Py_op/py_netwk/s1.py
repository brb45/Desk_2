#!/usr/bin/env python
"""
import urllib
from urllib.request import urlopen
try:
   import json
except ImportError:  # for Python 2.5
   import simplejson as json

params = {'q': '157 Beacon Dr, Milpitas, CA','output': 'json', 'oe': 'utf8'}
url = 'http://maps.google.com/maps/place' + urllib.parse.urlencode(params)

rawreply = urllib.request.urlopen(url).read()
reply = json.loads(rawreply)
print(reply['Placemark'][0]['Point']['coordinates'][:-1])

from googlemaps import GoogleMaps
address = '207 N. Defiance St, Archbold, OH'
print (GoogleMaps().address_to_latlng(address))
"""
#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 1 - search2.py

import urllib, urllib2
try:
   import json
except ImportError:  # for Python 2.5
   import simplejson as json

params = {'q': '207 N. Defiance St, Archbold, OH','output': 'json', 'oe': 'utf8'}

url = 'http://maps.google.com/maps/geo?' + urllib.urlencode(params)
#path = ('/maps/geo?q=207+N.+Defiance+St%2C+Archbold%2C+OH''&output=json&oe=utf8')
rawreply = urllib2.urlopen(url).read()
#connection = httplib.HTTPConnection('maps.google.com')
#connection.request('GET', path)
#rawreply = connection.getresponse().read()
reply = json.loads(rawreply)
print(reply['Placemark'][0]['Point']['coordinates'][:-1])
#[-84.3063479, 41.5228242]



