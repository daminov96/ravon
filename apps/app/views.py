from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet

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
