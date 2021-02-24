##1. Basic Authentication

# Basic Authentication
# Many web services that require authentication accept HTTP Basic Auth. This is the simplest kind, and Requests supports it straight out of the box.
#
# Making requests with HTTP Basic Auth is very simple:
#
# >>> from requests.auth import HTTPBasicAuth
# >>> requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))
# <Response [200]>
# In fact, HTTP Basic Auth is so common that Requests provides a handy shorthand for using it:
#
# >>> requests.get('https://api.github.com/user', auth=('user', 'pass'))
# <Response [200]>
# Providing the credentials in a tuple like this is exactly the same as the HTTPBasicAuth example above.

import requests, json #, jsonpath
from requests.auth import HTTPBasicAuth

# https://docs.github.com/en/rest/guides/getting-started-with-the-rest-api
# https://api.github.com/users/defunkt
# "https://api.github.com/user"


url = "https://api.github.com/users/brb45"
# url = "https://api.github.com/users/brb45/repos"
def authentication_get():
    response = requests.get(url, auth=("brb45", "z9"))
    # response = requests.get(url, verify=False,auth=("brb45", "z9"))
    # Note: sometimes, we may get SSL error certificate verify failed, to avoid, we can use verify=False
    # response = requests.get(url, auth=HTTPBasicAuth("brb45", "z9"))
    # response = requests.get(url, auth=HTTPBasicAuth(username="brb45", password="z9"))
    # print(json.loads(response.text))

    # print(type(response)) <class 'requests.models.Response'>
    response_dic = response.json()
    # print(type(response_dic)) <class 'dict'>
    print(response_dic)
    # {'login': 'brb45', 'id': 10520787, 'node_id': 'MDQ6VXNlcjEwNTIwNzg3',
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
    print(response.status_code)


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
    print(header_response['Content-Type'])
    # application / json;
    # charset = utf - 8
authentication_get()

# {'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/reference/users#get-the-authenticated-user'}
# {'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/reference/users#get-the-authenticated-user'}
# 401




