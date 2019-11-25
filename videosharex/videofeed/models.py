from django.db import models
from django.contrib.auth.models import User, Group


class YouTubeVideoRecommendation(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.CharField(max_length=16)
    text = models.CharField(max_length=120, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class YouTubeVideoRecommendationShare(models.Model):
    sharer = models.ForeignKey(User, on_delete=models.CASCADE)
    recommendation = models.ForeignKey(YouTubeVideoRecommendation, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
