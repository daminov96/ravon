from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from parler.admin import TranslatableAdmin

from apps.app import models as app_models


@admin.register(app_models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "latitude", "longtitude"]


@admin.register(app_models.Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ["id", "routine", "start_range", "end_range"]


@admin.register(app_models.MinimumPriceForKm)
class MinimumPriceForKmAdmin(admin.ModelAdmin):
    list_display = ["id", "price", "city", "routine"]


class PlanAdmin(TranslatableAdmin):
    list_display = ("id", "created", "updated", "name", "min_price", "rate", "image")


@admin.register(app_models.LocationType)
class LocationTypeAdmin(TranslatableAdmin):
    list_display = ("id", "created", "updated", "name")


@admin.register(app_models.Location)
class LocationAdmin(TranslatableAdmin):
    list_display = ("id", "location_name", "created", "updated")


@admin.register(app_models.Brand)
class BrandAdmin(TranslatableAdmin):
    list_display = ("id", "name", "created", "updated", "logo")


@admin.register(app_models.Model)
class BrandAdmin(TranslatableAdmin):
    list_display = ("id", "name", "created", "updated", "image")


@admin.register(app_models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "created", "updated", "brand", "model", "color", "gos_number")


@admin.register(app_models.PlanRequest)
class PlanRequestAdmin(admin.ModelAdmin):
    list_display = ["id", 'driver', "plan", 'status']


@admin.register(app_models.DriverLicensePhotoCheck)
class DriverLicensePhotoCheckAdmin(admin.ModelAdmin):
    list_display = ["id", "driver", 'is_verified']


@admin.register(app_models.CarTechPassportCheck)
class CarTechPassportCheckAdmin(admin.ModelAdmin):
    list_display = ["id", "driver", 'is_verified']


@admin.register(app_models.CarColor)
class CarColorAdmin(admin.ModelAdmin):
    list_display = ["id", 'hex_code', 'name']


admin.site.register(app_models.Plan, PlanAdmin)
