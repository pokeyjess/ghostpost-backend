from rest_framework import serializers
from ghostpost.models import Posts

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id', 'boast_or_roast', 'content', 'up_votes', 'down_votes', 'post_time']

