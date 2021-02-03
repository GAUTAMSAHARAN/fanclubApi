from django.db.models import query
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import viewsets
from fanclub import models
from fanclub import serializers
from django.contrib.auth.models import User
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializers

class ChatroomViewSet(viewsets.ModelViewSet):
    queryset = models.Chatroom.objects.all()
    serializer_class = serializers.ChatroomSerializers

class MessageViewSet(viewsets.ModelViewSet):
    queryset = models.Messages.objects.all()
    serializer_class = serializers.MessageSerializers