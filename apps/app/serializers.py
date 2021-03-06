from parler_rest.fields import TranslatedFieldsField
from parler_rest.serializers import TranslatableModelSerializer
from rest_framework import serializers

from apps.account_account.models import CustomUser

from .models import (
    Brand,
    Car,
    CarColor,
    CarTechPassportCheck,
    City,
    DriverLicensePhotoCheck,
    Location,
    LocationType,
    MinimumPriceForKm,
    Model,
    Plan,
    PlanRequest,
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
        fields = ["id", "username", "first_name", "last_name", "gender"]


class CarSerializer(serializers.ModelSerializer):
    owner = UserSerializerForCar(read_only=True)

    class Meta:
        model = Car
        fields = [
            "id",
            "image",
            "brand",
            "model",
            "min_price",
            "color",
            "available_wheelchair",
            "has_seat_for_babes",
            "number_of_seats",
            "type_of_car",
            "created",
            "updated",
            "owner",
            "manifacture_year",
            "gos_number",
        ]


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


class PlanRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanRequest
        fields = "__all__"


class CarColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarColor
        fields = "__all__"


class DriverLicensePhotoCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverLicensePhotoCheck
        fields = "__all__"


class CarTechPassportCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarTechPassportCheck
        fields = "__all__"


class LocationSerializerForTrip(serializers.Serializer):
    location_name = serializers.CharField(max_length=100)
    model_object_id = serializers.CharField(max_length=150)
    model_object_type = serializers.CharField(max_length=50)
    lat = serializers.CharField(max_length=150)
    long = serializers.CharField(max_length=150)


class ReasonToCancelTrip(serializers.Serializer):
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()
    reason = serializers.CharField(max_length=300)


class TripSerializer(serializers.Serializer):
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()
    driver = serializers.CharField(max_length=250)
    customer = serializers.CharField(max_length=250)
    plan = serializers.CharField(max_length=250)
    state = serializers.CharField(max_length=250)
    from_point = LocationSerializerForTrip(many=True)
    to_point = LocationSerializerForTrip(many=True)
    price = serializers.FloatField()
    reason_to_cancel = ReasonToCancelTrip(many=True)

