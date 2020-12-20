from datetime import datetime
from django.utils import timezone
from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .toys.models import Toy
from .toys.serializers import ToySerializer


toy_release_date = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
toy1 = Toy(name='Snoopy talking action figure', description='Snoopy speaks five languages', release_date=toy_release_date, toy_category='Action figures', was_included_in_home=False)
print(type(toy1))  # <class 'toys.models.Toy'>
toy1.save()
# print(type(toy1))
# <class 'toys.models.Toy' >

print(toy1.pk)
print(toy1.name)
print(toy1.created)
print(toy1.was_included_in_home)
print(toy2.pk)
print(toy2.name)
print(toy2.created)
print(toy2.was_included_in_home)
# >>> print(toy1.pk)
# 1
# >>> print(toy1.name)
# Snoopy talking action figure
# the generated dictionary, a rest_framework.utils.serializer_helpers.ReturnDict instance

serializer_for_toy1 = ToySerializer(toy1)
print(type(serializer_for_toy1))
# <class 'toys.serializers.ToySerializer' >
dir(serializer_for_toy1)

print(type(serializer_for_toy1.data))
# <class 'rest_framework.utils.serializer_helpers.ReturnDict' >

# print((serializer_for_toy1.data))
# {'id': 13, 'name': 'Management of fancy test', 'description': 'Tests overall',
#     'release_date': '2019-10-07T17:12:30.365450Z', 'toy_category': 'Action figures', 'was_included_in_home': True}


json_renderer = JSONRenderer()
# Render a dict to JSON
toy1_rendered_into_json = json_renderer.render(serializer_for_toy1.data)

print(type(toy1_rendered_into_json))
# <class 'bytes' >

print(toy1_rendered_into_json)
# b'{"id":13,"name":"Management of fancy test","description":"Tests overall", 
# "release_date":"2019-10-07T17:12:30.365450Z","toy_category":"Action figures","was_included_in_home":true}'

#___________________________________________________________________________________________________
# json to model instance
json_string_for_new_toy = \
    '{"name":"Clash Royale play set","description":"6 figures from Clash Royale", "release_date":"2017-10-09T12:10:00.776594Z","toy_category":"Playset","was_included_in_home":false}'
print(type(json_string_for_new_toy))
# <class 'str'>
print(json_string_for_new_toy)
{"name": "Clash Royale play set", "description": "6 figures from Clash Royale",
    "release_date": "2017-10-09T12:10:00.776594Z", "toy_category": "Playset", "was_included_in_home": false}

json_bytes_for_new_toy = bytes(json_string_for_new_toy, encoding="UTF-8")
# <class 'bytes'>
print((json_string_for_new_toy))
b'{"name":"Clash Royale play set","description":"6 figures from Clash Royale", "release_date":"2017-10-09T12:10:00.776594Z","toy_category":"Playset","was_included_in_home":false}'

stream_for_new_toy = BytesIO(json_bytes_for_new_toy)
print(type(stream_for_new_toy))
<class '_io.BytesIO' >
print(stream_for_new_toy)
<_io.BytesIO object at 0x06BDF330 >

parser = JSONParser()
parsed_new_toy = parser.parse(stream_for_new_toy)
print(type(parsed_new_toy))
<class 'dict' >
print(parsed_new_toy) # generate a dict from JSON
# {'name': 'Clash Royale play set', 'description': '6 figures from Clash Royale', 'release_date': '2017-10-09T12:10:00.776594Z', 'toy_category': 'Playset', 'was_included_in_home': False}

new_toy_serializer = ToySerializer(data=parsed_new_toy)
print(type(new_toy_serializer))
<class 'toys.serializers.ToySerializer' >

In[74]: if new_toy_serializer.is_valid():
    ...: print(new_toy_serializer.data)
    ...:
{'name': 'Clash Royale play set', 'description': '6 figures from Clash Royale',
    'release_date': '2017-10-09T12:10:00.776594Z', 'toy_category': 'Playset', 'was_included_in_home': False}

In[77]: if new_toy_serializer.is_valid():
    ...: print(type(new_toy_serializer.data))
    ...:
<class 'rest_framework.utils.serializer_helpers.ReturnDict' >


if new_toy_serializer.is_valid():
    toy3 = new_toy_serializer.save()
    print(toy3.name)

In[81]: if new_toy_serializer.is_valid():
    ...: print(type(new_toy_serializer.validated_data)
               ...:
               ...:
               ...:)
    ...:
    ...:
<class 'collections.OrderedDict' >
