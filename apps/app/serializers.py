from parler_rest.fields import TranslatedFieldsField
from parler_rest.serializers import TranslatableModelSerializer
from rest_framework import serializers
from apps.account_account.models import CustomUser
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
        fields = "__all__"


class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = "__all__"


class MinimumPriceKmSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinimumPriceForKm
        fields = "__all__"


class PlanSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Plan)

    class Meta:
        model = Plan
        fields = "__all__"


class LocationTypeSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=LocationType)

    class Meta:
        model = LocationType
        fields = "__all__"


class LocationSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Location)

    class Meta:
        model = Location
        fields = "__all__"


class UserSerializerForCar(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'gender']


class CarSerializer(serializers.ModelSerializer):
    owner = UserSerializerForCar(read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'image', 'brand', 'model', 'min_price', 'color', 'number', 'available_wheelchair',
                  'has_seat_for_babes', 'number_of_seats', 'type_of_car', 'created', 'updated', 'owner']


class BrandSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Brand)

    class Meta:
        model = Brand
        fields = "__all__"


class ModelSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Model)

    class Meta:
        model = Model
        fields = "__all__"
