from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from parler.models import TranslatableModel, TranslatedFields
from parler.managers import TranslationManager
from apps.constants import *


def validate_interval(value):
    if value < 0.0:
        raise ValidationError(_('%(value)s must be in the range [0.0, infinity]'), params={'value': value}, )


class Plan(TranslatableModel):
    created = models.DateTimeField(auto_now_add=True,  null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    translations = TranslatedFields(
        name=models.CharField(max_length=100)
    )
    min_price = models.FloatField(validators=[validate_interval])
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
    location_type = models.ForeignKey(LocationType, on_delete=models.CASCADE, related_name='locations', null=True, blank=True)
    owner = models.ForeignKey('account_account.CustomUser', related_name='locations', on_delete=models.SET_NULL,
                              null=True)
    model_object_id = models.CharField(max_length=150)
    model_object_type = models.CharField(max_length=50)
    lat = models.CharField(max_length=150)
    long = models.CharField(max_length=150)


class Brand(TranslatableModel):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True,  null=True)
    translations = TranslatedFields(
        name=models.CharField(max_length=100)
    )


class Model(TranslatableModel):
    created = models.DateTimeField(auto_now_add=True,  null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    translations = TranslatedFields(
        name=models.CharField(max_length=100)
    )
    image = models.ImageField(upload_to='model_image/')


class Car(models.Model):
    created = models.DateTimeField(auto_now_add=True,  null=True)
    updated = models.DateTimeField(auto_now=True,  null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True, blank=True)
    min_price = models.FloatField(validators=[validate_interval])
    image = models.ImageField(upload_to='plan_image/')
    color = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    available_wheelchair=models.BooleanField(default=False)
    has_seat_for_babes=models.BooleanField(default=False)
    number_of_seats=models.IntegerField(default=4)


class ReasonToCancelTrip(models.Model):
    created = models.DateTimeField(auto_now_add=True,  null=True)
    updated = models.DateTimeField(auto_now=True,  null=True)
    reason = models.CharField(max_length=300)


class Trip(models.Model):
    created = models.DateTimeField(auto_now_add=True,  null=True)
    updated = models.DateTimeField(auto_now=True,  null=True)
    driver = models.ForeignKey('account_account.CustomUser', on_delete=models.SET_NULL, null=True,
                               related_name='driver_trips')
    customer = models.ForeignKey('account_account.CustomUser', on_delete=models.SET_NULL, null=True,
                                 related_name='customer_trips')
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, related_name='trips', null=True)
    state = models.CharField(max_length=30, choices=STATE_CHOICES_OF_TRIP)
    from_point = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='starts')
    to_point = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='distinations')
    price = models.FloatField(default=0)
    reason_to_cancel = models.ManyToManyField(ReasonToCancelTrip, related_name='trips', null=True, blank=True)


class TripPath(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='paths')
    long = models.CharField(max_length=200)
    lat = models.CharField(max_length=200)


class RateOfDriver(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    on_trip = models.OneToOneField(Trip, on_delete=models.CASCADE)
    customer = models.ForeignKey('account_account.CustomUser', related_name='rated_trips', on_delete=models.SET_NULL,
                                 null=True)
    driver = models.ForeignKey('account_account.CustomUser', related_name='rates', on_delete=models.SET_NULL, null=True)
    rate = models.IntegerField(choices=RATE_CHOICES)
    comment = models.TextField()
