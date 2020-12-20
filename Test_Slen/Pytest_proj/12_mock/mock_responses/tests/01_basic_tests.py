import requests
import json


def test_get_locations_for_us_90210_check_status_code_equals_200():
    response = requests.get("http://api.zippopotam.us/us/90210")
    print("\nresponse Header")
    print(f"type of headers is {type(response.headers)}")
    with open("header.json", 'w') as fout:
        json.dump(dict(response.headers), fout, indent=5)
    print("\nresponse body")
    print(f"type of response is {type(response.json())}")
    with open('response1.json', 'w') as fout:
        json.dump(response.json(), fout, indent = 0)
    print(response.json())
    print("\n")
    assert response.status_code == 200


def test_get_locations_for_us_90210_check_content_type_equals_json():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.headers['Content-Type'] == "application/json"


def test_get_locations_for_us_90210_check_country_equals_united_states():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body["country"] == "United States"


def test_get_locations_for_us_90210_check_city_equals_beverly_hills():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == "Beverly Hills"


def test_get_locations_for_us_90210_check_one_place_is_returned():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert len(response_body["places"]) == 1
