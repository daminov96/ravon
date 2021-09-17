import grpc
from django.shortcuts import render
from rest_framework.views import APIView
import rest_framework.permissions as permissions

from apps.generated.trip.protos import trip_pb2, trip_pb2_grpc
from rest_framework.response import Response
import rest_framework.status  as status


class OrderList(APIView):
    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print('ad')
        user = self.request.user
        with grpc.insecure_channel('localhost:50051') as channel:
            print('tushdimiaaa')
            stub = trip_pb2_grpc.TripControllerStub(channel)
            trip_list_request = trip_pb2.TripListRequest()
            trip_list_request.driver = "asdfasdfa"
            users = []
            print('users', users)
            for user in stub.List(trip_list_request):
                print("user", user)
                item = dict()
                item.update({"id": user.id})
                item.update({"created": user.created})
                item.update({"driver": user.driver})
                item.update({"customer": user.customer})
                print("item", item)
                users.append(item)
            channel.close()
        return Response({"success": users}, status=status.HTTP_200_OK)


class OrderCreate(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        user = self.request.user
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = trip_pb2_grpc.TripControllerStub(channel)
            location = trip_pb2.Location(location_name="Asdfasdf", lat="ASDfa", long="ASDfasdf",
                                         model_object_type="ASDFa", model_object_id="Asdfasd")
            trip = trip_pb2.Trip(customer="asdafsd", driver='asdfasdfa', plan="Asdfasdfa", state="requested",
                                 to_point=location, from_point=location)
            stub.Create(trip)
            channel.close()
        return Response({"success": "success"}, status=status.HTTP_200_OK)

