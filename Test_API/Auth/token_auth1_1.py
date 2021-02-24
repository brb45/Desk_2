##2. Token Authentication

import requests, json #, jsonpath
from requests.auth import HTTPBasicAuth


def return_token():
    file = "C:\\Users\jsun\Desktop\QA\Weekly\\token.txt"
    with open(file) as fout:
        token = fout.read()
    token  = token.split()
    return token



url = 'https://api.github.com/user'

def authentication_get():
    token = return_token()[1]
    # headers = {'Authorization': token}
    headers = {'Authorization': 'token ' + token}

    response = requests.get(url, headers=headers)
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
    # application / json;
    # charset = utf - 8
authentication_get()


