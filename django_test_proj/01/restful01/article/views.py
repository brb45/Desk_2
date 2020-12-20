from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Article
from .serializers import ArticleSerializer
from django.shortcuts import get_list_or_404, get_object_or_404


class ArticleView(APIView):
    # [26/Jun/2019 11:25:45] "GET /api/articles/ HTTP/1.1" 200 5202
    def get(self, request):
        articles = Article.objects.all()
        # without creating serializers
        # return Response({"articles": articles})

        # Add serializers to convert python object instance (articles) into JSON string
        # two steps , first serializer convert object tributes into dict , or list
        # 2. convert JSON - ready python types to JSON string
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles_100": serializer.data})

    #
    # the list of articles is trying to be serialized/converted from an object into JSON.
    # If no class is created to serialize the Article objects, there will be error.
    # need to create an serializers.py
# Serializers allow complex data such as querysets and model instances to be converted
# to native Python datatypes that can then be easily rendered into JSON, XML
# or other content types.

# GET /api/articles/
# HTTP 200 OK
# Allow: GET, HEAD, OPTIONS
# Content-Type: application/json
# Vary: Accept
#
# {
#     "articles": []
# }
    # Create
    def post(self, request):
        article = request.data.get('article')

        # Create an article from the above data
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})

    # update
    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        #return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})
        return Response({"success": "Article '{}' updated successfully".format(article_saved.body)})

    # delete
    def delete(self, request, pk):
        # Get object with this pk
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)}, status=204)
