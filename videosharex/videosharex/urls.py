"""videosharex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users import views as usersviews
from videofeed import views as videofeedviews


router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    # Videofeed Related Views
    path('api/videos/recommendation', videofeedviews.RecommendYouTubeVideo.as_view()),
    path('api/videos/recommendation/share', videofeedviews.ShareRecommendation.as_view()),
    path('api/videos/recommendation/notifications', videofeedviews.Notifications.as_view()),
    # User Related Views
    path('api/users', include(router.urls)),
    path('api/users/signup', usersviews.SignUp.as_view()),
    path('api/users/signin', usersviews.SignIn.as_view()),
    path('api/users/profile', usersviews.ProfileView.as_view()),
    path('api/users/profile/public', usersviews.PublicProfileView.as_view()),
    path('api/users/follow', usersviews.Follow.as_view()),
    path('api/users/following', usersviews.Following.as_view()),
    path('api/users/followers', usersviews.Followers.as_view())
]
