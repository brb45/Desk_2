from django.conf.urls import url
from .views import hello_world

# Building REST APIs with plain old Django is very possible but we have to do a lot.
urlpatterns = [
    url(r'hello', hello_world, name="hello_world")  #http://localhost:8000/api/hello
]