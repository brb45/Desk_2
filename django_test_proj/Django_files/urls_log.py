# URL anatomy
# URI: Uniform Resource Identifier
# URI = Scheme + NetLocation + Path + Query + Fragment
# http://dev.example.com:80/gallery/videos?id=217#comments
# Scheme='http', netloc = 'dev.example.com:80',
# path = '/gallery/videos'
# params='', query='id=217', fragment='comments'

# In many cases, urls.py is the entry point for your project. Essentially, urls.py contains the root
# URL configuration or URLConf of the entire project
# It is a Python list of patterns assigned to a global called urlpatterns.
# Each incoming URL is matched with each pattern in the list from top to bottom in a sequence.
# In the first match, the search stops, and the request is sent to corresponding view.

# By default, Django looks up url definitions in the urls.py file inside a project’s main directory - it’s worth
# mentioning this is on account of the ROOT_URLCONF variable in settings.py. However, once a project grows beyond
# a couple of urls, it can become difficult to manage them inside this single file

urlpatterns = [

    # Homepage
    url(r'^$', views.IndexView.as_view(), name='home'),

    # About
    url(r'^about/$',
        TemplateView.as_view(template_name="python/about.html"),
        name='about'),

    # Blog URLs
    url(r'^blogs/', include('blogs.urls', namespace='blog')),

    # Job archive
    url(r'^jobs/(?P<pk>\d+)/$',
        views.JobArchive.as_view(),
        name='job_archive'),

    # Admin URLs    url(r'^admin/', include(admin.site.urls)),

    # ...
]
# Each URL pattern is created using ther url function. most patterns take 3 arguments:
# regular expression pattern, view callable, and name of the view

# From Django 2.0 onwards, you can use a simplified URL pattern without regular expression.
# simplified URL pattern syntax:
# Homepage
url(r'^$', IndexView.as_view(), name='home'), # 'home' is name of the pattern, not the name of the url
path('', IndexView.as_view(), name='home'),

url(r'^about/$',AboutView.as_view(),name='about')
path('about/',AboutView.as_view(), name='home'),

url(r'^hello/(?P<name>\w+)/$', views.hello_fn)
path('hello/<str:name>/', views.hello_fn),

url(r'^(?P<year>[0-9]{4})/(?P<month>[-\w]+)/(?P<day>[0-9]+)/(?P<pk>[0-9]+)/$'
path('<int:year>/<int:month>/<int:day>/<int:pk>/'

# types:
str, int ,
slug: Any string made up of a combination of letters, numbers, hyphen - , or underscore _
uuid
path: any string including the path separator /

# Regular expression URL pattern Syntax
^year/(\d{4})/
year/<int:year>

# Names and namespaces:
# Always name your patterns. Names must be unique, namespace is created to solve name conflicts.
# Pattern names used in namespace only have to be unique within the namespace, not the entire project.

# URL format:
# Use / as separator, don't use a trailing slash

url(r'^$', ) # empty string (home page), http://127.0.0.1/

url(r'^stores/', ) # any trailing characters,
# http://127.0.0.1/stores, http://127.0.0.1/stores/
# http://127.0.0.1/stores/long+string+with+anything+12345

url(r'^about/contact/$', ...) , exact, no trailing characters.
# http://127.0.0.1/about/contact/
# Doesn’t match: http://127.0.0.1/about/

url(r'^stores/\d+\', ...)
# Matches:
# http://127.0.0.1/stores/2/
# http://127.0.0.1/stores/34/
# Doesn't match: http://127.0.0.1/stores/downtown/

url(r'^drinks/\D+/', ...)
# Matches: http://127.0.0.1/drinks/mocha/
# Doesn't match: http://127.0.0.1/drinks/324/

url(r'^drinks/mocha|espresso/', ... )
# Matches: http://127.0.0.1/drinks/mocha/
# Doesn't match: http://127.0.0.1/drinks/mochaccino/

url(r'drinks/mocha$|espresso/$', ...)
# Matches: http://127.0.0.1/drinks/espresso/
# Doesn't match: http://127.0.0.1/drinks/espressomacchiato/

url(r'^stores/\w+/', ...)
# Matches: http://127.0.0.1/stores/sandiego/
# http://127.0.0.1/stores/LA/
# http://127.0.0.1/stores/1/
# Doesn't match:
# http://127.0.0.1/san-diego/

url(r'^stores/[-\w+/', ...)
# Matches:
# http://127.0.0.1/stores/san-diego/

url(r'^state/[A-Z]{2}')
# Matches:
# http://127.0.0.1/state/CA/
# Doesn’t match:
# http://127.0.0.1/state/Ca/

url(r'^drinks/(?P<drink_name>\D+/')
# ?P <> tells Django to treat this as a named group
# /drinks/mocha/
# /drinks/espresso/
# /drinks/latte/

























