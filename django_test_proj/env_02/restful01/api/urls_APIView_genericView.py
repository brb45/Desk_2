from django.conf.urls import url
#from .views import HelloWorldView
from .views import SubscriberView

# Building REST APIs with plain old Django is very possible but we have to do a lot.
urlpatterns = [
    #url(r'hello', hello_world, name="hello_world")  #http://localhost:8000/api/hello
    url("subscriber", SubscriberView.as_view(), name="Subscripber")
]