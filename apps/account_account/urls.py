from django.urls import path
from rest_framework import routers

from .views import (
    GetUser,
    ResendVerificationCode,
    TokenGenerateView,
    TokenRefreshView,
    UserList,
     CurrentLocationOfDriverViewSet,
    VerifyPhone,
    RateOfDriverViewSet,
)

router = routers.SimpleRouter()
router.register("users", UserList)
router.register("current/location/of/driver", CurrentLocationOfDriverViewSet)
router.register('rate_of_driver', RateOfDriverViewSet)

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
