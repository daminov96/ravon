import grpc
from django.shortcuts import render
from rest_framework.views import APIView
import rest_framework.permissions as permissions

from apps.generated.trip.protos import trip_pb2, trip_pb2_grpc


class OrderList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = self.request.user
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = trip_pb2_grpc.TripControllerStub(channel)
            trip_list_request = trip_pb2.TripListRequest()
            trip_list_request.driver = user.uuid
            for user in stub.List(trip_pb2.TripListRequest()):
                print(user, end='')
