from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse


# Instead of the usual HttpResponse, we used JsonResponse because we want to render our response
# as JSON. Using this class ensures that the reponse is JSON and the appropriate content type is set.
def hello_world(request):
    return JsonResponse({"message": "Hello World!"})