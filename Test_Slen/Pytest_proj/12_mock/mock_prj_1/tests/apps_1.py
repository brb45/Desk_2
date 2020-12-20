import requests


def call_external_api():
    response = requests.get("http://worldtimeapi.org/api/timezone/Europe/Rome")
    data = response.json()
    currenttime = data.get("datetime")
    return currenttime