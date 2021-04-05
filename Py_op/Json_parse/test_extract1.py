from extract import json_extract
import requests

API_KEY = "ajflsjlsjflkajflakjflaksjfaljfkj"

"""Fetch distance between two points."""
def google_maps_distance():
  params = {
       'units': 'imperial',
       'key': API_KEY,
       'origins': "New York City,NY",
       'destinations': "Washington,DC|Philadelphia,PA|Santa Barbara,CA|Miami,FL|Austin,TX|Napa Valley,CA",
       'transit_mode': 'car'
  }
  endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json"
  r = requests.get(endpoint, params=params)
  travel_values = json_extract(r.json(), 'text')
  return travel_values

print(google_maps_distance())

