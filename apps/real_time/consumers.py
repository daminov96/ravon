# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from rest_framework import response

from channels.db import database_sync_to_async
# from .serializers import MessageSerializer, RoomSerializer
from django.db.models import Q
from rest_framework import status
from django.contrib.gis.measure import D
from django.contrib.gis.geos import *
from apps.account_account.models import CustomUser, CurrentLocationOfDriver
from channels.layers import get_channel_layer

CREATE_ACTION_TYPE = 'create'
CONNECT_ACTION_TYPE = 'connect'
GET_ACTIVE_ROOM = 'get_active_room'
EDIT_ACTION_TYPE = 'edit'
DELETE_ACTION_TYPE = 'delete'
TEXT_MESSAGE_TYPE = 'text'
IMAGE_MESSAGE_TYPE = 'image'


# data = {
#     'type': 'chat_message',
#     'message': {
#         "action_type": text_data["action_type"],
#         "event_type": text_data["event_type"],
#         "message_type": text_data["message_type"],
#     }
# }


class TripConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.rooms = []
        self.user = self.scope['user']
        print("connet")
        print(self.user)
        if self.user.is_anonymous:
            await self.close()
        await self.room({'user': self.user})
        print("after await")
        for i in self.rooms:
            await self.channel_layer.group_add(
                group=i,
                channel=self.channel_name
            )
        print("after for")
        await self.accept()

    @database_sync_to_async
    def room(self, text_data=None):
        self.rooms.append(f'chat_user_{self.user.id}')

    def disconnect(self, close_code):
        # Leave room group
        for room in self.rooms:
            self.channel_layer.group_discard(
                room,
                self.channel_name
            )

    async def send_new_order_alert_to_drivers(self, order):
        rooms = await self.get_nearest_available_drivers(order['from_point'])
        data = {
            'type': 'chat_message',
            'message': {
                "order": order
            }
        }
        for i in rooms:
            await self.channel_layer.group_send(
                i,
                data
            )

    @database_sync_to_async
    def get_nearest_available_drivers(self, from_location=None):
        pnt = fromstr(f"POINT({float(from_location['lat'])} {float(from_location['long'])} )", srid=32140)
        qs = CurrentLocationOfDriver.objects.filter(point__distance_lte=(pnt, D(km=20)), driver__is_online=True,
                                                    driver__is_busy=False)
        rooms = []
        rooms.append(f'chat_user_1')
        for i in qs:
            rooms.append(f'chat_user_{i.id}')
        return rooms

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = await self.define_action_and_message_type_call_proper_function(text_data_json)
        if message['data']['message']['event_type'] == 'message':
            await self.channel_layer.group_send(
                "chat_%s" % message['room_name'],
                message['data']
            )
        elif message['data']['message']['event_type'] == 'room':
            if message['data']['message']['action_type'] == 'create':
                if not message['data']['message']['message'].get('success', None):
                    for i in message['data']['message']['message'].get('subscribers'):
                        print(i)
                        await self.channel_layer.group_send(
                            f"chat_user_{i.get('id')}",
                            message['data']
                        )
                else:
                    await self.channel_layer.group_send(
                        "chat_user_%s" % self.user.id,
                        message['data']
                    )

            elif message['data']['message']['action_type'] == 'connect':
                await self.channel_layer.group_send(
                    "chat_user_%s" % self.user.id,
                    message['data']
                )
            elif message['data']['message']['action_type'] == GET_ACTIVE_ROOM:
                await self.channel_layer.group_send(
                    "chat_user_%s" % self.user.id,
                    message['data']
                )

    def define_action_and_message_type_call_proper_function(self, text_data):
        # if text_data['event_type'] == 'message':
        #     if text_data['action_type'] == CREATE_ACTION_TYPE:
        #         if text_data["message_type"] == TEXT_MESSAGE_TYPE:
        #             return self.save_message(text_data)
        #         if text_data["message_type"] == IMAGE_MESSAGE_TYPE:
        #             return self.get_message(text_data)
        #     elif text_data['action_type'] == DELETE_ACTION_TYPE:
        #         return self.delete_message(text_data)
        #     elif text_data['action_type'] == EDIT_ACTION_TYPE:
        #         return self.edit_message(text_data)
        # elif text_data['event_type'] == 'room':
        #     if text_data['action_type'] == CREATE_ACTION_TYPE:
        #         return self.save_room(text_data)
        #     elif text_data['action_type'] == CONNECT_ACTION_TYPE:
        #         return self.connect_to_room(text_data)
        #     elif text_data['action_type'] == GET_ACTIVE_ROOM:
        #         return self.get_active_room(text_data)
        #     elif text_data['action_type'] == EDIT_ACTION_TYPE:
        #         return self.edit_message(text_data)

        return ""

    # Receive message from room group
    async def chat_message(self, event):
        print("message event")
        message = event['message']
        await self.send(text_data=json.dumps(message))


expected_style_of_request = {
    "event_type": ['room', 'message'],
    "action_type": ["create", 'delete', 'edit', 'connect', 'get_active_room'],
    "message_type": ["text", "image"],
    "message": {
        "owner": 1,
        "text": "asgad",
        "room": 1
    }
}