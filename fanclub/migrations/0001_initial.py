# Generated by Django 3.1.5 on 2021-02-03 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('admins', models.ManyToManyField(related_name='admin_rooms', to=settings.AUTH_USER_MODEL)),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_rooms', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='joined_rooms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_chat', to='fanclub.chatroom')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
