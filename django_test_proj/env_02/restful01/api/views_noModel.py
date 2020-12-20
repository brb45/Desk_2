# serializers enabled views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelloWorldSerializer

class HelloWorldView(APIView):

    # HelloWorldView extends APIView, and overrides the get method
    def get(self, request):
        return Response({"message": "Hello World!"})

    def post(self, request):
        # name = request.data.get("name")
        # if not name:
        #     return Response({"error": "No name passed"})
        # return Response({"message": "Hello {}!".format(name)})

        serializer = HelloWorldSerializer(data=request.data)
        if serializer.is_valid():
            valid_data = serializer.data

            name = valid_data.get("name")
            age = valid_data.get("age")
            return Response({"message": "Hello {}, you're {} years old".format(name, age)})
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


