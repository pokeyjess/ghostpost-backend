from django.db import models

from django.utils import timezone

class Posts(models.Model):
    boast_or_roast = models.BooleanField()
    content = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)
    post_time = models.DateTimeField(default=timezone.now)

    
