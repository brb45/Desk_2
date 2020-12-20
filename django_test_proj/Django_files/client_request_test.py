#@@  1. django client
from requests.exceptions import HTTPError
from django.test import TestCase


class PollsViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/polls/')
        self.assertEqual(resp.status_code, 200)

# Client (self.client) built-in to Django's TestCase to fetch the URL /polls/ using GET
# We store that response (an HttpResponse in resp, then perform tests on it.

# resp.status_code
# resp.context
# resp.templates
# resp[<header name>]

class PollsViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/polls/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('latest_poll_list' in resp.context)
        self.assertEqual([poll.pk for poll in resp.context['latest_poll_list']], [1])

import datetime
from django.test import TestCase
from polls.models import Poll, Choice


class PollsViewsTestCase(TestCase):
    def test_index(self):
        poll_1 = Poll.objects.create(
            question='Are you learning about testing in Django?',
            pub_date=datetime.datetime(2011, 04, 10, 0, 37)
        )
        choice_1 = Choice.objects.create(
            poll=poll_1,
            choice='Yes',
            votes=0
        )
        choice_2 = Choice.objects.create(
            poll=poll_1,
            choice='No',
            votes=0
        )

        resp = self.client.get('/polls/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('latest_poll_list' in resp.context)
        self.assertEqual([poll.pk for poll in resp.context['latest_poll_list']], [1])


def test_good_vote(self):
      poll_1 = Poll.objects.get(pk=1)
      self.assertEqual(poll_1.choice_set.get(pk=1).votes, 1)

      resp = self.client.post('/polls/1/vote/', {'choice': 1})
      self.assertEqual(resp.status_code, 302)
      self.assertEqual(resp['Location'], 'http://testserver/polls/1/results/')

      self.assertEqual(poll_1.choice_set.get(pk=1).votes, 2)


#@@ 2.  requests lib
'_content'
'status_code'
'headers'

print(response.content)           # To print response bytes
print(response.text)              # To print unicode response string
jsonRes = response.json()         # To get response dictionary as JSON
# output: Python Requests : Requests are awesome
print(jsonRes['title'], jsonRes['body'], sep=' : ')

import requests
response = requests.get('https://api.github.com')s
Out[2]: < Response[200] >
<class 'requests.models.Response' >

status_code = response.status_code
print(status_code, type(status_code))
# #200 < class 'int' >

response.headers['Content-Type']
# 'application/json; charset=utf-8'

#&&  content
# returns content in raw bytes.
In[18]: response.content
Out[18]: b'{"current_user_url":"https://api.github.com/user","current_user_authorizations_html_url":"https://github.com/settings/connections/applications{/client_id}","authorizations_url":"https://api.github.com/authorizations","code_search_url":"https://api.github.com/search/code?q={query}{&page,per_page,sort,order}","commit_search_url":"https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}","emails_url":"https://api.github.com/user/emails","emojis_url":"https://api.github.com/emojis","events_url":"https://api.github.com/events","feeds_url":"https://api.github.com/feeds","followers_url":"https://api.github.com/user/followers","following_url":"https://api.github.com/user/following{/target}","gists_url":"https://api.github.com/gists{/gist_id}","hub_url":"https://api.github.com/hub","issue_search_url":"https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}","issues_url":"https://api.github.com/issues","keys_url":"https://api.github.com/user/keys","notifications_url":"https://api.github.com/notifications","organization_repositories_url":"https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}","organization_url":"https://api.github.com/orgs/{org}","public_gists_url":"https://api.github.com/gists/public","rate_limit_url":"https://api.github.com/rate_limit","repository_url":"https://api.github.com/repos/{owner}/{repo}","repository_search_url":"https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}","current_user_repositories_url":"https://api.github.com/user/repos{?type,page,per_page,sort}","starred_url":"https://api.github.com/user/starred{/owner}{/repo}","starred_gists_url":"https://api.github.com/gists/starred","team_url":"https://api.github.com/teams","user_url":"https://api.github.com/users/{user}","user_organizations_url":"https://api.github.com/user/orgs","user_repositories_url":"https://api.github.com/users/{user}/repos{?type,page,per_page,sort}","user_search_url":"https://api.github.com/search/users?q={query}{&page,per_page,sort,order}"}'

# Convert content to  string encoded with UTF-8 by default
# Optional: requests infers this internally
In[21]: response.encoding = 'utf-8'
In[22]: response.text
# output is serialized JSON string.
Out[22]: '{"current_user_url":"https://api.github.com/user","current_user_authorizations_html_url":"https://github.com/settings/connections/applications{/client_id}","authorizations_url":"https://api.github.com/authorizations","code_search_url":"https://api.github.com/search/code?q={query}{&page,per_page,sort,order}","commit_search_url":"https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}","emails_url":"https://api.github.com/user/emails","emojis_url":"https://api.github.com/emojis","events_url":"https://api.github.com/events","feeds_url":"https://api.github.com/feeds","followers_url":"https://api.github.com/user/followers","following_url":"https://api.github.com/user/following{/target}","gists_url":"https://api.github.com/gists{/gist_id}","hub_url":"https://api.github.com/hub","issue_search_url":"https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}","issues_url":"https://api.github.com/issues","keys_url":"https://api.github.com/user/keys","notifications_url":"https://api.github.com/notifications","organization_repositories_url":"https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}","organization_url":"https://api.github.com/orgs/{org}","public_gists_url":"https://api.github.com/gists/public","rate_limit_url":"https://api.github.com/rate_limit","repository_url":"https://api.github.com/repos/{owner}/{repo}","repository_search_url":"https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}","current_user_repositories_url":"https://api.github.com/user/repos{?type,page,per_page,sort}","starred_url":"https://api.github.com/user/starred{/owner}{/repo}","starred_gists_url":"https://api.github.com/gists/starred","team_url":"https://api.github.com/teams","user_url":"https://api.github.com/users/{user}","user_organizations_url":"https://api.github.com/user/orgs","user_repositories_url":"https://api.github.com/users/{user}/repos{?type,page,per_page,sort}","user_search_url":"https://api.github.com/search/users?q={query}{&page,per_page,sort,order}"}'

# deserialize to dictionary with json.loads()
In[24]: import json

In[25]: json.loads(response.content)
Out[25]:
{'current_user_url': 'https://api.github.com/user',
 'current_user_authorizations_html_url': 'https://github.com/settings/connections/applications{/client_id}',
 'authorizations_url': 'https://api.github.com/authorizations',
 'code_search_url': 'https://api.github.com/search/code?q={query}{&page,per_page,sort,order}',
 'commit_search_url': 'https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}',
 'emails_url': 'https://api.github.com/user/emails',
 'emojis_url': 'https://api.github.com/emojis',
 'events_url': 'https://api.github.com/events',
 'feeds_url': 'https://api.github.com/feeds',
 'followers_url': 'https://api.github.com/user/followers',
 'following_url': 'https://api.github.com/user/following{/target}',
 'gists_url': 'https://api.github.com/gists{/gist_id}',
 'hub_url': 'https://api.github.com/hub',
 'issue_search_url': 'https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}',
 'issues_url': 'https://api.github.com/issues',
 'keys_url': 'https://api.github.com/user/keys',
 'notifications_url': 'https://api.github.com/notifications',
 'organization_repositories_url': 'https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}',
 'organization_url': 'https://api.github.com/orgs/{org}',
 'public_gists_url': 'https://api.github.com/gists/public',
 'rate_limit_url': 'https://api.github.com/rate_limit',
 'repository_url': 'https://api.github.com/repos/{owner}/{repo}',
 'repository_search_url': 'https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}',
 'current_user_repositories_url': 'https://api.github.com/user/repos{?type,page,per_page,sort}',
 'starred_url': 'https://api.github.com/user/starred{/owner}{/repo}',
 'starred_gists_url': 'https://api.github.com/gists/starred',
 'team_url': 'https://api.github.com/teams',
 'user_url': 'https://api.github.com/users/{user}',
 'user_organizations_url': 'https://api.github.com/user/orgs',
 'user_repositories_url': 'https://api.github.com/users/{user}/repos{?type,page,per_page,sort}',
 'user_search_url': 'https://api.github.com/search/users?q={query}{&page,per_page,sort,order}'}

## or desrialize with .json()
In[27]: response.json()
Out[27]:
{'current_user_url': 'https://api.github.com/user',
 'current_user_authorizations_html_url': 'https://github.com/settings/connections/applications{/client_id}',
 'authorizations_url': 'https://api.github.com/authorizations',
 'code_search_url': 'https://api.github.com/search/code?q={query}{&page,per_page,sort,order}',
 'commit_search_url': 'https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}',
 'emails_url': 'https://api.github.com/user/emails',
 'emojis_url': 'https://api.github.com/emojis',
 'events_url': 'https://api.github.com/events',
 'feeds_url': 'https://api.github.com/feeds',
 'followers_url': 'https://api.github.com/user/followers',
 'following_url': 'https://api.github.com/user/following{/target}',
 'gists_url': 'https://api.github.com/gists{/gist_id}',
 'hub_url': 'https://api.github.com/hub',
 'issue_search_url': 'https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}',
 'issues_url': 'https://api.github.com/issues',
 'keys_url': 'https://api.github.com/user/keys',
 'notifications_url': 'https://api.github.com/notifications',
 'organization_repositories_url': 'https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}',
 'organization_url': 'https://api.github.com/orgs/{org}',
 'public_gists_url': 'https://api.github.com/gists/public',
 'rate_limit_url': 'https://api.github.com/rate_limit',
 'repository_url': 'https://api.github.com/repos/{owner}/{repo}',
 'repository_search_url': 'https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}',
 'current_user_repositories_url': 'https://api.github.com/user/repos{?type,page,per_page,sort}',
 'starred_url': 'https://api.github.com/user/starred{/owner}{/repo}',
 'starred_gists_url': 'https://api.github.com/gists/starred',
 'team_url': 'https://api.github.com/teams',
 'user_url': 'https://api.github.com/users/{user}',
 'user_organizations_url': 'https://api.github.com/user/orgs',
 'user_repositories_url': 'https://api.github.com/users/{user}/repos{?type,page,per_page,sort}',
 'user_search_url': 'https://api.github.com/search/users?q={query}{&page,per_page,sort,order}'}
##
#&& header
# http spec: header attributes are case-insensitive
In[29]: response.headers['content-type']
Out[29]: 'application/json; charset=utf-8'

In[30]: response.headers["Content-Type"]
Out[30]: 'application/json; charset=utf-8'

#@@ querry string parameters
In[32]: response = requests.get(
    'https://api.github.com/search/repositories', params={'q': 'requests+language:python'},)

#@@ cusomize request with headers
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

#@@ 3. Post 
# Using requests, you’ll pass the payload to the corresponding function’s data parameter.
# data takes a dictionary, a list of tuples, bytes, or a file-like object.
requests.post('https://httpbin.org/post', data={'key': 'value'})
requests.put('https://httpbin.org/put', data={'key': 'value'})
requests.delete('https://httpbin.org/delete')
requests.head('https://httpbin.org/get')
requests.patch('https://httpbin.org/patch', data={'key': 'value'})
requests.options('https://httpbin.org/get')

#@@
# if your request’s content type is application/x-www-form-urlencoded
In[49]: requests.post('https://httpbin.org/post', data={'key': 'value'})
In[50]: requests.post('https://httpbin.org/post', data=[('key', 'value')])  #  list of tuples
# If, however, you need to send JSON data, you can use the json parameter
In[51]: response = requests.post(
    'https://httpbin.org/post', json={'key': 'value'})
In[53]: response.json()
Out[53]:
{'args': {},
 'data': '{"key": "value"}',
 'files': {},
 'form': {},
 'headers': {'Accept': '*/*',
             'Accept-Encoding': 'gzip, deflate',
             'Content-Length': '16',
             'Content-Type': 'application/json',
             'Host': 'httpbin.org',
             'User-Agent': 'python-requests/2.21.0'},
 'json': {'key': 'value'},
 'origin': '12.206.238.98, 12.206.238.98',
 'url': 'https://httpbin.org/post'}

#@@  3.1 other HTTP methods
requests.put('url', data={'key': 'value'})
requests.delete('url')
requests.head('url')
requests.options('url')
#@@  4. send files

url = 'http://httpbin.org/post'
file_list = [
    ('image', ('image1.jpg', open('image1.jpg', 'rb'), 'image/png')),
    ('image', ('image2.jpg', open('image2.jpg', 'rb'), 'image/png'))
]

r = requests.post(url, files=file_list)
print(r.text)

#@@ 5. redirect
In[1]: import requests
...:
   ...: r = requests.post("http://www.github.com")
   ...: print(r.url)
https: // github.com/

In[2]:

In[2]: r.status_code
Out[2]: 200

In[3]: r.history
Out[3]: [ < Response [301] > , < Response [301] > ]

# As you can see the redirection process is automatically handled by requests, 
# so you don't need to deal with it yourself. The history property contains the 
# list of all response objects created to complete the redirection. In our example, 
# two Response objects were created with the 301 response code. HTTP 301 and 302 responses 
# are used for permanent and temporary redirection, respectively.

# If you don't want the Requests library to automatically follow redirects, then you can 
# disable it by passing the allow_redirects = False parameter along with the request.
#@@ 6.  Authentication
In[1]: from getpass import getpass
In[5]: import requests
In[6]: requests.get('https://api.github.com/user')
# Out[6]: < Response[401] >
In[7]: requests.get('https://api.github.com/user', auth=('brb45', getpass()))
Password:
Out[7]: < Response[200] >

#
In[10]: from getpass import getpass

In[11]: from requests.auth import HTTPBasicAuth

In[13]: requests.get('https://api.github.com/user',
                     auth=HTTPBasicAuth('brb45', getpass()))
Password:
Out[13]: < Response[200] >


#@@  7.  Security: SSL Certificate Verification
requests verify SSL certificate by default with  verify=True
requests.get('https://api.github.com', verify=False)
c: \users\jsun\appdata\local\programs\python\python37-32\lib\site-packages\urllib3\connectionpool.py: 847:
InsecureRequestWarning: Unverified HTTPS request is being made. 
# ssl-warnings
InsecureRequestWarning)
    Out[14]: < Response[200] >

#@@  8.Performance
# Timeout
    # By default, requests will wait indefinitely on the response


    # The timeout can be configured for both the "connect" and "read" 
    # operations of the request using a tuple, which allows you to specify both values separately:

    import requests
    requests.get('http://www.google.com', timeout = 1)
    requests.get('http://www.google.com', timeout = (5, 14))

# The Session Object
    # high level requests APIs such as get() and post().
    # Underneath those abstractions is a class called Session
    # The primary performance optimization of sessions comes in the form of persistent connections. 
    # When your app makes a connection to a server using a Session, it keeps that connection 
    # around in a connection pool. When your app wants to connect to the same server again, 
    # it will reuse a connection from the pool rather than establishing a new one.

    import requests
    from getpass import getpass

    # By using a context manager, you can ensure the resources used by
    # the session will be released after use
    with requests.Session() as session:
        session.auth=('username', getpass())

    # Instead of requests.get(), you'll use session.get()
        response=session.get('https://api.github.com/user')

    # You can inspect the response just like you did before
        print(response.headers)
        print(response.json())

##
    import requests

    first_session=requests.Session()
    second_session=requests.Session()

    first_session.get('http://httpbin.org/cookies/set/cookieone/111')
    r=first_session.get('http://httpbin.org/cookies')
    print(r.text)

    second_session.get('http://httpbin.org/cookies/set/cookietwo/222')
    r=second_session.get('http://httpbin.org/cookies')
    print(r.text)

    r=first_session.get('http://httpbin.org/anything')
    print(r.text)

    ##
        


# max retries
# When a request fails, you may want your application to retry the same request. 
# However, requests will not do this for you by default. 
# To apply this functionality, you need to implement a custom Transport Adapter.

    import requests
    from requests.adapters import HTTPAdapter
    from requests.exceptions import ConnectionError

    github_adapter=HTTPAdapter(max_retries = 3)

    session=requests.Session()

    # Use `github_adapter` for all requests to endpoints that start with this URL
    session.mount('https://api.github.com', github_adapter)

    try:
    session.get('https://api.github.com')
    except ConnectionError as ce:
    print(ce)


#@@ 9. Cookies
    # Common uses include session tracking, maintaining data across multiple visits, 
    # holding shopping cart contents, storing login details, and more.
    # Because of their privacy implications, cookies can be read only from the issuing domain.

custom_cookie = {'cookie_name': 'cookie_value'}
r = requests.get('http://www.examplesite.com/cookies', cookies=custom_cookie)
r.cookies['cookie_name']

    jar=requests.cookies.RequestsCookieJar()
    jar.set('cookie_one', 'one', domain = 'httpbin.org', path = '/cookies')
    jar.set('cookie_two', 'two', domain = 'httpbin.org', path = '/other')

    r=requests.get('https://httpbin.org/cookies', cookies = jar)
    print(r.text)

    #@@ 10. Proxies
    http="http://10.10.1.10:1080"
    https="https://10.10.1.11:3128"
    ftp="ftp://10.10.1.10:8080"

    proxy_dict={
"http": http,
"https": https,
"ftp": ftp
}

    r = requests.get('http://sampleurl.com', proxies=proxy_dict)

    #@@ 11. Downloading a file

    r = requests.get(
'https://cdn.pixabay.com/photo/2018/07/05/02/50/sun-hat-3517443_1280.jpg', stream = True)
    downloaded_file=open("sun-hat.jpg", "wb")
    for chunk in r.iter_content(chunk_size = 256):
        if chunk:
            downloaded_file.write(chunk)
    
    #@@ 12. Errors and Exceptions
    # 
    # requests throws different types of exception and errors if there is ever a network problem. 
    # All exceptions are inherited from requests.exceptions.RequestException class.

    # Here is a short description of the common erros you may run in to:

    # ConnectionError exception is thrown in case of DNS failure, refused connection or any other connection related issues.
    # Timeout is raised if a request times out.
    # TooManyRedirects is raised if a request exceeds the maximum number of predefined redirections.
    # HTTPError exception is raised for invalid HTTP responses.
    

#@@ 12 Get again
# importing the requests library 
import requests 
  
# api-endpoint 
URL = "http://maps.googleapis.com/maps/api/geocode/json"
    In[9]: r.url
    Out[9]: 'http://maps.googleapis.com/maps/api/geocode/json?address=delhi+technological+university'
  
# location given here 
location = "delhi technological university"
  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'address':location} 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
  
# extracting data in json format 
data = r.json() 
  
  
# extracting latitude, longitude and formatted address  
# of the first matching location 
latitude = data['results'][0]['geometry']['location']['lat'] 
longitude = data['results'][0]['geometry']['location']['lng'] 
formatted_address = data['results'][0]['formatted_address'] 
  
# printing the output 
print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
      %(latitude, longitude,formatted_address)) 










#@@
In[19]: response.__dict__
Out[19]:
{'_content': b'{"current_user_url":"https://api.github.com/user","current_user_authorizations_html_url":"https://github.com/settings/connections/applications{/client_id}","authorizations_url":"https://api.github.com/authorizations","code_search_url":"https://api.github.com/search/code?q={query}{&page,per_page,sort,order}","commit_search_url":"https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}","emails_url":"https://api.github.com/user/emails","emojis_url":"https://api.github.com/emojis","events_url":"https://api.github.com/events","feeds_url":"https://api.github.com/feeds","followers_url":"https://api.github.com/user/followers","following_url":"https://api.github.com/user/following{/target}","gists_url":"https://api.github.com/gists{/gist_id}","hub_url":"https://api.github.com/hub","issue_search_url":"https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}","issues_url":"https://api.github.com/issues","keys_url":"https://api.github.com/user/keys","notifications_url":"https://api.github.com/notifications","organization_repositories_url":"https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}","organization_url":"https://api.github.com/orgs/{org}","public_gists_url":"https://api.github.com/gists/public","rate_limit_url":"https://api.github.com/rate_limit","repository_url":"https://api.github.com/repos/{owner}/{repo}","repository_search_url":"https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}","current_user_repositories_url":"https://api.github.com/user/repos{?type,page,per_page,sort}","starred_url":"https://api.github.com/user/starred{/owner}{/repo}","starred_gists_url":"https://api.github.com/gists/starred","team_url":"https://api.github.com/teams","user_url":"https://api.github.com/users/{user}","user_organizations_url":"https://api.github.com/user/orgs","user_repositories_url":"https://api.github.com/users/{user}/repos{?type,page,per_page,sort}","user_search_url":"https://api.github.com/search/users?q={query}{&page,per_page,sort,order}"}',
 '_content_consumed': True,
 '_next': None,
 'status_code': 200,
 'headers': {'Date': 'Wed, 06 Nov 2019 22:27:11 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Server': 'GitHub.com', 'Status': '200 OK', 'X-RateLimit-Limit': '60', 'X-RateLimit-Remaining': '58', 'X-RateLimit-Reset': '1573082831', 'Cache-Control': 'public, max-age=60, s-maxage=60', 'Vary': 'Accept, Accept-Encoding', 'ETag': 'W/"7dc470913f1fe9bb6c7355b50a0737bc"', 'X-GitHub-Media-Type': 'github.v3; format=json', 'Access-Control-Expose-Headers': 'ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type', 'Access-Control-Allow-Origin': '*', 'Strict-Transport-Security': 'max-age = 31536000
             includeSubdomains
             preload', 'X-Frame-Options': 'deny', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '1
             mode = block', 'Referrer-Policy': 'origin-when-cross-origin,
             strict-origin-when-cross-origin', 'Content-Security-Policy': "default-src 'none'", 'Content-Encoding': 'gzip', 'X-GitHub-Request-Id': '7443: 40E2: 4F0B791: 5C9081C: 5DC348BF'},
 'raw': < urllib3.response.HTTPResponse at 0x4c93f70 > ,
 'url': 'https://api.github.com/',
 'encoding': 'utf-8',
 'history': [],
 'reason': 'OK',
 'cookies': < RequestsCookieJar[] > ,
 'elapsed': datetime.timedelta(microseconds=209040),
 'request': < PreparedRequest [GET] > ,
 'connection': < requests.adapters.HTTPAdapter at 0x4ca0b50 > }
#@@

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')




