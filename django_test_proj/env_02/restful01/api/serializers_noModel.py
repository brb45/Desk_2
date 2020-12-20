# Django model, or a queryset , are not Jason serializable. They need to be converted to Python data structure,
# which could be serialized into Json. We can serialize queryset into python list, and model instances into
# python dictionary.
# On the other hand, incoming data as request.data comes as key-value pairs, which can't be saved in database directly.
# We have to transform them into Django's data structure like models and queryset.
#
# json string->(json-parser)=> python data structure(dict, or list) ->(De-serializer)=>Django data structure(model, or queryset)
# -> saved to database
# Serialize(Django data type) ->> python data types

# serializer also do data validation.

from rest_framework import serializers


class HelloWorldSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=20)
    age = serializers.IntegerField(required=False, min_value=10, default=30)

