from rest_framework import serializers
from ghostpost.models import Posts

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ['id', 'boast_or_roast', 'content', 'total_votes', 'post_time']

