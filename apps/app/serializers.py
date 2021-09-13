from parler_rest.fields import TranslatedFieldsField
from parler_rest.serializers import TranslatableModelSerializer
from rest_framework import serializers

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


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["id", "name", "latitude", "longtitude"]


class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = ["id", "routine", "start_range", "end_range"]


class MinimumPriceKmSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinimumPriceForKm
        fields = ["id", "price", "city", "routine"]


class PlanSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Plan)

    class Meta:
        model = Plan
        fields = ["translations", "id", "min_price", "rate", "image"]


class LocationTypeSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=LocationType)

    class Meta:
        model = LocationType
        fields = ["translations", "created", "updated"]


class LocationSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Location)

    class Meta:
        model = Location
        fields = [
            "translations",
            "id",
            "location_type",
            "owner",
            "model_object_id",
            "model_object_type",
            "lat",
            "long",
        ]


class CarSerializer(serializers.ModelSerializer):
    image = serializers.FileField(source='details_sample.image', read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'brand', 'model', 'min_price', 'image', 'color', 'number', 'available_wheelchair', 'has_seat_for_babes', 'number_of_seats']


class BrandSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Brand)

    class Meta:
        model = Brand
        fields = ['id', 'translations', 'logo']


class ModelSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Model)

    class Meta:
        model = Model
        fields = ['id', 'translations', 'image']

