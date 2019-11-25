from django.contrib.auth.models import User, Group
from rest_framework import serializers

from users.models import Follower


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# TODO(hyunminch): implement
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
