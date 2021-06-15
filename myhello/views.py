#from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from .models import API
import json
import logging

# Create your views here.
logger = logging.getLogger('django')

@api_view(['GET'])
def add_api(request):
    title = request.GET.get('title', '')
    content = request.GET.get('content', '')
    photo = request.GET.get('photo', '')
    location = request.GET.get('location', '')

    new_post = API()
    new_post.id = id
    new_post.title = title
    new_post.classify = classify
    new_post.descrption = descrption
    new_post.picture = picture
    new_post.poblish = poblish
    new_post.save()
    logger.debug(" *************** myhello_api: " + title)
    if title:
        return Response({"data": title + " insert!"}, status = status.HTTP_200_OK)
    else:
        return Response(
            {"res": "parameter: name is None"}, 
            status = status.HTTP_400_BAD_request
        )

@api_view(['GET'])
def list_api(request):
    posts = Post.objects.all().values()
    # return JsonResponse(list(posts), safe=False)
    return Response({"data":
        json.dumps(
            list(posts),
            sort_keys = True,
            indent = 1,
            cls = DjangoJSONEncoder)},
        status = status.HTTP_200_OK
    )
