
##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# from rest_framework import models
# class User(models.Model):
#  name = models.CharField(max_length=255)
#  surname = models.CharField(max_length=255)
# class Invoice(models.Model):
#  user = models.ForeignKey(User)
#  number = models.CharField(max_length=25)
#
# class testUser(models.Model):
#     testName = models.CharField(max_length=255)
#     testuser = models.ForeignKey()

#list of json object,
# json object, enclosed with {}
# array of json 2 objects
family = [{
    "name" : "Jason",
    "age" : "24",
    "gender" : "male"
},
{
    "name" : "Kyle",
    "age" : "21",
    "gender" : "male"
}];

#nest json objects
testtest={
    "jason" : {
        "name" : "Jason Lengstorf",
        "age" : "24",
        "gender" : "male"
    },
    "kyle" : {
        "name" : "Kyle Lengstorf",
        "age" : "21",
        "gender" : "male"
    }
}

from rest_framework import serializers
from main.models import Cat, Dog

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('owner ' , ' name ' , ' birthday ' )
        read_only_fields = ( ' owner ' ,)
class CatSerializer(serializers.ModelSerializer):
 class Meta:
    model = Cat
    fields = ('owner', 'name', 'birthday')
    read_only_fields = ('owner',)
## viewset
from rest_framework import viewsets, permissions
from main.models import Cat, Dog
from .permissions import IsOwnerOrReadOnly
from .serializers import CatSerializer, DogSerializer
# Create your views here.
class BaseViewSet ( viewsets . ModelViewSet ):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
def get_queryset(self):
    qs = self.queryset.filter(owner=self.request.user)
    return qs
def perform_create(self, serializer):
    serializer.save(owner = self.request.user)
class DogViewSet(BaseViewSet):
    serializer_class = DogSerializer
    queryset = Dog.objects.all ()
class CatViewSet(BaseViewSet):
    serializer_class = CatSerializer
    queryset = Cat.objects.all ()

class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    def get_queryset(self):
        qs = self.queryset.filter()

####
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from .models import Dog


class DogFeedView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsOwnerOrReadOnly,)

    def get(self, request, pk=None):
        dog = get_object_or_404(Dog, pk=pk)
        dog.feed()
        return Response({'msg': 'Dog fed', status : status.HTTP_200_OK})

###
        from rest_framework import routers
        from .views import DogViewSet, CatViewSet, DogFeedView
        router = routers.DefaultRouter(trailing_slash=False)
        router.register('dogs', DogViewSet)
        router.register('cats', CatViewSet)
        urlpatterns = router.urls
        urlpatterns += [
            url(r'dogs / (?P < pk >[\d]+) / feed /$', DogFeedView.as_view(), name = dogfeed)
        ]
## renderer
        # …
        # (… other definition code)
        from rest_framework import renderers
        from rest_framework_xml.renderers import XMLRenderer

    class DogFeedView(APIView):
        renderer_classes = (renderers.TemplateHTMLRenderer, renderers.JSONRenderer, XMLRenderer)
        # (other definition code …)

    # …
##
    class ImageRenderer(renderers.BaseRenderer):
        media_type = 'image/png'
        format = 'image'

        def render(self, data, media_type=None, renderer_context=None):
            return data

            # view class

    class ShowImage(APIView):
        renderer_classes = (ImageRenderer,)

        def get(self, request, format=None):
            print('format', format)
            if format == 'image':
                image_file = open('path_to_image', 'rb')
                response = HttpResponse(image_file, content_type='image/png')
                response['Content-Disposition'] = 'attachment; filename={}'.format('image_filename')

    # urls.py
    urlpatterns = format_suffix_patterns([
        url(r'image/?$', views.ShowImage.as_view())
    ])
## 1.