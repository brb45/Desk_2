#1.
# from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# def lenses(request):
#     if request.method == 'GET':
#         arguments = {}
#         for k, v in request.GET.items():
#             if v:
#                 arguments[k] = v
#         l = Lens.objects.filter(**arguments)
#         serializer = LensSerializer(l, many=True)
#         return JSONResponse(serializer.data)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = LensSerializer(data=data, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=201)
#
#         return JSONResponse(serializer.errors, status=400)
# 2.
# A JSONRenderer converts the request data into JSON using utf-8 encoding. Normally we use this when
# we want our data to be streamable.

python_dict = {'cal_id': u'2', 'username': u'tester'}
# json_string = JSONRenderer().render(python_dict)
# print("json_string is of type: {}".format(type(json_string)))
# print("json_stirng is ", json_string)
