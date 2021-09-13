from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView

from .models import City, LocationType, MinimumPriceForKm, Plan, Routine, Location, Car, Brand, Model
from .serializers import (
    CitySerializer,
    LocationSerializer,
    LocationTypeSerializer,
    MinimumPriceKmSerializer,
    PlanSerializer,
    RoutineSerializer,
    CarSerializer,
    BrandSerializer,
    ModelSerializer
)


class CityView(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


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
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarCreateView(CreateAPIView):
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        serializer.instance = Car.objects.create_car_with_brand(
            serializer.validated_data
        )


class BrandView(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ModelView(ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
