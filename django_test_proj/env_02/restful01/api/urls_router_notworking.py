# urls using Router
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import SubscriberViewSet

router = SimpleRouter()
router.register(r"subscribers", SubscriberViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     #url(r'hello', hello_world, name="hello_world")  #http://localhost:8000/api/hello
#     url(r"subscriber", include(router.urls))
# ]

# urlpatterns = [
#     #url(r'hello', hello_world, name="hello_world")  #http://localhost:8000/api/hello
#     url("subscriber", SubscriberView.as_view(), name="Subscripber")
# ]

