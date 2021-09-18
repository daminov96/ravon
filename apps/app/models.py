from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.managers import TranslationManager
from parler.models import TranslatableModel, TranslatedFields

from apps.account_account.models import CustomUser
from apps.constants import *

from .managers import CarBrandManager, CarManager, CityManager


def validate_interval(value):
    if value < 0.0:
        raise ValidationError(
            _("%(value)s must be in the range [0.0, infinity]"),
            params={"value": value},
        )


class City(models.Model):
    name = models.TextField(unique=True)
    latitude = models.TextField()
    longtitude = models.TextField()

    objects = CityManager()


class Routine(models.Model):
    MORNING_ROUTINE = 1
    NOON_ROUTINE = 2
    AFTERNOON_ROUTINE = 3
    EVENING_ROUTINE = 4
    ROUTINE_CHOICES = (
        (MORNING_ROUTINE, "Morning Routine"),
        (NOON_ROUTINE, "Noon Routine"),
        (AFTERNOON_ROUTINE, "Noon Routine"),
        (EVENING_ROUTINE, "Evening Routine"),
    )
    routine = models.IntegerField(choices=ROUTINE_CHOICES)
    start_range = models.TimeField(unique=True)
    end_range = models.TimeField(unique=True)


class MinimumPriceForKm(models.Model):
    price = models.FloatField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("city", "routine")


class Plan(TranslatableModel):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    translations = TranslatedFields(name=models.CharField(max_length=100))
    min_price = models.FloatField(validators=[validate_interval])
    rate = models.FloatField(default=1)
    image = models.ImageField(upload_to="plan_image/")
    objects = TranslationManager()

    def __str__(self):
        return self.safe_translation_getter("name") or ""


class PlanRequest(models.Model):
    driver = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    car_front_image = models.FileField(null=True, blank=True, upload_to="plan_request/")
    car_left_image = models.FileField(null=True, blank=True, upload_to="plan_request/")
    car_back_image = models.FileField(null=True, blank=True, upload_to="plan_request/")
    car_right_image = models.FileField(null=True, blank=True, upload_to="plan_request/")
    car_front_interior_image = models.FileField(
        null=True, blank=True, upload_to="plan_request/"
    )
    car_rear_interior_image = models.FileField(
        null=True, blank=True, upload_to="plan_request/"
    )
    car_open_truck_image = models.FileField(
        null=True, blank=True, upload_to="plan_request/"
    )
    status = models.CharField(
        choices=PLAN_REQUEST_STATUS_CHOICES, default=PLAN_REQUEST_CREATED, max_length=60
    )


class LocationType(TranslatableModel):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    translations = TranslatedFields(name=models.CharField(max_length=300))


class Location(TranslatableModel):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    translations = TranslatedFields(location_name=models.CharField(max_length=100))
    location_type = models.ForeignKey(
        LocationType,
        on_delete=models.CASCADE,
        related_name="locations",
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        "account_account.CustomUser",
        related_name="locations",
        on_delete=models.SET_NULL,
        null=True,
    )
    model_object_id = models.CharField(max_length=150)
    model_object_type = models.CharField(max_length=50)
    lat = models.CharField(max_length=150)
    long = models.CharField(max_length=150)


class Brand(TranslatableModel):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    translations = TranslatedFields(name=models.CharField(max_length=100))
    logo = models.FileField(null=True, blank=True)

    # objects = CarBrandManager()
    def __str__(self):
        return self.safe_translation_getter("name") or ""


class Model(TranslatableModel):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    translations = TranslatedFields(name=models.CharField(max_length=100))
    image = models.ImageField(upload_to="model_image/")

    def __str__(self):
        return self.safe_translation_getter("name") or ""


class CarColor(models.Model):
    hex_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=30, unique=True)


class Car(models.Model):
    STANDARD = "standard"
    COMFORT = "comfort"
    LUXURY = "luxury"
    TYPE = (
        (STANDARD, "Standard"),
        (COMFORT, "Comfort"),
        (LUXURY, "Luxury"),
    )
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    color = models.ForeignKey(CarColor, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True, blank=True)
    min_price = models.FloatField(validators=[validate_interval])
    image = models.ImageField(upload_to="plan_image/")
    manifacture_year = models.IntegerField(null=True)
    gos_number = models.CharField(max_length=100)
    available_wheelchair = models.BooleanField(default=False)
    has_seat_for_babes = models.BooleanField(default=False)
    number_of_seats = models.IntegerField(default=4)
    type_of_car = models.CharField(max_length=100, choices=TYPE, null=True)
    # objects = CarManager()


class DriverLicensePhotoCheck(models.Model):
    driver = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    front_image = models.FileField(null=True, blank=True)
    back_image = models.FileField(null=True, blank=True)
    licence_and_driver = models.FileField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)


class CarTechPassportCheck(models.Model):
    driver = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    front_image = models.FileField(null=True, blank=True)
    back_image = models.FileField(null=True, blank=True)
    tech_passport_and_driver = models.FileField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)


# class TaxiPark(models.Model):
#     name = models.CharField(max_length=200)
#     info = RichTextField()
