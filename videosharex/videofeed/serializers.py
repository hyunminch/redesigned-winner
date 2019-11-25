from django.contrib.auth.models import User
from rest_framework import serializers

from videofeed.models import YouTubeVideoRecommendation, YouTubeVideoRecommendationShare


class YouTubeVideoRecommendationSerializer(serializers.ModelSerializer):
    poster = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    username = serializers.SerializerMethodField()
    
    def get_username(self, obj):
        return obj.poster.username

    class Meta:
        fields = '__all__'
        model = YouTubeVideoRecommendation

class YouTubeVideoRecommendationShareSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='id', read_only=True)
    sharer = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    recommendation = serializers.PrimaryKeyRelatedField(queryset=YouTubeVideoRecommendation.objects.all())

    class Meta:
        fields = '__all__'
        model = YouTubeVideoRecommendationShare
