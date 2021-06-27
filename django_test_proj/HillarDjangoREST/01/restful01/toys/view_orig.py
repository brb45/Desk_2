
## Original view
# (JSON stirng) ->JSONParser ->  Python data type( dict, list);->de-serializer(python datatype)->python Object instance, -> saved in database directly
# Retrieve(database)-> Python Object instance -> serializer-> Python data type -> JSONRenderer(python datatype) -> JSON string -> API to send
from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Toy
from .serializers import ToySerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs): # data is in python dict data type
        content = JSONRenderer().render(data)  # JSON string
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def toy_list(request):
    if request.method == 'GET': # use serializer
        toys = Toy.objects.all() # Model instance / python object
        toys_serializer = ToySerializer(toys, many=True) # python dictionary data type
        return JSONResponse(toys_serializer.data)  # http response
    elif request.method == 'POST': # use de-serializer
        toy_data = JSONParser().parse(request)  # Python dict data type
        toy_serializer = ToySerializer(data=toy_data)  # Python object, model instance
        if toy_serializer.is_valid():
            toy_serializer.save()
            return JSONResponse(toy_serializer.data, \
                status=status.HTTP_201_CREATED)
        return JSONResponse(toy_serializer.errors, \
            status=status.HTTP_400_BAD_REQUEST)

# example of request = GET localhost:8000/toys/
# GET localhost:8000/toys/      will call toy_list(request)
@csrf_exempt
def toy_detail(request, pk):
    try:
        toy = Toy.objects.get(pk=pk)
    except Toy.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        toy_serializer = ToySerializer(toy)
        return JSONResponse(toy_serializer.data)
    elif request.method == 'PUT':
        toy_data = JSONParser().parse(request)
        toy_serializer = ToySerializer(toy, data=toy_data)
        if toy_serializer.is_valid():
            toy_serializer.save()
            return JSONResponse(toy_serializer.data)
        return JSONResponse(toy_serializer.errors, \
            status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        toy.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
