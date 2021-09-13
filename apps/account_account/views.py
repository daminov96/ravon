import requests
from clickuz import ClickUz
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db.models import Q, Sum
from django.utils import timezone
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, response
from rest_framework import status
from rest_framework import status as rest_status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView as JWTTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView as JWTTokenRefreshView

from apps.account_account import filter_params

from ..app.models import *
from ..utils.utils import invalidate_verification_code, sendsms
from .models import Cashilok, CashilokFill, CustomUser
from .permissions import IsSelf
from .serializers import *


class GoogleView(APIView):
    def post(self, request):
        payload = {"access_token": request.data.get("token")}  # validate the token
        r = requests.get(
            "https://www.googleapis.com/oauth2/v2/userinfo", params=payload
        )
        data = json.loads(r.text)

        if "error" in data:
            content = {
                "message": "wrong google token / this google token is already expired."
            }
            return Response(content)
        try:
            user = CustomUser.objects.get(email=data["email"])
        except CustomUser.DoesNotExist:
            user = CustomUser()
            user.username = data["email"]
            # provider random default password
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = data["email"]
            user.save()

        token = RefreshToken.for_user(
            user
        )  # generate token without username & password
        response = {}
        response["username"] = user.username
        response["access_token"] = str(token.access_token)
        response["refresh_token"] = str(token)
        return Response(response)


class GetUser(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (IsSelf,)


class UserList(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSelf,)

    def get_serializer_context(self):
        return {"request": self.request}

    def create(self, request, *args, **kwargs):

        return super(UserList, self).create(request, *args, **kwargs)

    @action(detail=True, methods=["Post"])
    def create_child(self, request, pk=None):
        context = {"request": request, "parent": self.get_object()}
        serializer = self.serializer_class(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error": serializer.errors})

    def get_queryset(self):
        queryset = super().get_queryset()
        queryparam = self.request.query_params
        query = queryparam.get("query", None)
        group_id = queryparam.get("group_id", None)
        not_in_group_id = queryparam.get("not_in_group_id", None)
        center_id = queryparam.get("center_id", None)
        parent_id = queryparam.get("parent_id", None)
        type_of_user = queryparam.get("type_of_user", None)
        is_verified = queryparam.get("is_verified", None)
        not_verified = queryparam.get("not_verified", None)
        if center_id:
            queryset = queryset.filter(connections__center__id=center_id)
        if is_verified:
            queryset = queryset.filter(connections__is_verified=True)
        if not_verified:
            queryset = queryset.filter(connections__is_verified=False)
        if parent_id:
            queryset = queryset.filter(parents__id__in=parent_id)
        if query:
            queryset = queryset.filter(
                Q(first_name__icontains=query)
                | Q(username__icontains=query)
                | Q(last_name__icontains=query)
            ).distinct()
        if type_of_user:
            queryset = queryset.filter(
                connections__center__id=center_id, connections__status=type_of_user
            )
        if queryparam.get("parent_id", None):
            queryset = queryset.filter(parents__in=[queryparam.get("parent_id", None)])
        if group_id:
            queryset = queryset.filter(regsitered_groups__id=group_id)
        if not_in_group_id:
            queryset = queryset.exclude(regsitered_groups__id=not_in_group_id)
        return queryset.distinct()

    @swagger_auto_schema(manual_parameters=filter_params.get_user_params())
    def list(self, request, *args, **kwargs):
        return super(UserList, self).list(kwargs)


class Login(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", None)
        if username:
            user = CustomUser.objects.get_or_create(username=username)
            code = sendsms(phone=user.username)
            user.phone_verification_code = code
            time = timezone.now()
            invalidate_verification_code.apply_async(user, time)
            user.save()
            return Response({"success": "User found"}, status=status.HTTP_200_OK)
        return Response(
            {"error": "Phone number or code not provided"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class VerifyPhone(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", None)
        code = request.data.get("code", None)
        if username and code:
            user = CustomUser.objects.filter(username=username)
            if user:
                user = user.last()
                if user.phone_verification_code != None:
                    if code == user.phone_verification_code:
                        user.is_active = True
                        user.save()
                        refresh = TokenObtainPairSerializer().get_token(user)
                        data = {}
                        data["refresh"] = str(refresh)
                        data["access"] = str(refresh.access_token)
                        data["user"] = UserSerializer(instance=user).data
                        return Response(data=data, status=status.HTTP_201_CREATED)
                    return Response(
                        {"error": "wrong code"}, status=status.HTTP_403_FORBIDDEN
                    )
                return Response(
                    {"error": "Verification code is not sent or expired!"},
                    status=status.HTTP_403_FORBIDDEN,
                )
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            {"error": "Phone number or code not provided"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class TokenGenerateView(JWTTokenObtainPairView):
    serializer_class = TokenSerializer
    post_responses = {
        rest_status.HTTP_201_CREATED: openapi.Response(description="Token obtained"),
        rest_status.HTTP_404_NOT_FOUND: openapi.Response(description="User not found"),
        rest_status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Validation error"
        ),
    }

    def get_serializer_context(self):
        return {"request": self.request}

    @swagger_auto_schema(
        operation_id="token_obtain",
        operation_description="Token obtaining",
        responses=post_responses,
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        else:
            data = serializer.validated_data
        return response.Response(data, status=rest_status.HTTP_201_CREATED)


class TokenRefreshView(JWTTokenRefreshView):
    post_responses = {
        rest_status.HTTP_201_CREATED: openapi.Response(description="Token obtained"),
        rest_status.HTTP_404_NOT_FOUND: openapi.Response(description="Token not found"),
        rest_status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Validation error"
        ),
    }

    @swagger_auto_schema(
        operation_id="token_refreshing",
        operation_description="Token refreshing",
        responses=post_responses,
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ResendVerificationCode(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", None)
        if username:
            try:
                user = CustomUser.objects.get(username=username)
                code = sendsms(phone=user.phone)
                user.phone_verification_code = code
                time = timezone.now()
                invalidate_verification_code.apply_async(user, time)
                user.save()
                return Response({"success": status.HTTP_200_OK})
            except CustomUser.DoesNotExist:
                Response({"error": "User with this phone number does not exist"})
        return Response({"error": "Username number not provided"})


class ForgetPasword(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", None)
        if username:
            try:
                user = CustomUser.objects.get(username=username)
                code = sendsms(phone=user.phone)
                user.phone_verification_code = code
                user.save()
                return Response({"success": status.HTTP_200_OK})
            except CustomUser.DoesNotExist:
                Response({"error": "User with this phone number does not exist"})
        return Response({"error": "Username number not provided"})
