from django.db.models import query
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import viewsets
from fanclub import models
from fanclub import serializers
from django.contrib.auth.models import User
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializers
    filter_backends = [DjangoFilterBackend ,filters.SearchFilter]
    search_fields = ['username', 'email']

class ChatroomViewSet(viewsets.ModelViewSet):
    queryset = models.Chatroom.objects.all()
    serializer_class = serializers.ChatroomSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['members', 'admins', 'creater', 'created_at', 'type']
    search_fields = ['name']

class MessageViewSet(viewsets.ModelViewSet):
    queryset = models.Messages.objects.all()
    serializer_class = serializers.MessageSerializers

class FriendViewSet(viewsets.ModelViewSet):
    queryset = models.Friends.objects.all()
    serializer_class = serializers.FriendSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sender', 'receiver']