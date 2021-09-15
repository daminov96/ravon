from django_grpc_framework import generics

from apps.account_account.serializers import UserProtoSerializer

from .models import CustomUser


class UserService(generics.ModelService):
    """
    gRPC service that allows users to be retrieved or updated.
    """

    queryset = CustomUser.objects.all().order_by("-date_joined")
    serializer_class = UserProtoSerializer
