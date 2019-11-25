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
router.register(r'users', usersviews.UserViewSet)
router.register(r'groups', usersviews.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Videofeed Related Views
    path('api/videos/recommendation', videofeedviews.RecommendYouTubeVideo.as_view()),
    path('api/videos/recommendation/share', videofeedviews.ShareRecommendation.as_view()),
    path('api/videos/recommendation/notifications', videofeedviews.Notifications.as_view()),
    # User Related Views
    path('api/users/follow', usersviews.Follow.as_view()),
    path('api/', include(router.urls))
]
