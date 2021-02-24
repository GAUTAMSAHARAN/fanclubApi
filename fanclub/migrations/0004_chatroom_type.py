# Generated by Django 3.1.5 on 2021-02-17 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanclub', '0003_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='type',
            field=models.CharField(choices=[('Movies', 'M'), ('Coding', 'C'), ('Study', 'S')], default='Movies', max_length=50),
        ),
    ]