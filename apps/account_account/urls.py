from django.urls import path
from rest_framework import routers

from .views import GetUser, UserList, SystemStatistics, TokenGenerateView, CreateCashilokFill, CashelokFillViewSet, \
    TokenRefreshView, Statistics, VerifyPhone, CashelokViewSet, ResendVerificationCode, FollowConnectionViewSet, \
    Followers, Followings, FollowerFollowingStatistics, PostsFilesView, PostsCommentsView, VideoViewSet, \
    CommentOfVideoViewSet, PostsViewSet

router = routers.SimpleRouter()
router.register('users', UserList)
router.register('casheloks', CashelokViewSet)
router.register('cashelokfill', CashelokFillViewSet)
router.register('follow/connections', FollowConnectionViewSet)
router.register('posts/files', PostsFilesView)
router.register('comments_of_post', PostsCommentsView)
router.register('posts', PostsViewSet)
router.register('videos', VideoViewSet)
router.register('comments_of_video', CommentOfVideoViewSet)

urlpatterns = router.urls + [
    path('token/', TokenGenerateView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('current_user/', GetUser.as_view()),
    path('statistics/', Statistics.as_view(), name='statistics'),
    path('system_statistics/', SystemStatistics.as_view(), name='system_statistics'),
    path('verify-phone/', VerifyPhone.as_view(), name='verify-phone'),
    path('resend/verification/password/', ResendVerificationCode.as_view(), name='resend_verification_password'),
    path('fill/cashilok/', CreateCashilokFill.as_view()),
    path('followers', Followers.as_view()),
    path('followings', Followings.as_view()),
    path('follow/connection/statistics/', FollowerFollowingStatistics.as_view()),
]

