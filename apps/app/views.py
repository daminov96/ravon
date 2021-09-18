from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from apps.app import filter_params
from drf_yasg.utils import swagger_auto_schema

from .models import (
    Brand,
    Car,
    City,
    Location,
    LocationType,
    MinimumPriceForKm,
    Model,
    Plan,
    Routine,
)
from .serializers import (
    BrandSerializer,
    CarSerializer,
    CitySerializer,
    LocationSerializer,
    LocationTypeSerializer,
    MinimumPriceKmSerializer,
    ModelSerializer,
    PlanSerializer,
    RoutineSerializer,
)


class CityView(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryparams = self.request.query_params
        name = queryparams.get('name', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    @swagger_auto_schema(manual_parameters=filter_params.get_city_params())
    def list(self, request, *args, **kwargs):
        return super(CityView, self).list(kwargs)


class RoutineView(ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryparams = self.request.query_params
        name = queryparams.get('name', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    @swagger_auto_schema(manual_parameters=filter_params.get_routine_params())
    def list(self, request, *args, **kwargs):
        return super(RoutineView, self).list(kwargs)


class MinimumPriceKmView(ModelViewSet):
    queryset = MinimumPriceForKm.objects.all()
    serializer_class = MinimumPriceKmSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryparams = self.request.query_params

        price = queryparams.get('price', None)
        if price:
            queryset = queryset.filter(price=price)
        return queryset

    @swagger_auto_schema(manual_parameters=filter_params.get_min_price_params())
    def list(self, request, *args, **kwargs):
        return super(MinimumPriceKmView, self).list(kwargs)


class PlanView(ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class LocationTypeView(ModelViewSet):
    queryset = LocationType.objects.all()
    serializer_class = LocationTypeSerializer


class LocationView(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class CarView(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryparams = self.request.query_params
        number = queryparams.get('number', None)
        if number:
            queryset = queryset.filter(number=number)

        return queryset

    @swagger_auto_schema(manual_parameters=filter_params.get_car_params())
    def list(self, request, *args, **kwargs):
        return super(CarView, self).list(kwargs)


class BrandView(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryparams = self.request.query_params
        name = queryparams.get('name', None)
        if name:
            queryset = queryset.filter(name=name)

        return queryset

    @swagger_auto_schema(manual_parameters=filter_params.get_brand_params())
    def list(self, request, *args, **kwargs):
        return super(BrandView, self).list(kwargs)


class ModelView(ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryparams = self.request.query_params
        name = queryparams.get('name', None)
        if name:
            queryset = queryset.filter(name=name)

        return queryset

    @swagger_auto_schema(manual_parameters=filter_params.get_model_params())
    def list(self, request, *args, **kwargs):
        return super(ModelView, self).list(kwargs)
