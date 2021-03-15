from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.
class Chatroom(models.Model):
    name = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    TYPE_CHOICES=[
        ('Movies', 'M'),
        ('Coding', 'C'),
        ('Study', 'S'),
    ]
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Movies')
    desc = models.CharField(max_length=100, blank=True)
    creater = models.ForeignKey(User, related_name='my_rooms', on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='group_icon', blank=True)
    cover = models.ImageField(upload_to='group_cover', blank=True)
    admins = models.ManyToManyField(User, related_name='admin_rooms', blank=True)
    members = models.ManyToManyField(User, related_name="joined_rooms", blank=True)

class Messages(models.Model):
    message = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    imageMsg = models.ImageField(upload_to='msg_image', blank=True)
    writer = models.ForeignKey(User, related_name="my_messages", on_delete=models.CASCADE)
    room = models.ForeignKey(Chatroom, related_name="room_chat", on_delete=models.CASCADE)


class Bio(models.Model):
    bio = models.CharField(max_length=100, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True) # validators should be a list   
    user = models.OneToOneField(User, related_name="user_data", on_delete=models.CASCADE)