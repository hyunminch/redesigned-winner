from django.contrib.auth.models import User, Group
from rest_framework import serializers

from users.models import Profile, Follower


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Profile

class FollowerSerializer(serializers.ModelSerializer):
    follower = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    followed = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def get_follower(self, obj):
        return obj.follower.username

    def get_followed(self, obj):
        return obj.followed.username

    class Meta:
        fields = '__all__'
        model = Follower 
