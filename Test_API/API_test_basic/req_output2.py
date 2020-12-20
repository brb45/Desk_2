import requests
import json

url = "https://api.nasa.gov/planetary/apod"
param={"api_key": "DEMO_KEY", "date": "2019-04-11"}
headers = {"content-type": "application/json"}
r = requests.get(
    url,
    params=param,
    headers= headers
)

print(json.dumps(dict(r.request.headers), indent=3))


headers = {"content-type": "application/json"}
r = requests.get(
    url,
    params=param,
    # headers= headers
)

print(json.dumps(dict(r.request.headers), indent=3))

