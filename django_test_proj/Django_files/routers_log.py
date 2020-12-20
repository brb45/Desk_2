# serializers.py
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# viewsets.py
from rest_framework import viewsets
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# urls.py
from django.conf.urls import url, include
from .viewsets import UserViewSet

router = routers.DefaultRouter()
router.register(r'custom_name', UserViewSet)

urlpatterns = [
    # .......
    url(r'^', include(router.urls, namespace="myapp")),
    # .......
]

# Now, try the following in the django shell (python manage.py shell)
from test_rest.urls import router

for url in router.urls:
    print(url.__dict__)

# You will get output like below
# {'_regex_dict': {}, u'regex': < _sre.SRE_Pattern
# object
# at
# 0x7ff790dbd730 >, 'name': u'user-list', 'callback': < function
# CUserViewSet
# at
# 0x7ff790dd1b18 >, '_regex': u'^custom_name/$', 'default_args': {}}
#
# {'_regex_dict': {}, 'callback': < function
# CUserViewSet
# at
# 0x7ff790dd1b18 >, 'name': u'user-list', '_regex': u'^custom_name\\.(?P<format>[a-z0-9]+)/?$', 'default_args': {}}
# {'_regex_dict': {}, u'regex': < _sre.SRE_Pattern
# object
# at
# 0x7ff790dbc280 >, 'name': u'user-detail', 'callback': < function
# CUserViewSet
# at
# 0x7ff790dd1c08 >, '_regex': u'^custom_name/(?P<pk>[^/.]+)/$', 'default_args': {}}
#
# {'_regex_dict': {}, 'callback': < function
# CUserViewSet
# at
# 0x7ff790dd1c08 >, 'name': u'user-detail', '_regex': u'^custom_name/(?P<pk>[^/.]+)\\.(?P<format>[a-z0-9]+)/?$', 'default_args': {}}
# {'_regex_dict': {}, u'regex': < _sre.SRE_Pattern
# object
# at
# 0x7ff790e61ab0 >, 'name': u'api-root', 'callback': < function
# APIRootView
# at
# 0x7ff790dd1cf8 >, '_regex': u'^$', 'default_args': {}}
# {'_regex_dict': {}, 'callback': < function
# APIRootView
# at
# 0x7ff790dd1cf8 >, 'name': u'api-root', '_regex': u'^\\.(?P<format>[a-z0-9]+)/?$', 'default_args': {}}