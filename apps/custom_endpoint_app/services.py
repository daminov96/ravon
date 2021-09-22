import grpc
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service

from apps.app.serializers import TripSerializer
from apps.custom_endpoint_app.views import cast_json
from apps.real_time.consumers import TripConsumer
from google.protobuf.json_format import MessageToDict
from channels.generic.websocket import AsyncWebsocketConsumer

from channels.layers import get_channel_layer

from asgiref.sync import async_to_sync



class NewTripService(Service):
    def Signal(self, request, context):
        print('keldi')
        order = MessageToDict(request, False, True)
        trip_consumer = TripConsumer()
        trip_consumer.channel_layer=get_channel_layer()
        async_to_sync(trip_consumer.send_new_order_alert_to_drivers)(
           order
        )
        # trip_consumer.resend()
        # async_to_sync(get_channel_layer().group_send)("chat_user_1",{})
        # get_channel_layer().group_send(
        #     'chat_user_1',
        #     {"type": "forward_group_message", "data": order}
        # )
        # await trip_consumer.connect()
        # await trip_consumer.send_new_order_alert_to_drivers(order)
        return empty_pb2.Empty()
