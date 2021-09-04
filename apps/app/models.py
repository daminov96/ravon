from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from parler.models import TranslatableModel, TranslatedFields
from parler.managers import TranslationManager
from apps.constants import *


def validate_interval(value):
    if value < 0.0:
        raise ValidationError(_('%(value)s must be in the range [0.0, infinity]'), params={'value': value}, )


class City(models.Model):
    name = models.TextField(unique=True)
    latitude = models.TextField()
    longtitude = models.TextField()


class Routine(models.Model):
    MORNING_ROUTINE = 1
    NOON_ROUTINE = 2
    AFTERNOON_ROUTINE = 3
    EVENING_ROUTINE = 4
    ROUTINE_CHOICES = (
        (MORNING_ROUTINE, 'Morning Routine'),
        (NOON_ROUTINE, 'Noon Routine'),
        (AFTERNOON_ROUTINE, 'Noon Routine'),
        (EVENING_ROUTINE, 'Evening Routine'),
    )
    routine = models.IntegerField(choices=ROUTINE_CHOICES)
    start_range = models.TimeField(unique=True)
    end_range = models.TimeField(unique=True)


class MinimumPriceForKm(models.Model):
    price = models.FloatField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('city', 'routine')


class Plan(TranslatableModel):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    translations = TranslatedFields(
        name=models.CharField(max_length=100)
    )
    min_price = models.FloatField(validators=[validate_interval])
    rate = models.FloatField(default=1)
    image = models.ImageField(upload_to='plan_image/')
    objects = TranslationManager()


class LocationType(TranslatableModel):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    translations = TranslatedFields(
        name=models.CharField(max_length=300)
    )


class Location(TranslatableModel):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    translations = TranslatedFields(
        location_name=models.CharField(max_length=100)
    )
    location_type = models.ForeignKey(LocationType, on_delete=models.CASCADE, related_name='locations', null=True,
                                      blank=True)
    owner = models.ForeignKey('account_account.CustomUser', related_name='locations', on_delete=models.SET_NULL,
                              null=True)
    model_object_id = models.CharField(max_length=150)
    model_object_type = models.CharField(max_length=50)
    lat = models.CharField(max_length=150)
    long = models.CharField(max_length=150)


class Brand(TranslatableModel):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    translations = TranslatedFields(
        name=models.CharField(max_length=100)
    )
    logo = models.FileField(null=True, blank=True)


class Model(TranslatableModel):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    translations = TranslatedFields(
        name=models.CharField(max_length=100)
    )
    image = models.ImageField(upload_to='model_image/')


class Car(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True, blank=True)
    min_price = models.FloatField(validators=[validate_interval])
    image = models.ImageField(upload_to='plan_image/')
    color = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    available_wheelchair = models.BooleanField(default=False)
    has_seat_for_babes = models.BooleanField(default=False)
    number_of_seats = models.IntegerField(default=4)




class RateOfDriver(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    on_trip = models.OneToOneField(Trip, on_delete=models.CASCADE)
    customer = models.ForeignKey('account_account.CustomUser', related_name='rated_trips', on_delete=models.SET_NULL,
                                 null=True)
    driver = models.ForeignKey('account_account.CustomUser', related_name='rates', on_delete=models.SET_NULL, null=True)
    rate = models.IntegerField(choices=RATE_CHOICES)
    comment = models.TextField()
