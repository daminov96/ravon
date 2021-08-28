import requests
from clickuz import ClickUz
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db.models import Q, Sum
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import response, permissions, status as rest_status, viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import (TokenObtainPairView as JWTTokenObtainPairView,
                                            TokenRefreshView as JWTTokenRefreshView,
                                            )

from apps.account_account import filter_params
from apps.rest_api.permissions import IsOwnerOrReadOnly
from .models import CustomUser, Cashilok, CashilokFill, FollowConnection, Video
from .models import Post, CommentOfPost, FilesOfPost
from .permissions import IsSelf
from .serializers import *
from ..app.models import Lecture
from ..app.modules import sendsms
from ..rest_api.models import Group, Connection, Material, Subject, Center, SessionOfTeacher


class GoogleView(APIView):
    def post(self, request):
        payload = {'access_token': request.data.get("token")}  # validate the token
        r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        data = json.loads(r.text)

        if 'error' in data:
            content = {'message': 'wrong google token / this google token is already expired.'}
            return Response(content)
        try:
            user = CustomUser.objects.get(email=data['email'])
        except CustomUser.DoesNotExist:
            user = CustomUser()
            user.username = data['email']
            # provider random default password
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = data['email']
            user.save()

        token = RefreshToken.for_user(user)  # generate token without username & password
        response = {}
        response['username'] = user.username
        response['access_token'] = str(token.access_token)
        response['refresh_token'] = str(token)
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
        return {'request': self.request}

    def create(self, request, *args, **kwargs):

        return super(UserList, self).create(request, *args, **kwargs)

    @action(detail=True, methods=['Post'])
    def create_child(self, request, pk=None):
        context = {
            'request': request,
            'parent': self.get_object()
        }
        serializer = self.serializer_class(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error": serializer.errors})

    def get_queryset(self):
        queryset = super().get_queryset()
        queryparam = self.request.query_params
        query = queryparam.get('query', None)
        group_id = queryparam.get('group_id', None)
        not_in_group_id = queryparam.get('not_in_group_id', None)
        center_id = queryparam.get('center_id', None)
        parent_id = queryparam.get('parent_id', None)
        type_of_user = queryparam.get('type_of_user', None)
        is_verified = queryparam.get('is_verified', None)
        not_verified = queryparam.get('not_verified', None)
        if center_id:
            queryset = queryset.filter(connections__center__id=center_id)
        if is_verified:
            queryset = queryset.filter(connections__is_verified=True)
        if not_verified:
            queryset = queryset.filter(connections__is_verified=False)
        if parent_id:
            queryset = queryset.filter(parents__id__in=parent_id)
        if query:
            queryset = queryset.filter(Q(first_name__icontains=query) | Q(username__icontains=query) | Q(
                last_name__icontains=query)).distinct()
        if type_of_user:
            queryset = queryset.filter(connections__center__id=center_id, connections__status=type_of_user)
        if queryparam.get('parent_id', None):
            queryset = queryset.filter(parents__in=[queryparam.get('parent_id', None)])
        if group_id:
            queryset = queryset.filter(regsitered_groups__id=group_id)
        if not_in_group_id:
            queryset = queryset.exclude(regsitered_groups__id=not_in_group_id)
        return queryset.distinct()

    @swagger_auto_schema(manual_parameters=filter_params.get_user_params())
    def list(self, request, *args, **kwargs):
        return super(UserList, self).list(kwargs)


class FollowConnectionViewSet(viewsets.ModelViewSet):
    queryset = FollowConnection.objects.all()
    serializer_class = FollowConnectionSerializer
    permission_classes = (IsSelf,)

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):
        queryset = super().get_queryset()
        queryparam = self.request.query_params
        return queryset.distinct()

    @swagger_auto_schema(manual_parameters=filter_params.get_follow_connection_params())
    def list(self, request, *args, **kwargs):
        return super(FollowConnectionViewSet, self).list(kwargs)


class VerifyPhone(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username', None)
        code = request.data.get('code', None)
        if username and code:
            user = CustomUser.objects.filter(username=username)
            if user:
                user=user.last()
                if code == user.phone_verification_code:
                    user.is_active = True
                    user.save()
                    return Response({'success': status.HTTP_200_OK})
                return Response({"error": "wrong code"}, status=status.HTTP_403_FORBIDDEN)
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Phone number or code not provided'}, status=status.HTTP_400_BAD_REQUEST)


class TokenGenerateView(JWTTokenObtainPairView):
    serializer_class = TokenSerializer
    post_responses = {
        rest_status.HTTP_201_CREATED: openapi.Response(description='Token obtained'),
        rest_status.HTTP_404_NOT_FOUND: openapi.Response(description='User not found'),
        rest_status.HTTP_400_BAD_REQUEST: openapi.Response(description='Validation error'),
    }

    def get_serializer_context(self):
        return {'request': self.request}

    @swagger_auto_schema(operation_id='token_obtain', operation_description='Token obtaining', responses=post_responses)
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
        rest_status.HTTP_201_CREATED: openapi.Response(description='Token obtained'),
        rest_status.HTTP_404_NOT_FOUND: openapi.Response(description='Token not found'),
        rest_status.HTTP_400_BAD_REQUEST: openapi.Response(description='Validation error'),
    }

    @swagger_auto_schema(operation_id='token_refreshing', operation_description='Token refreshing',
                         responses=post_responses)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class Statistics(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    center_id = openapi.Parameter('center_id', openapi.IN_QUERY,
                                  description="center_id id ",
                                  type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(manual_parameters=[center_id])
    def get(self, request, *args, **kwargs):
        user = self.request.user
        center__id = self.request.query_params.get('center_id')
        center = Center.objects.get(id=center__id)
        connection = Connection.objects.get(user=user, center=center)
        students = Connection.objects.filter(center__id=center__id, status=Connection.STUDENT)
        teachers_count = Connection.objects.filter(center__id=center__id, status=Connection.MENTOR).count()
        parents_count = Connection.objects.filter(center__id=center__id, status=Connection.PARENT).count()
        male_students_count = Connection.objects.filter(center__id=center__id, status=Connection.STUDENT,
                                                        user__gender=CustomUser.MALE).count()
        female_students_count = Connection.objects.filter(center__id=center__id, status=Connection.STUDENT,
                                                          user__gender=CustomUser.FEMALE).count()
        groups = Group.objects.filter(center__id=center__id)
        lectures = Lecture.objects.filter(center__id=center__id)
        books_count = Material.objects.filter(center__id=center__id).count()
        subjects_count = Subject.objects.all().count()
        graduates_count = Group.objects.filter(center__id=center__id, status=Group.CLOSED).values_list('students',
                                                                                                       flat=True).count()
        other_profits = center.profits.aggregate(total=Sum('amount'))['total']
        student_sessions = center.center_sessions.aggregate(total=Sum('paid_amount'))['total']
        total_profit = 0
        if other_profits:
            total_profit = other_profits
        if student_sessions:
            total_profit = total_profit + student_sessions
        if connection.status == Connection.MENTOR:
            graduates_count = Group.objects.filter(owner=user, center__id=center__id, status=Group.CLOSED).values_list(
                'students',
                flat=True).count()
            total_profit = \
                SessionOfTeacher.objects.filter(user=user, center=center).aggregate(total=Sum('paid_amount'))['total']
            return response.Response({
                'students_count': students.count(),
                'groups_count': groups.filter(owner=user).count(),
                'lectures_count': lectures.filter(owner=user).count(),
                'graduates_counts': graduates_count,
                'total_profit': total_profit
            })

        if connection.status == Connection.STUDENT:
            return response.Response({
                'groups_count': groups.filter(students__in=[user]).count(),
                'lectures_count': lectures.filter(owner=user).count(),
            })
        return response.Response({
            'students_count': students.count(),
            'teachers_count': teachers_count,
            'parents_count': parents_count,
            'male_students_count': male_students_count,
            'female_students_count': female_students_count,
            'groups_count': groups.count(),
            'lectures_count': lectures.count(),
            'books_count': books_count,
            'subjects_count': subjects_count,
            'graduates_counts': graduates_count,
            'total_profit': total_profit
        })


class CashelokViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CashelokSerializer
    queryset = Cashilok.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        queryset = super().get_queryset()
        owner_id = self.request.query_params.get('owner_id', None)
        if owner_id:
            return queryset.filter(owner__id=owner_id)
        return queryset

    @swagger_auto_schema(manual_parameters=filter_params.get_cashelok_params())
    def list(self, request, *args, **kwargs):
        return super(CashelokViewSet, self).list(kwargs)


class CashelokFillViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CashelokFillFUllSerializer
    queryset = CashilokFill.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        owner_id = self.request.query_params.get('owner_id', None)
        if owner_id:
            return queryset.filter(owner__id=owner_id)
        return queryset

    @swagger_auto_schema(manual_parameters=filter_params.get_cashelokfill_params())
    def list(self, request, *args, **kwargs):
        return super(CashelokFillViewSet, self).list(kwargs)


class CreateCashilokFill(APIView):
    def post(self, reqeust, *args, **kwargs):
        serializer = CashelokFillSerializer(data=self.request.data)
        url = None
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            if data['payment_method'] == 'click':
                url = ClickUz.generate_url(order_id=data['id'], amount=data['amount'])
            CashilokFill.objects.create(**serializer.validated_data)
        return Response({"cool": 'cool', 'url': url})


class SystemStatistics(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"number_of_users": CustomUser.objects.all().count()})


class ResendVerificationCode(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username', None)
        if username:
            try:
                user = CustomUser.objects.get(username=username)
                code = sendsms(phone=user.phone)
                user.phone_verification_code = code
                user.save()
                return Response({'success': status.HTTP_200_OK})
            except CustomUser.DoesNotExist:
                Response({'error': 'User with this phone number does not exist'})
        return Response({'error': 'Username number not provided'})


class ForgetPasword(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username', None)
        if username:
            try:
                user = CustomUser.objects.get(username=username)
                code = sendsms(phone=user.phone)
                user.phone_verification_code = code
                user.save()
                return Response({'success': status.HTTP_200_OK})
            except CustomUser.DoesNotExist:
                Response({'error': 'User with this phone number does not exist'})
        return Response({'error': 'Username number not provided'})


class Followers(ListAPIView):
    serializer_class = FollowConnectionSerializer
    queryset = FollowConnection.objects.all()

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):
        queryset = super().get_queryset()
        queryparams = self.request.query_params
        user_id = queryparams.get('user_id', None)
        query = queryparams.get('query', None)
        if user_id:
            queryset = queryset.filter(to_user=user_id)
            if query:
                queryset = queryset.filter(
                    Q(from_user__first_name__icontains=query) | Q(from_user__last_name__icontains=query))
            return queryset.distinct()
        return None

    @swagger_auto_schema(manual_parameters=filter_params.get_followers_params())
    def get(self, request, *args, **kwargs):
        return super(Followers, self).get(kwargs)


class Followings(ListAPIView):
    serializer_class = FollowConnectionSerializer
    queryset = FollowConnection.objects.all()

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):
        queryset = super().get_queryset()
        queryparams = self.request.query_params
        user_id = queryparams.get('user_id', None)
        query = queryparams.get('query', None)
        if user_id:
            queryset = queryset.filter(from_user=user_id)
            if query:
                queryset = queryset.filter(
                    Q(to_user__first_name__icontains=query) | Q(to_user__last_name__icontains=query))
            return queryset.distinct()
        return None

    @swagger_auto_schema(manual_parameters=filter_params.get_followers_params())
    def get(self, request, *args, **kwargs):
        return super(Followings, self).get(kwargs)


class FollowerFollowingStatistics(APIView):
    @swagger_auto_schema(manual_parameters=filter_params.get_followers_params())
    def get(self, request, *args, **kwargs):
        queryparams = self.request.query_params
        user_id = queryparams.get('user_id', None)
        if user_id:
            follow_connections = FollowConnection.objects.filter(
                Q(from_user__id=user_id) | Q(to_user__id=user_id)).distinct('id')
            connections_count = Connection.objects.filter(user__id=user_id).count()
            followers_count = follow_connections.filter(to_user__id=user_id).distinct('id').count()
            followings_count = follow_connections.filter(from_user__id=user_id).distinct('id').count()
            return Response({"followers_count": followers_count, "followings_count": followings_count,
                             'connections_count': connections_count}, status=status.HTTP_200_OK)
        return Response({"error": "You should provide user id"},
                        status=status.HTTP_400_BAD_REQUEST)


class PostsFilesView(ModelViewSet):
    queryset = FilesOfPost.objects.all()
    serializer_class = FilesOfPostSerializer
    permission_classes = [IsOwnerOrReadOnly, ]

    def get_queryset(self):
        queryset = super().get_queryset()
        post_id = self.request.query_params.get('post_id', None)
        if post_id:
            return queryset.filter(post__id=post_id)
        return queryset

    @swagger_auto_schema(manual_parameters=filter_params.get_post_file_comments())
    def list(self, request, *args, **kwargs):
        return super(PostsFilesView, self).list(kwargs)


class PostsCommentsView(ModelViewSet):
    queryset = CommentOfPost.objects.all()
    serializer_class = CommentOfPostSerializer
    permission_classes = [IsOwnerOrReadOnly, ]

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):
        queryset = super().get_queryset()
        post_id = self.request.query_params.get('post_id', None)
        if post_id:
            queryset = queryset.filter(post__id=post_id, replay_to=None)
        return queryset

    @swagger_auto_schema(manual_parameters=filter_params.get_post_file_comments())
    def list(self, request, *args, **kwargs):
        return super(PostsCommentsView, self).list(kwargs)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        user = self.request.user
        if user.is_authenticated:
            user_id = user.id
            if user_id:
                comment_of_post = self.get_object()
                if int(user_id) in list(comment_of_post.user_likes.all().values_list('id', flat=True)):
                    comment_of_post.user_likes.remove(user_id)
                    comment_of_post.save()
                else:
                    comment_of_post.user_likes.add(user_id)
                comment_of_post.save()
                serializer = self.serializer_class(instance=comment_of_post, context=self.get_serializer_context())
                return Response(serializer.data)
        return Response({"error": "You should login first"})


class PostsViewSet(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsOwnerOrReadOnly, ]
    serializer_class = PostSerializers

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):
        queryset = super().get_queryset()
        queryparams = self.request.query_params
        owner_id = queryparams.get('owner_id')
        if owner_id:
            queryset = queryset.filter(owner__id=owner_id)
        return queryset

    @swagger_auto_schema(manual_parameters=filter_params.get_post_params())
    def list(self, request, *args, **kwargs):
        return super(PostsViewSet, self).list(kwargs)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        user = self.request.user
        if user.is_authenticated:
            user_id = user.id
            if user_id:
                post = self.get_object()
                if int(user_id) in list(post.user_likes.all().values_list('id', flat=True)):
                    post.user_likes.remove(user_id)
                    post.save()
                else:
                    post.user_likes.add(user_id)
                post.save()
                serializer = self.serializer_class(instance=post, context=self.get_serializer_context())
                return Response(serializer.data)
        return Response({"error": "You should login first"})


class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    permission_classes = [IsOwnerOrReadOnly, ]
    serializer_class = VideoSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):
        queryset = super().get_queryset()
        queryparams = self.request.query_params
        owner_id = queryparams.get('owner_id')
        if owner_id:
            queryset = queryset.filter(owner__id=owner_id)
        return queryset

    @swagger_auto_schema(manual_parameters=filter_params.get_video_params())
    def list(self, request, *args, **kwargs):
        return super(VideoViewSet, self).list(kwargs)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        user = self.request.user
        if user.is_authenticated:
            user_id = user.id
            if user_id:
                video = self.get_object()
                if int(user_id) in list(video.user_likes.all().values_list('id', flat=True)):
                    video.user_likes.remove(user_id)
                    video.save()
                else:
                    video.user_likes.add(user_id)
                video.save()
                serializer = self.serializer_class(instance=video, context=self.get_serializer_context())
                return Response(serializer.data)
        return Response({"error": "You should login first"})


class CommentOfVideoViewSet(viewsets.ModelViewSet):
    queryset = CommentOfVideo.objects.all()
    serializer_class = CommentOfVideoSerializer
    permissions = (IsOwnerOrReadOnly,)

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):
        queryset = super().get_queryset()
        queryparams = self.request.query_params
        owner_id = queryparams.get('owner_id', None)
        if owner_id:
            queryset = queryset.filter(owner_id=owner_id)
        video_id = queryparams.get('video_id')
        if video_id:
            queryset = queryset.filter(video__id=video_id)
            queryset.filter(replay_to=None)
        return queryset

    @swagger_auto_schema(manual_parameters=filter_params.get_comment_of_video_params())
    def list(self, request, *args, **kwargs):
        return super(CommentOfVideoViewSet, self).list(kwargs)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        user = self.request.user
        if user.is_authenticated:
            user_id = user.id
            if user_id:
                comment = self.get_object()
                if int(user_id) in list(comment.user_likes.all().values_list('id', flat=True)):
                    comment.user_likes.remove(user_id)
                    comment.save()
                else:
                    comment.user_likes.add(user_id)
                comment.save()
                serializer = self.serializer_class(instance=comment, context=self.get_serializer_context())
                return Response(serializer.data)
        return Response({"error": "You should login first"})
