from django.db import models

# Create your models here.
class Toy(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=False, default='')
    description = models.CharField(max_length=250, blank=True, default='')
    toy_category = models.CharField(max_length=200, blank=False, default='')
    release_date = models.DateTimeField()
    was_included_in_home = models.BooleanField(default=False)


    class Meta:
        ordering = ('name',)


# >>> from datetime import datetime
# >>> from django.utils import timezone
# >>> from django.utils.six import BytesIO
# >>> from rest_framework.renderers import JSONRenderer
# >>> from rest_framework.parsers import JSONParser
# >>> from toys.models import Toy
# >>> from toys.serializers import ToySerializer
# >>> toy_release_date = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
# >>> toy1 = Toy(name='Snoopy talking action figure', description='Snoopy speaks five languages', release_date=toy_release_date, toy_category='Action figures', was_included_in_home=False)
# >>> toy1.save()
# >>> toy2 = Toy(name='Hawaiian Barbie', description='Barbie loves Hawaii', release_date=toy_release_date, toy_category='Dolls', was_included_in_home=True)
# >>> toy2.save()

# In [1]: from datetime import datetime
#
# In [2]: from django.utils import timezone
#
# In [3]: from django.utils.six import BytesIO
#
# In [4]: from rest_framework.renderers import JSONRenderer
#
# In [5]: from rest_framework.parsers import JSONParser
#
# In [6]: from toys.models import Toy
#
# In [7]: from toys.serializers import ToySerializer
#
# In [8]: rd = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
#
# In [9]: t = Toy(name="System Test fundamental",description="wifi",release_date=rd, toy_category="Text",was_included_in_home=False)
#
# In [10]: t.save()

# {
#     "id": 7,
#     "name": "System Test fundamental",
#     "description": "wifi",
#     "release_date": "2019-06-28T15:50:22.706195Z",
#     "toy_category": "Text",
#     "was_included_in_home": false
# },