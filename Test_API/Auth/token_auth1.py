##2. Token Authentication

import requests, json #, jsonpath
from requests.auth import HTTPBasicAuth
# Using OAuth tokens for apps
# Apps that need to read or write private information using the API on behalf of another user should use OAuth.
#
# OAuth uses tokens. Tokens provide two big features:
#
# Revokable access: users can revoke authorization to third party apps at any time
# Limited access: users can review the specific access that a token will provide before authorizing a third party app
# Tokens should be created via a web flow. An application sends users to GitHub to log in.
# GitHub then presents a dialog indicating the name of the app, as well as the level of access the app has once
# it's authorized by the user. After a user authorizes access, GitHub redirects the user back to the application:
# list repositories for another user:

def return_token():
    file = "C:\\Users\jsun\Desktop\QA\Weekly\\token.txt"
    with open(file) as fout:
        token = fout.read()
    token  = token.split()
    return token

url = "https://api.github.com/users/brb45/repos"

def authentication_get():
    token = return_token()[1]
    # headers={'Authorization': 'token ' + token}
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers = headers)
    print(response.status_code)
    print("-----------------------------")
    response_dic = response.json()
    print(response_dic)
    # {'login': 'brb', 'id': 10520787, 'node_id': 'MDQ6VXNlcjEwNTIwNzg3',
    #  'avatar_url': 'https://avatars.githubusercontent.com/u/10520787?v=4', 'gravatar_id': '',
    #  'url': 'https://api.github.com/users/brb45', 'html_url': 'https://github.com/brb45',
    #  'followers_url': 'https://api.github.com/users/brb45/followers',
    #  'following_url': 'https://api.github.com/users/brb45/following{/other_user}',
    #  'gists_url': 'https://api.github.com/users/brb45/gists{/gist_id}',
    #  'starred_url': 'https://api.github.com/users/brb45/starred{/owner}{/repo}',
    #  'subscriptions_url': 'https://api.github.com/users/brb45/subscriptions',
    #  'organizations_url': 'https://api.github.com/users/brb45/orgs',
    #  'repos_url': 'https://api.github.com/users/brb45/repos',
    #  'events_url': 'https://api.github.com/users/brb45/events{/privacy}',
    #  'received_events_url': 'https://api.github.com/users/brb45/received_events', 'type': 'User', 'site_admin': False,
    #  'name': 'Jian Sun', 'company': None, 'blog': '', 'location': None, 'email': None, 'hireable': None, 'bio': None,
    #  'twitter_username': None, 'public_repos': 26, 'public_gists': 0, 'followers': 0, 'following': 0,
    #  'created_at': '2015-01-13T19:39:38Z', 'updated_at': '2021-02-15T18:20:34Z'}
    # print(response.json()) # user profile



    print("-------------------------------------")
    header_response = response.headers
    print(header_response)
    # {'Date': 'Mon, 15 Feb 2021 19:52:40 GMT', 'Content-Type': 'application/json; charset=utf-8',
    #  'Transfer-Encoding': 'chunked', 'Server': 'GitHub.com', 'Cache-Control': 'public, max-age=60, s-maxage=60',
    #  'Vary': 'Accept, Accept-Encoding, Accept, X-Requested-With, Accept-Encoding',
    #  'ETag': 'W/"5369ced994090838c55fb43f9d2a5dc15b0822b8e0245bb10839b508e0d8b2d3"',
    #  'last-modified': 'Mon, 15 Feb 2021 18:20:34 GMT', 'X-GitHub-Media-Type': 'github.v3; format=json',
    #  'X-RateLimit-Limit': '60', 'X-RateLimit-Remaining': '48', 'X-RateLimit-Reset': '1613421876',
    #  'x-ratelimit-used': '12',
    #  'Access-Control-Expose-Headers': 'ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, Deprecation, Sunset',
    #  'Access-Control-Allow-Origin': '*', 'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload',
    #  'X-Frame-Options': 'deny', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '1; mode=block',
    #  'Referrer-Policy': 'origin-when-cross-origin, strict-origin-when-cross-origin',
    #  'Content-Security-Policy': "default-src 'none'", 'Content-Encoding': 'gzip',
    #  'X-GitHub-Request-Id': 'C8A9:6786:A0C91A:BC7538:602AD108'}
    # print(type(header_response)) # <class 'requests.structures.CaseInsensitiveDict'>
    print(header_response['content-type'])
    # application / json;
    # charset = utf - 8

authentication_get()





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

def test_oauth_api_2():

    auth_token = 'kbkcmbkcmbkcbc9ic9vixc9vixc9v'
    hed = {'Authorization': 'Bearer ' + auth_token}
    data = {'app': 'aaaaa'}

    url = 'https://api.xy.com'
    response = requests.post(url, json=data, headers=hed)
    print(response)
    print(response.json())

def get_oauth_token():
    import json

    user_passwd = {"username": "youremail@email.com", "password": "YOURPASSWORD"}

    headers = {"Client_id": "3QC11Sm45ti8wEG0d9A5hma5XIlGG7U9",
               "Client_secret": "ipu3WQDqTEjqZDXW",
               "Content-Type": "application/json"}

    response = requests.post("https://sandbox-us-api.experian.com/oauth2/v1/token", data=user_passwd, headers=headers)

    if response.status_code in [200]:
        tok_dict = json.loads(response.text)
        print(tok_dict)
        issued_at = tok_dict["issued_at"]
        expires_in = tok_dict["expires_in"]
        token_type = tok_dict["token_type"]
        access_token = tok_dict["access_token"]
    else:
        print(response.text)

def get_oauth_token1():
    url = 'https://login.insideview.com/Auth/login/v1/token'
    payload = {'clientId': '****', 'clientSecret': '****', 'grantType': 'cred'}
    headers = {'Accept': 'application/json'}
    r = requests.post(url, headers=headers, params=payload)

    data = json.loads(r.text)
    data['accessTokenDetails']['accessToken']
    res = {"accessTokenDetails": {"accessToken": "the_access_token", "tokenType": "bearer",
                            "expirationTime": "Fri, Mar 25, 2016 09:59:53 PM GMT",
                            "userInfo": {"userId": null, "firstName": null, "lastName": null, "userName": null,
                                         "companyName": null, "accountId": null, "role": null}}}

import requests, json

access_token = requests.get("https://graph.facebook.com/oauth/access_token"
                            "?grant_type=client_credentials&client_id=your_client_id&client_secret=your_client_secret").json()["access_token"]