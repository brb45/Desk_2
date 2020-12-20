from django.conf.urls import url
from .views import HelloWorldView

# Building REST APIs with plain old Django is very possible but we have to do a lot.
urlpatterns = [
    #url(r'hello', hello_world, name="hello_world")  #http://localhost:8000/api/hello
    url("hello", HelloWorldView.as_view(), name="hello_world")
]