from typing import DefaultDict
from django.urls import path, include
from fanclub import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'chatroom', views.ChatroomViewSet)
router.register(r'messages', views.MessageViewSet)
router.register(r'friends', views.FriendViewSet)

urlpatterns = [
    path('', include(router.urls)),
]