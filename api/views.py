from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import PostSerializer
from ghostpost.models import Posts

# https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing

# https://stackoverflow.com/questions/22063748/django-get-returned-more-than-one-topic
# https://docs.djangoproject.com/en/3.1/ref/class-based-views/mixins-single-object/

class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by('-post_time')
    serializer_class = PostSerializer
 
    @action(detail=True, methods=['get'])
    def up_vote(self, request, pk=None):
        vote = self.get_object()
        vote.total_votes += 1
        vote.save()
        return Response(vote.total_votes)
        
    @action(detail=True, methods=['get'])
    def down_vote(self, request, pk=None):
        vote = self.get_object()
        vote.total_votes -= 1
        vote.save()
        return Response(vote.total_votes)

    @action(detail=False)
    def boasts(self, request):
        boasts = Posts.objects.filter(boast_or_roast=True)
        serializer = self.get_serializer(boasts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roasts(self, request):
        roasts = Posts.objects.filter(boast_or_roast=False)
        serializer = self.get_serializer(roasts, many=True)
        return Response(serializer.data)
    

