from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Chatroom(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)
    creater = models.ForeignKey(User, related_name='my_rooms', on_delete=models.CASCADE)
    admins = models.ManyToManyField(User, related_name='admin_rooms')
    members = models.ManyToManyField(User, related_name="joined_rooms")

class Messages(models.Model):
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(User, related_name="my_messages", on_delete=models.CASCADE)
    room = models.ForeignKey(Chatroom, related_name="room_chat", on_delete=models.CASCADE)