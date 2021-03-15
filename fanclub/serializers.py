from django.db.models import fields
from rest_framework import serializers
from fanclub import models
from django.contrib.auth.models import User

class BioSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Bio
        fields = "__all__"

class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username', 'email', 'password']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ChatroomSerializers(serializers.ModelSerializer):
    admins = UserSerializers(many=True, read_only=True)
    members = UserSerializers(many=True, read_only=True)
    class Meta:
        model = models.Chatroom
        fields = ['id', 'name', 'desc', 'type', 'created_at', 'admins', 'members', 'icon', 'cover', 'creater']

class MessageSerializers(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = models.Messages
        fields = ['id', 'message', 'created_at', 'writer', 'room', 'username', 'imageMsg']

    def get_username(self, messages):
        username = messages.writer.username
        return username


