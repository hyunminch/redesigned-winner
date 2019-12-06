from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from users.models import Profile
from users.serializers import UserSerializer, ProfileSerializer, GroupSerializer, FollowerSerializer


class SignUp(APIView):
    def post(self, request, format=None):
        name = request.data['username']
        # email = request.data['email']
        password = request.data['password']

        user = User.objects.create_user(name, '', password)
        profile = Profile.objects.create_profile(user, "")

        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)

class SignIn(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        return Response()


class ProfileView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = ProfileSerializer(request.user.profile)
        return Response(serializer.data)

    def post(self, request, format=None):
        profile = request.user.profile
        profile.profile = request.data['profile']
        profile.save()

        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    
class Follow(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        request.data['follower'] = request.user.id
        serializer = FollowerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Following(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        following = request.user.following.all()
        serializer = FollowerSerializer(following, many=True)
        return Response(serializer.data)

class Followers(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        followers = request.user.followers.all()
        serializer = FollowerSerializer(followers, many=True)
        return Response(serializer.data)
