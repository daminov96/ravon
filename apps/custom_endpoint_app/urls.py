from django.urls import path
from rest_framework import routers

from .views import *

urlpatterns = [
    path("order/list/", OrderList.as_view(), name="order_list"),
    path("order/create/", OrderCreate.as_view(), name="order_create"),
]
