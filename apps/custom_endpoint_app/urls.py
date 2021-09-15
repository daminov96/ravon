from django.urls import path
from rest_framework import routers
from .views import OrderList


urlpatterns = [
    path('order/list/', OrderList.as_view(), name='order_list'),

]


