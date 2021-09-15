from django.urls import path
from rest_framework import routers

import account_pb2_grpc

from .services import UserService
from .views import (
    GetUser,
    ResendVerificationCode,
    TokenGenerateView,
    TokenRefreshView,
    UserList,
    VerifyPhone,
)

router = routers.SimpleRouter()
router.register("users", UserList)
urlpatterns = router.urls + [
    path("token/", TokenGenerateView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("current_user/", GetUser.as_view()),
    path("verify-phone/", VerifyPhone.as_view(), name="verify-phone"),
    path(
        "resend/verification/password/",
        ResendVerificationCode.as_view(),
        name="resend_verification_password",
    ),
]
