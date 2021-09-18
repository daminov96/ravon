import grpc
from rest_framework.views import APIView
from genprotos.trip_protos import trip_pb2, trip_pb2_grpc
from rest_framework.response import Response
import rest_framework.status as status


def cast_json(value):
    from google.protobuf.json_format import MessageToDict

    try:
        if not value:
            return []
        repeated_values = list(value)
        values = []
        for value in repeated_values:
            if isinstance(value, (int, str, float)):
                values.append(value)
                continue
            values.append(MessageToDict(value, False, True))
    except Exception as e:
        print(e)
        values = MessageToDict(value, False, True)
    return values


class OrderList(APIView):

    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print('ad')
        user = self.request.user
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = trip_pb2_grpc.TripControllerStub(channel)
            trip_list_request = trip_pb2.TripListRequest()
            trip_list_request.driver = "asdfasdfa"
            response = stub.List(trip_list_request)
            channel.close()
        return Response({"success": cast_json(response.results)}, status=status.HTTP_200_OK)


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


