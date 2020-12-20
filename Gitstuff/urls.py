# urls created from scratch
from django.conf.urls import url
# from ..toys import views
from . import views
#route URLs from request to views
urlpatterns = [
	url(r'^toys/$', views.toy_list),
	url(r'^toys/(?P<pk>[0-9]+)$', views.toy_detail),
]


