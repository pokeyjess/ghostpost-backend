from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import PostSerializer
from ghostpost.models import Posts

class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

