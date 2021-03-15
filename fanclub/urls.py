from typing import DefaultDict
from django.urls import path, include
from fanclub import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'chatroom', views.ChatroomViewSet)
router.register(r'messages', views.MessageViewSet)
router.register(r'bio', views.BioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth-social/facebook/', views.FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth-social/google/', views.GoogleLogin.as_view(), name='google_login'),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^accounts/', include('allauth.urls'), name='socialaccount_signup'),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]