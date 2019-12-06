from django.db import models
from django.contrib.auth.models import User, Group


class ProfileManager(models.Manager):
    def create_profile(self, user, profile):
        profile = self.create(user=user, profile=profile)
        return profile

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.CharField(max_length=500, blank=True)

    objects = ProfileManager()

class Follower(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers') 
