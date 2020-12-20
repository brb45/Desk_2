# Use Generic View

from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import SubscriberSerializer
from .models import Subscriber

class SubscriberView(ListAPIView, CreateAPIView):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()

    # We no longer need to provide get, or post methods in the view class, the generic views know
    # how to take care of them