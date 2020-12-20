import requests, json, jsonpath
from requests.auth import HTTPBasicAuth

def test_with_authentication():
    response = requests.get("https://api.github.com/user", auth=HTTPBasicAuth("br","zh"))
    print(json.loads(response.text))
    print(response.status_code)
test_with_authentication()


# Resource:
#
# POST /auth/v1/oauth/token
# GET  /auth/v1/validate_token
#
# Response:
# access_token, refresh_token, token_type (bearer), expires_in(second), scope("email access")

# Get a token
# POST https://geobigdata.io/auth/v1/oauth/token/
# Form data: {grant_type: password, username: email_address, password: userpasswd}
def test_oauth_api():
    token_url = "https://thetestingworldapi.com/Token"
    data= {"grant_type":"password", "username":"admin", "password":"passwd"}
    response = requests.post(token_url, data)

    token_value = jsonpath.jsonpath(response.json(), "access_token")

    auth = {"Authorization": "Bearer "+ token_value[0]}
    API_URL = "http://thetestingworldapi.com/api/StDetails/1104"
    response  = requests.get(API_URL, headers=auth)
