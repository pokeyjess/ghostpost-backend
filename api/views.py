from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import PostSerializer
from ghostpost.models import Posts

# https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing

class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    
    @action(detail=True, methods=['get'])
    def up_vote(self, request, pk=None):
        vote = Posts.objects.get()
        vote.total_votes += 1
        vote.save()
        return Response(vote.total_votes)
        
    @action(detail=True, methods=['get'])
    def down_vote(self, request, pk=None):
        vote = Posts.objects.get()
        vote.total_votes -= 1
        vote.save()
        return Response(vote.total_votes)
    