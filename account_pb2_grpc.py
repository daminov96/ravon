# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

import account_pb2 as account__pb2


class CustomUserControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
            "/account.CustomUserController/List",
            request_serializer=account__pb2.CustomUserListRequest.SerializeToString,
            response_deserializer=account__pb2.CustomUser.FromString,
        )
        self.Create = channel.unary_unary(
            "/account.CustomUserController/Create",
            request_serializer=account__pb2.CustomUser.SerializeToString,
            response_deserializer=account__pb2.CustomUser.FromString,
        )
        self.Retrieve = channel.unary_unary(
            "/account.CustomUserController/Retrieve",
            request_serializer=account__pb2.CustomUserRetrieveRequest.SerializeToString,
            response_deserializer=account__pb2.CustomUser.FromString,
        )
        self.Update = channel.unary_unary(
            "/account.CustomUserController/Update",
            request_serializer=account__pb2.CustomUser.SerializeToString,
            response_deserializer=account__pb2.CustomUser.FromString,
        )
        self.Destroy = channel.unary_unary(
            "/account.CustomUserController/Destroy",
            request_serializer=account__pb2.CustomUser.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class CustomUserControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_CustomUserControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "List": grpc.unary_stream_rpc_method_handler(
            servicer.List,
            request_deserializer=account__pb2.CustomUserListRequest.FromString,
            response_serializer=account__pb2.CustomUser.SerializeToString,
        ),
        "Create": grpc.unary_unary_rpc_method_handler(
            servicer.Create,
            request_deserializer=account__pb2.CustomUser.FromString,
            response_serializer=account__pb2.CustomUser.SerializeToString,
        ),
        "Retrieve": grpc.unary_unary_rpc_method_handler(
            servicer.Retrieve,
            request_deserializer=account__pb2.CustomUserRetrieveRequest.FromString,
            response_serializer=account__pb2.CustomUser.SerializeToString,
        ),
        "Update": grpc.unary_unary_rpc_method_handler(
            servicer.Update,
            request_deserializer=account__pb2.CustomUser.FromString,
            response_serializer=account__pb2.CustomUser.SerializeToString,
        ),
        "Destroy": grpc.unary_unary_rpc_method_handler(
            servicer.Destroy,
            request_deserializer=account__pb2.CustomUser.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "account.CustomUserController", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class CustomUserController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/account.CustomUserController/List",
            account__pb2.CustomUserListRequest.SerializeToString,
            account__pb2.CustomUser.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Create(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/account.CustomUserController/Create",
            account__pb2.CustomUser.SerializeToString,
            account__pb2.CustomUser.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Retrieve(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/account.CustomUserController/Retrieve",
            account__pb2.CustomUserRetrieveRequest.SerializeToString,
            account__pb2.CustomUser.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Update(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/account.CustomUserController/Update",
            account__pb2.CustomUser.SerializeToString,
            account__pb2.CustomUser.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Destroy(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/account.CustomUserController/Destroy",
            account__pb2.CustomUser.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
