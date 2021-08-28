from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, data):
        if data.get('password1') and data.get('password2'):
            if data['password1'] != data['password2']:
                raise serializers.ValidationError('Passwords must match.')
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            request = self.context['request']
            if request.query_params.get('center_id', None):
                try:
                    status = Connection.objects.get(user__id=instance.id,
                                                    center__id=self.context['request'].query_params.get(
                                                        'center_id',
                                                        None)).status
                    role = Connection.objects.get(user__id=instance.id,
                                                  center__id=self.context['request'].query_params.get(
                                                      'center_id',
                                                      None)).role
                    data['role'] = status if status != Connection.OTHER else role
                    data['is_verified'] = Connection.objects.get(user__id=instance.id,
                                                                 center__id=self.context['request'].query_params.get(
                                                                     'center_id',
                                                                     None)).is_verified
                except Exception:
                    data['role'] = ''
            if request.user.is_authenticated:
                if request.user in instance.followers.all():
                    data['is_following'] = True
                    data['following_connection_id'] = \
                        FollowConnection.objects.filter(from_user=request.user, to_user=instance)[0].id
                else:
                    data['is_following'] = False
                follower_connection = FollowConnection.objects.filter(from_user=instance, to_user=request.user)
                if follower_connection:
                    data['is_followed'] = True
                    data['follower_connection_id'] = follower_connection[0].id
                else:
                    data['is_followed'] = False
        except Exception:
            pass
        return data

    def create(self, validated_data):
        data = {
            key: value for key, value in validated_data.items()
            if key not in ('password1', 'password2')
        }
        data['password'] = validated_data['password1']
        data['username'] = data['phone']
        user = self.Meta.model.objects.create_user(**data)
        code = sendsms(phone=user.phone)
        user.phone_verification_code = code
        user.is_active = False
        user.save()
        import telebot
        count = CustomUser.objects.all().count()
        bot = telebot.TeleBot(
            "1309416311:AAEr_hirX_4-DhBLVoM-fpNLUPBQ3vqF4zk")  # You can set parse_mode by default. HTML or MARKDOWN
        message = f"https://edumanager.uz 🎉 saytiga yangi foydalanuvchi qoshildi \n" \
                  f"Username:{user.username}\nFull Name: {user.first_name} {user.last_name}\n" \
                  f"Foydalanuvchilar Soni: {count} ga yetdi"
        bot.send_message('-442365863', f'{message}')
        bot.send_message('-557715643', f'{message}')

        return user

    class Meta:
        model = CustomUser
        exclude = ['password', 'is_superuser', 'user_permissions', 'groups', 'email', 'phone_verification_code']
        read_only_fields = ('username', 'parents', 'last_login', 'is_staff', 'is_superuser', 'is_active')
        write_only_fields = ('password1', 'password2')


class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'username']


class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = CustomUser
        fields = ('token', 'username', 'password')


class UsersInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class TokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user'] = UserSerializer(instance=self.user, context=self.context).data
        return data


class CashelokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashilok
        fields = '__all__'


class FollowConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowConnection
        fields = '__all__'

    def to_representation(self, instance):
        data = super(FollowConnectionSerializer, self).to_representation(instance)
        data['from_user'] = UserSerializer(instance=instance.from_user,
                                           context={'request': self.context['request']}).data
        data['to_user'] = UserSerializer(instance=instance.to_user,
                                         context={'request': self.context['request']}).data
        return data


class CashelokFillSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashilokFill
        fields = ('id', 'owner', 'payment_method', 'amount')


class CashelokFillFUllSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashilokFill
        fields = "__all__"


class FilesOfPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilesOfPost
        fields = "__all__"


class CommentOfMiniPostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentOfPost
        fields = ['id', 'owner', 'post', 'replay_to', 'comment', 'created_at']

    def to_representation(self, instance):
        data = super(CommentOfMiniPostoSerializer, self).to_representation(instance)
        request = self.context['request']
        data['owner_info'] = UserSerializer(instance=instance.owner, context={'request': request}).data
        data['liked'] = False
        data['likes_count'] = instance.user_likes.count()
        user = self.context['request'].user
        if user.is_authenticated:
            if user in instance.user_likes.all():
                data['liked'] = True
        return data


def recursive_comment_of_post(replies, request) -> list:
    data = []
    if len(replies) > 0:
        for i in replies:
            data.append(CommentOfMiniPostoSerializer(instance=i, context={'request': request}).data)
            if i.replies.all():
                if len(recursive_comment_of_post(i.replies.all(), request)) > 0:
                    for j in recursive_comment_of_post(i.replies.all(), request):
                        data.append(j)
    return data


class CommentOfPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentOfVideo
        fields = ['id', 'owner', 'video', 'replay_to', 'comment', 'created_at']

    def to_representation(self, instance):
        data = super(CommentOfPostSerializer, self).to_representation(instance)
        request = self.context['request']
        data['owner_info'] = UserSerializer(instance=instance.owner, context={'request': request}).data
        data['replies'] = recursive_comment_of_post(instance.replies.all().order_by("-created_at"),
                                                    request) if instance.replies.all() else []
        data['liked'] = False
        data['likes_count'] = instance.user_likes.count()
        user = self.context['request'].user
        if user.is_authenticated:
            if user in instance.user_likes.all():
                data['liked'] = True
        return data


class PostSerializers(serializers.ModelSerializer):
    files = FilesOfPostSerializer(many=True)

    class Meta:
        model = Post
        exclude = ('user_likes',)

    def to_representation(self, instance):
        data = super(PostSerializers, self).to_representation(instance)
        data['liked'] = False
        data['owner'] = UserSerializer(instance=instance.owner, context=self.context).data
        data['likes_count'] = instance.user_likes.count()
        data['comments_count'] = instance.comment.all().count()
        user = self.context['request'].user
        if user.is_authenticated:
            if user in instance.user_likes.all():
                data['liked'] = True
        return data


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        exclude = ('user_likes',)

    def to_representation(self, instance):
        data = super(VideoSerializer, self).to_representation(instance)
        data['liked'] = False
        data['owner'] = UserSerializer(instance=instance.owner, context=self.context).data
        data['likes_count'] = instance.user_likes.count()
        data['comments_count'] = instance.comments.all().count()
        user = self.context['request'].user
        if user.is_authenticated:
            if user in instance.user_likes.all():
                data['liked'] = True
        return data

    def create(self, validated_data):
        obj = Video.objects.create(**validated_data)
        obj.save()
        upload(self.context['request'], obj)
        return obj


class CommentOfMiniVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentOfVideo
        fields = ['id', 'owner', 'video', 'replay_to', 'comment', 'created_at']

    def to_representation(self, instance):
        data = super(CommentOfMiniVideoSerializer, self).to_representation(instance)
        request = self.context['request']
        data['owner_info'] = UserSerializer(instance=instance.owner, context={'request': request}).data
        data['liked'] = False
        data['likes_count'] = instance.user_likes.count()
        user = self.context['request'].user
        if user.is_authenticated:
            if user in instance.user_likes.all():
                data['liked'] = True
        return data


def recursive_comment_of_vidoe(replies, request) -> list:
    data = []
    if len(replies) > 0:
        for i in replies:
            data.append(CommentOfMiniVideoSerializer(instance=i, context={'request': request}).data)
            if i.replies.all():
                if len(recursive_comment_of_vidoe(i.replies.all(), request)) > 0:
                    for j in recursive_comment_of_vidoe(i.replies.all(), request):
                        data.append(j)
    return data


class CommentOfVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentOfVideo
        fields = ['id', 'owner', 'video', 'replay_to', 'comment', 'created_at']

    def to_representation(self, instance):
        data = super(CommentOfVideoSerializer, self).to_representation(instance)
        request = self.context['request']
        data['owner_info'] = UserSerializer(instance=instance.owner, context={'request': request}).data
        data['replies'] = recursive_comment_of_vidoe(instance.replies.all().order_by("-created_at"),
                                                     request) if instance.replies.all() else []
        data['liked'] = False
        data['likes_count'] = instance.user_likes.count()
        user = self.context['request'].user
        if user.is_authenticated:
            if user in instance.user_likes.all():
                data['liked'] = True
        return data
