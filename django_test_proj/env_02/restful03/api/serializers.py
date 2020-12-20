# define ModelSerializer

from rest_framework import serializers
from .models import Subscriber

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = "__all__"

    # Our new SubscriberSerializer infers the fields from the model Subscriber, we passed on to it. We can however
    # choose which fields should be used while serializing/deserializing. In this implementation, we use "__all__"
    # and use all fields. In many cases, we want to selectively use some fields, like not include password field.

    # this should work with APIView, without any changes on the views.py, except serializers.py is more concise.

