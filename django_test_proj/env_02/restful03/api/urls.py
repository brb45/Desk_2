from django.conf.urls import url
#from .views import HelloWorldView
from .views import SubscriberViewSet

# Building REST APIs with plain old Django is very possible but we have to do a lot.
urlpatterns = [
    #url(r'hello', hello_world, name="hello_world")  #http://localhost:8000/api/hello
    url("subscriber", SubscriberViewSet.as_view({'get': 'list', 'post': 'create'})),
    url("subscriber/(?P<pk>[0-9]+)$",
        SubscriberViewSet.as_view({'get': 'retrieve', 'put': 'update'}))
    # url("subscriber/^[0-9]+$", SubscriberViewSet.as_view({'get': 'retrieve', 'put': 'update'}))
    # SubscriberViewSet.as_view({'get': 'list', 'post': 'create'})  # For: /api/subscriber
    # SubscriberViewSet.as_view({'get': 'retrieve', 'put': 'update'})  # For: /api/subscriber/1
]
