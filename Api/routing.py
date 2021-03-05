from django.conf.urls import url
from fanclub import consumers

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/(?P<user_id>[^/]+)$', consumers.ChatConsumer.as_asgi()),
]


