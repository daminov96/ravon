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
        queryset = self.get_queryset()
        queryparams = self.request.query_params

        name = queryparams.get('name', None)
        if name:
            queryset = queryset.filter(name__incontains=name)

        return queryset

    @swagger_auto_schema(manual_parameters=filter_params.get_city_params())
    def list(self, request, *args, **kwargs):
        return super(CityView).list(**kwargs)


class RoutineView(ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer


class MinimumPriceKmView(ModelViewSet):
    queryset = MinimumPriceForKm.objects.all()
    serializer_class = MinimumPriceKmSerializer


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
    # queryset = Car.objects.select_related('brand', 'model').all()
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class BrandView(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ModelView(ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
