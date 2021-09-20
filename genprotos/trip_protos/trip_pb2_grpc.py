# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from genprotos.trip_protos import trip_pb2 as protobufs_dot_trip__pb2


class TripControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/trip.TripController/List',
                request_serializer=protobufs_dot_trip__pb2.TripListRequest.SerializeToString,
                response_deserializer=protobufs_dot_trip__pb2.TripListResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/trip.TripController/Create',
                request_serializer=protobufs_dot_trip__pb2.Trip.SerializeToString,
                response_deserializer=protobufs_dot_trip__pb2.Trip.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/trip.TripController/Retrieve',
                request_serializer=protobufs_dot_trip__pb2.TripRetrieveRequest.SerializeToString,
                response_deserializer=protobufs_dot_trip__pb2.Trip.FromString,
                )
        self.Update = channel.unary_unary(
                '/trip.TripController/Update',
                request_serializer=protobufs_dot_trip__pb2.Trip.SerializeToString,
                response_deserializer=protobufs_dot_trip__pb2.Trip.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/trip.TripController/Destroy',
                request_serializer=protobufs_dot_trip__pb2.Trip.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class TripControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TripControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=protobufs_dot_trip__pb2.TripListRequest.FromString,
                    response_serializer=protobufs_dot_trip__pb2.TripListResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=protobufs_dot_trip__pb2.Trip.FromString,
                    response_serializer=protobufs_dot_trip__pb2.Trip.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=protobufs_dot_trip__pb2.TripRetrieveRequest.FromString,
                    response_serializer=protobufs_dot_trip__pb2.Trip.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=protobufs_dot_trip__pb2.Trip.FromString,
                    response_serializer=protobufs_dot_trip__pb2.Trip.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=protobufs_dot_trip__pb2.Trip.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'trip.TripController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TripController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trip.TripController/List',
            protobufs_dot_trip__pb2.TripListRequest.SerializeToString,
            protobufs_dot_trip__pb2.TripListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trip.TripController/Create',
            protobufs_dot_trip__pb2.Trip.SerializeToString,
            protobufs_dot_trip__pb2.Trip.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trip.TripController/Retrieve',
            protobufs_dot_trip__pb2.TripRetrieveRequest.SerializeToString,
            protobufs_dot_trip__pb2.Trip.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trip.TripController/Update',
            protobufs_dot_trip__pb2.Trip.SerializeToString,
            protobufs_dot_trip__pb2.Trip.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trip.TripController/Destroy',
            protobufs_dot_trip__pb2.Trip.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class NewTripControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Signal = channel.unary_unary(
                '/trip.NewTripController/Signal',
                request_serializer=protobufs_dot_trip__pb2.Trip.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class NewTripControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Signal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NewTripControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Signal': grpc.unary_unary_rpc_method_handler(
                    servicer.Signal,
                    request_deserializer=protobufs_dot_trip__pb2.Trip.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'trip.NewTripController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NewTripController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Signal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trip.NewTripController/Signal',
            protobufs_dot_trip__pb2.Trip.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class LocationControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/trip.LocationController/List',
                request_serializer=protobufs_dot_trip__pb2.LocationListRequest.SerializeToString,
                response_deserializer=protobufs_dot_trip__pb2.Location.FromString,
                )
        self.Create = channel.unary_unary(
                '/trip.LocationController/Create',
                request_serializer=protobufs_dot_trip__pb2.Location.SerializeToString,
                response_deserializer=protobufs_dot_trip__pb2.Location.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/trip.LocationController/Retrieve',
                request_serializer=protobufs_dot_trip__pb2.LocationRetrieveRequest.SerializeToString,
                response_deserializer=protobufs_dot_trip__pb2.Location.FromString,
                )
        self.Update = channel.unary_unary(
                '/trip.LocationController/Update',
                request_serializer=protobufs_dot_trip__pb2.Location.SerializeToString,
                response_deserializer=protobufs_dot_trip__pb2.Location.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/trip.LocationController/Destroy',
                request_serializer=protobufs_dot_trip__pb2.Location.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class LocationControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LocationControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=protobufs_dot_trip__pb2.LocationListRequest.FromString,
                    response_serializer=protobufs_dot_trip__pb2.Location.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=protobufs_dot_trip__pb2.Location.FromString,
                    response_serializer=protobufs_dot_trip__pb2.Location.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=protobufs_dot_trip__pb2.LocationRetrieveRequest.FromString,
                    response_serializer=protobufs_dot_trip__pb2.Location.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=protobufs_dot_trip__pb2.Location.FromString,
                    response_serializer=protobufs_dot_trip__pb2.Location.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=protobufs_dot_trip__pb2.Location.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'trip.LocationController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LocationController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/trip.LocationController/List',
            protobufs_dot_trip__pb2.LocationListRequest.SerializeToString,
            protobufs_dot_trip__pb2.Location.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trip.LocationController/Create',
            protobufs_dot_trip__pb2.Location.SerializeToString,
            protobufs_dot_trip__pb2.Location.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trip.LocationController/Retrieve',
            protobufs_dot_trip__pb2.LocationRetrieveRequest.SerializeToString,
            protobufs_dot_trip__pb2.Location.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trip.LocationController/Update',
            protobufs_dot_trip__pb2.Location.SerializeToString,
            protobufs_dot_trip__pb2.Location.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trip.LocationController/Destroy',
            protobufs_dot_trip__pb2.Location.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class ReasonToCancelTripControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/trip.ReasonToCancelTripController/List',
                request_serializer=protobufs_dot_trip__pb2.ReasonToCancelTripListRequest.SerializeToString,
                response_deserializer=protobufs_dot_trip__pb2.ReasonToCancelTrip.FromString,
                )
        self.Create = channel.unary_unary(
                '/trip.ReasonToCancelTripController/Create',
                request_serializer=protobufs_dot_trip__pb2.ReasonToCancelTrip.SerializeToString,
                response_deserializer=protobufs_dot_trip__pb2.ReasonToCancelTrip.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/trip.ReasonToCancelTripController/Retrieve',
                request_serializer=protobufs_dot_trip__pb2.ReasonToCancelTripRetrieveRequest.SerializeToString,
                response_deserializer=protobufs_dot_trip__pb2.ReasonToCancelTrip.FromString,
                )
        self.Update = channel.unary_unary(
                '/trip.ReasonToCancelTripController/Update',
                request_serializer=protobufs_dot_trip__pb2.ReasonToCancelTrip.SerializeToString,
                response_deserializer=protobufs_dot_trip__pb2.ReasonToCancelTrip.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/trip.ReasonToCancelTripController/Destroy',
                request_serializer=protobufs_dot_trip__pb2.ReasonToCancelTrip.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class ReasonToCancelTripControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReasonToCancelTripControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=protobufs_dot_trip__pb2.ReasonToCancelTripListRequest.FromString,
                    response_serializer=protobufs_dot_trip__pb2.ReasonToCancelTrip.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=protobufs_dot_trip__pb2.ReasonToCancelTrip.FromString,
                    response_serializer=protobufs_dot_trip__pb2.ReasonToCancelTrip.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=protobufs_dot_trip__pb2.ReasonToCancelTripRetrieveRequest.FromString,
                    response_serializer=protobufs_dot_trip__pb2.ReasonToCancelTrip.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=protobufs_dot_trip__pb2.ReasonToCancelTrip.FromString,
                    response_serializer=protobufs_dot_trip__pb2.ReasonToCancelTrip.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=protobufs_dot_trip__pb2.ReasonToCancelTrip.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'trip.ReasonToCancelTripController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ReasonToCancelTripController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/trip.ReasonToCancelTripController/List',
            protobufs_dot_trip__pb2.ReasonToCancelTripListRequest.SerializeToString,
            protobufs_dot_trip__pb2.ReasonToCancelTrip.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trip.ReasonToCancelTripController/Create',
            protobufs_dot_trip__pb2.ReasonToCancelTrip.SerializeToString,
            protobufs_dot_trip__pb2.ReasonToCancelTrip.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trip.ReasonToCancelTripController/Retrieve',
            protobufs_dot_trip__pb2.ReasonToCancelTripRetrieveRequest.SerializeToString,
            protobufs_dot_trip__pb2.ReasonToCancelTrip.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trip.ReasonToCancelTripController/Update',
            protobufs_dot_trip__pb2.ReasonToCancelTrip.SerializeToString,
            protobufs_dot_trip__pb2.ReasonToCancelTrip.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trip.ReasonToCancelTripController/Destroy',
            protobufs_dot_trip__pb2.ReasonToCancelTrip.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
