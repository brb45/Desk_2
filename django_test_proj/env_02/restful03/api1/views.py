# ModelViewSet

from rest_framework.viewsets import ModelViewSet

from .serializers import SubscriberSerializer
from .models import Subscriber

class SubscriberViewSet(ModelViewSet):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()
    # handles both the collection: /api/subscriber and element path /api/subscriber/1
    # in urls: we can declare those paths separately
    # SubscriberViewSet.as_view({'get': 'list', 'post': 'create'})     # For: /api/subscriber
    # SubscriberViewSet.as_view({'get': 'retrieve', 'put': 'update'})  # For: /api/subscriber/1
    # or we can use Router