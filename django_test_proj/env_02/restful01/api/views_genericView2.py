# ListCreateAPIView function as both ListAPIView and CreateAPIView for GET and POST
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView\
    #, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from .serializers import SubscriberSerializer
from .models import Subscriber

class SubscriberView(ListCreateAPIView):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()

# RetrieveUpdateDestroyAPIView
# used to GET, PUT, PATCH and DELETE.


