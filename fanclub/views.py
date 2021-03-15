from django.db.models import query
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import viewsets
from fanclub import models
from fanclub import serializers
from django.contrib.auth.models import User
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView
from rest_framework.decorators import action
from rest_auth.registration.serializers import SocialLoginSerializer
from rest_framework.decorators import action
from django.db.models import Q
from rest_framework.response import Response
# Create your views here.

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializers
    filter_backends = [DjangoFilterBackend ,filters.SearchFilter]
    search_fields = ['username', 'email']

class ChatroomViewSet(viewsets.ModelViewSet):
    queryset = models.Chatroom.objects.all()
    serializer_class = serializers.ChatroomSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['members', 'admins', 'creater', 'created_at', 'type', 'name']
    search_fields = ['name']

    @action(methods=['get', ], detail=False, url_path='userGroups', url_name='userGroups')
    def get_user_groups(self, request):
        groups = models.Chatroom.objects.filter(Q(admins=request.user) | Q(creater=request.user) | Q(members=request.user))
        serializer = serializers.ChatroomSerializers(groups, many=True)
        return Response(serializer.data)

    @action(methods=['patch', ], detail=True, url_path='updateadmins', url_name='updateadmins')
    def updateAdmins(self, request, pk):
        group = models.Chatroom.objects.get(pk = pk)
        admin_array = request.data.get('admin_array')
        newAdmin = []
        for element in admin_array:
            temp = models.User.objects.get(pk = element)
            newAdmin.append(temp)
        group.admins.set(newAdmin)
        group.save()
        serializer = serializers.ChatroomSerializers(group)
        return Response(serializer.data)

    @action(methods=['patch', ], detail=True, url_path='updatemember', url_name='updatemember')
    def updateMembers(self, request, pk):
        group = models.Chatroom.objects.get(pk = pk)
        member_array = request.data.get('member_array')
        newMember = []
        for element in member_array:
            temp = models.User.objects.get(pk = element)
            newMember.append(temp)
        group.members.set(newMember)
        group.save()
        serializer = serializers.ChatroomSerializers(group)
        return Response(serializer.data)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = models.Messages.objects.all()
    serializer_class = serializers.MessageSerializers

class BioViewSet(viewsets.ModelViewSet):
    queryset = models.Bio.objects.all()
    serializer_class = serializers.BioSerializers    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['user']
    search_fields = ['user']