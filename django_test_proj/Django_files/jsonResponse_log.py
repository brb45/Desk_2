# JsonResponse class, a subclass of HttpResponse.
# Its default Content-Type is set to application/json
# ex1.

from django.http import JsonResponse
# By default, JsonResponse's first parameter, data, should be a dict instance. To pass any other Json-serializable
# object, you must set the safe parameter to False.

# class JsonResponse(data, encoder, safe, json_dumps_params, **kwargs)
def profile(request):
    data = {
        'name': 'Victor',
        'location': 'Campbell',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data)

# print(profile(None))