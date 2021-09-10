from django.contrib import admin
from apps.app import models as app_models
from mptt.admin import DraggableMPTTAdmin
from parler.admin import TranslatableAdmin


@admin.register(app_models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'latitude', 'longtitude']


@admin.register(app_models.Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ['id', 'routine', 'start_range', 'end_range']


@admin.register(app_models.MinimumPriceForKm)
class MinimumPriceForKmAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'city', 'routine']


@admin.register(app_models.Plan)
class PlanAdmin(TranslatableAdmin):
    list_display = ('id', 'created', 'updated', 'name', 'min_price', 'rate', 'image')


@admin.register(app_models.LocationType)
class LocationTypeAdmin(TranslatableAdmin):
    list_display = ('id', 'created', 'updated', 'name')


@admin.register(app_models.Location)
class LocationAdmin(TranslatableAdmin):
    list_display = ('id', 'location_name', 'created', 'updated')


@admin.register(app_models.Brand)
class BrandAdmin(TranslatableAdmin):
    list_display = ('id', 'name', 'created', 'updated', 'logo')


@admin.register(app_models.Model)
class BrandAdmin(TranslatableAdmin):
    list_display = ('id', 'name', 'created', 'updated', 'image')


@admin.register(app_models.Car)
class CarAdmin(TranslatableAdmin):
    list_display = ('id', 'created', 'updated', 'brand', 'model', 'color', 'number')
