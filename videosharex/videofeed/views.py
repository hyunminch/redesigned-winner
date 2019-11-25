from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from videofeed.models import YouTubeVideoRecommendation
from videofeed.serializers import YouTubeVideoRecommendationSerializer, YouTubeVideoRecommendationShareSerializer


class Notifications(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

class ShareRecommendation(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        request.data['sharer'] = request.user.id
        serializer = YouTubeVideoRecommendationShareSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecommendYouTubeVideo(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        recommendations = YouTubeVideoRecommendation.objects.order_by('-id')
        serializer = YouTubeVideoRecommendationSerializer(recommendations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        request.data['poster'] = request.user.id
        serializer = YouTubeVideoRecommendationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
