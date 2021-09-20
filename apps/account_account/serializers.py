from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.account_account.models import *

from apps.utils.utils import sendsms


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, data):
        if data.get("password1") and data.get("password2"):
            if data["password1"] != data["password2"]:
                raise serializers.ValidationError("Passwords must match.")
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # data['teacher'] = UserSerializer(instance=instance.teacher_id)
        # try:
        #     request = self.context['request']
        #     if request.query_params.get('center_id', None):
        #         try:
        #             status = Connection.objects.get(user__id=instance.id,
        #                                             center__id=self.context['request'].query_params.get(
        #                                                 'center_id',
        #                                                 None)).status
        #             role = Connection.objects.get(user__id=instance.id,
        #                                           center__id=self.context['request'].query_params.get(
        #                                               'center_id',
        #                                               None)).role
        #             data['role'] = status if status != Connection.OTHER else role
        #             data['is_verified'] = Connection.objects.get(user__id=instance.id,
        #                                                          center__id=self.context['request'].query_params.get(
        #                                                              'center_id',
        #                                                              None)).is_verified
        #         except Exception:
        #             data['role'] = ''
        #     if request.user.is_authenticated:
        #         if request.user in instance.followers.all():
        #             data['is_following'] = True
        #             data['following_connection_id'] = \
        #                 FollowConnection.objects.filter(from_user=request.user, to_user=instance)[0].id
        #         else:
        #             data['is_following'] = False
        #         follower_connection = FollowConnection.objects.filter(from_user=instance, to_user=request.user)
        #         if follower_connection:
        #             data['is_followed'] = True
        #             data['follower_connection_id'] = follower_connection[0].id
        #         else:
        #             data['is_followed'] = False
        # except Exception:
        #     pass
        return data

    def create(self, validated_data):
        data = {
            key: value
            for key, value in validated_data.items()
            if key not in ("password1", "password2")
        }
        data["password"] = validated_data["password1"]
        data["username"] = data["phone"]
        user = self.Meta.model.objects.create_user(**data)
        code = sendsms(phone=user.phone)
        user.phone_verification_code = code
        user.is_active = False
        user.save()
        import telebot

        count = CustomUser.objects.all().count()
        bot = telebot.TeleBot(
            "1309416311:AAEr_hirX_4-DhBLVoM-fpNLUPBQ3vqF4zk"
        )  # You can set parse_mode by default. HTML or MARKDOWN
        message = (
            f"https://edumanager.uz 🎉 saytiga yangi foydalanuvchi qoshildi \n"
            f"Username:{user.username}\nFull Name: {user.first_name} {user.last_name}\n"
            f"Foydalanuvchilar Soni: {count} ga yetdi"
        )
        bot.send_message("-442365863", f"{message}")
        bot.send_message("-557715643", f"{message}")

        return user

    class Meta:
        model = CustomUser
        exclude = [
            "password",
            "is_superuser",
            "user_permissions",
            "groups",
            "email",
            "phone_verification_code",
        ]
        read_only_fields = (
            "username",
            "parents",
            "last_login",
            "is_staff",
            "is_superuser",
            "is_active",
        )
        write_only_fields = ("password1", "password2")


class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "username"]


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
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = CustomUser
        fields = ("token", "username", "password")


class UsersInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class TokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["user"] = UserSerializer(instance=self.user, context=self.context).data
        return data


class CurrentLocationOfDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentLocationOfDriver
        read_only_fields = ('point',)
class RateOfDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateOfDriver
        fields = "__all__"
