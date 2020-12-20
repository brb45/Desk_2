# Using APIView,
# APIView is very similar to Django's View class,but it has methods for the HTTP verbs.

from rest_framework.views import APIView
from rest_framework.response import Response

# function-based APIView
# @api_view(["GET", "POST"])
# def hello_world(request):
#     if request.method == "GET":
#         return Response({"message": "Hello World!"})
#
#     else:
#         name = request.data.get("name")
#         if not name:
#             return Response({"error": "No name passed"})
#         return Response({"message": "Hello {}!".format(name)})

# class-based APIView
class HelloWorldView(APIView):

    # HelloWorldView extends APIView, and overrides the get method
    def get(self, request):
        return Response({"message": "Hello World!"})
    # We returns an instance of the Response class, DRF will do the content
    # negotiation for us and it will render the response in the correct format
    # We don't need to worry about rendering JSON/XML any more

    # Accepting Input
    # We must learn how to handle inputs from user, on our /api/hello endpoint, we would
    # acceppt a name in a POST request. If the name is passed, we will show a customize greeting.

    # post function to handle POST request. We use request.data, which works on POST, PUT, and PATCH.

    def post(self, request):
        name = request.data.get("name")
        if not name:
            return Response({"error": "No name passed"})
        return Response({"message": "Hello {}!".format(name)})


# ##################################################################################

    # http: // localhost:8000/api/ hello
    # Hello  World
    #
    # GET / api / hello
    # HTTP 200 OK
    # Allow: GET, HEAD, OPTIONS
    # Content - Type: application / json
    # Vary: Accept
    #
    # {
    #     "message": "Hello World!"
    # }

    # We import the class based view and call the as_view method on it to return a view that Django can deal with.
    # Under the hood, the as_view class method works as an entry point for the request.
    # The class inspects the request and properly dispatches to the get, post, put etc methods to process the request.
    # It then takes the result and sends back like a normal function based view would do.
    # In short, the as_view method kind of works as a bridge between the class based view and
    # the function based views commonly used with Django.

    # APIView presents a nice HTML view with our json response, called web Browsable API

    # if you visit http://localhost:8000/api/hello, you will now see a nice html view
    # with our json response displayed along with other useful information (response headers).This html view is an
    # excellent feature of DRF – it’s called the web browsable API.The APIs we create, DRF automagically
    # generates a web view for us from where we can interact with our API,
    # testing / debugging things.No need for swagger or any other external clients for testing.

    ################
    # localhost: 8000/api/hello?name =rest_framework
    # {
    #     "message": "Hello rest_framework!"
    # }