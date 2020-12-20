from datetime import datetime
from django.utils import timezone
from django.utils.six import BytesIO
# from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
from .models import Toy
from .serializers import ToySerializer
# rd = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
# t = Toy(name="System Test fundamental",description="wifi",release_date=rd, toy_category="Text",was_included_in_home=False)
# t.save()
Toy.objects.filter(pk=1).values()
Toy.objects.values()
a = Toy.objects.filter(pk=2).values()
type(a)
a[0]

Toy.objects.all.values()
Toy.objects.all().values()
Toy.objects.all().values('name')
Toy.objects.all()

# a = Toy.objects.filter(pk=2).values()
#
# In [14]: type(a)
# Out[14]: django.db.models.query.QuerySet
#
# In [15]: a[0]
# Out[15]:
# {'id': 2,
#  'created': datetime.datetime(2019, 5, 15, 0, 45, 50, 828926, tzinfo=<UTC>),
#  'name': 'Hawaiian Barbie',
#  'description': 'Barbie loves Hawaii',
#  'toy_category': 'Dolls',
#  'release_date': datetime.datetime(2019, 5, 14, 17, 42, 13, 29376, tzinfo=<UTC>),
#  'was_included_in_home': True}

# In [23]: Toy.objects.all().values('name')
# Out[23]: <QuerySet [{'name': 'Clash Royale play set'}, {'name': 'Formal Test Methodology'},
#                     {'name': 'Hawaiian Barbie'}, {'name': 'Snoopy talking action figure'},
#                     {'name': 'System Test fundamental'}, {'name': 'Wonderboy puzzle'}]>

# 1. QuerySet: returns a QuerySet of Toy instances,
queryset = Toy.objects.all() # It won't hit the database,
# Out[26]: <QuerySet [<Toy: Toy object>, <Toy: Toy object>, <Toy: Toy object>,
# <Toy: Toy object>, <Toy: Toy object>, <Toy: Toy object>]>

#
##