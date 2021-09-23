# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/second/', consumers.TripConsumer.as_asgi()),
    # re_path(r'ws/chat/second/(?P<username>\w+)/(?P<type>\w+)', consumers.ChatConsumer.as_asgi()),
]
