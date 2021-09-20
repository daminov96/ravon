import grpc
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service

from apps.app.serializers import TripSerializer
from apps.custom_endpoint_app.views import cast_json
from apps.real_time.consumers import TripConsumer
from google.protobuf.json_format import MessageToDict


class NewTripService(Service):
    def Signal(self, request, context):
        print(request)
        order = MessageToDict(request, False, True)

        TripConsumer().send_new_order_alert_to_drivers(order)
        return empty_pb2.Empty()