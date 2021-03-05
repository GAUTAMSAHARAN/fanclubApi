import asyncio
import json
import io
from json.decoder import JSONDecodeError
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from fanclub import models, serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.group_id = int(self.room_name)
        group = models.Chatroom.objects.get(pk = self.group_id)
        self.access = []
        for user in group.members.all():
            self.access.append(user)
        for user in group.admins.all():
            self.access.append(user)
        self.access.append(group.creater)
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code=None):
        # Leave room group
        self.send(json.dumps({"end_message": close_code}))
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        self.close()

    def init_chat(self, data):
        user_id = data['userid']
        user = models.User.objects.get(pk = user_id)
        content = {
               'command': 'init_chat',
        }
        if user in self.access:
            content['error'] = 'sorry, Your request is not processed right now. Please try again later!'
            self.send_message(content)
        else:
            print('false')
            self.disconnect('Sorry, this user is not allowed to acces this chat')


    def fetch_messages(self, data2):
        group = None
        try:
            group = models.Chatroom.objects.get(pk = self.group_id)
        except:
            self.disconnect('Group does not exist')

        messages = group.room_chat.all()
        serialized_messages = serializers.MessageSerializers(messages, many=True).data
        info = JSONRenderer().render(serialized_messages)
        stream = io.BytesIO(info)
        data = JSONParser().parse(stream)
        content = {
            'command': 'messages',
            'messages': data
        }
        user_id = data2['userid']
        user = models.User.objects.get(pk = user_id)
        if user in self.access:
            self.send_message(content)
        else:
            self.disconnect('sorry, you are not allowed to access the chat')

    def new_message(self, data):
        text = data['text']
        group = models.Chatroom.objects.get(pk = self.group_id)
        creater_user = models.User.objects.get(pk = data['userId'])

        if creater_user in self.access:
            message = models.Messages.objects.create(writer = creater_user, message = text, room=group)
            content = {
                'command': 'new_message',
                'message': self.message_to_json(message)
            }
            self.send_chat_message(content)
        else:
            self.disconnect('Sorry, you are not allowed to send msg in this group')

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return {
            'id': str(message.id),
            'creater': message.writer.id,
            'message': message.message, 
            'group': message.room.id,
        }

    commands = {
        'init_chat': init_chat,
        'fetch_messages': fetch_messages,
        'new_message': new_message,
    }

    # Receive message from WebSocket

    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_message(self, content):
        self.send(text_data=json.dumps(content))

    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))