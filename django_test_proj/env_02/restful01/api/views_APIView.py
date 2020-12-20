# serializers enabled views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SubscriberSerializer
from .models import Subscriber



class SubscriberView(APIView):

    # HelloWorldView extends APIView, and overrides the get method

    def get(self, request):
        #return Response({"message": "Hello World!"})
        # fetching all subscribers and pass the queryset to serializer constructor,
        # since we pass a list of model instances, we need to set many=True.
        # We don't need to call is_valid since the data comes from database, they are
        # already valid.
        all_subscribers = Subscriber.objects.all() # all_subscribers is a queryset
        serialized_subscribers = SubscriberSerializer(all_subscribers, many=True)
        return Response(serialized_subscribers.data)


    def post(self, request):
        # name = request.data.get("name")
        # if not name:
        #     return Response({"error": "No name passed"})
        # return Response({"message": "Hello {}!".format(name)})

        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            #valid_data = serializer.data
            subscriber_instance = Subscriber.objects.create(**serializer.data)
            return Response({"message": "Created subscriber {}".format(subscriber_instance.id)})

            # name = valid_data.get("name")
            # age = valid_data.get("age")
            # return Response({"message": "Hello {}, you're {} years old".format(name, age)})
        return Response({"error": serializer.errors})

    # # localhost:8000/api/hello
    # {
    #     "name": "Crappy Morning",
    #     "age": 59
    # }
    #output
    # {
    #     "message": "Hello Crappy Morning, you're 59 years old"
    # }


