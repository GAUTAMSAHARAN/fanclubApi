from django.db.models import fields
from rest_framework import serializers
from fanclub import models
from django.contrib.auth.models import User

class ChatroomSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Chatroom
        fields = "__all__"

class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Messages
        fields = "__all__"

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"