from django.urls import path
from rest_framework import routers

from .views import (
    BrandView,
    CarColorViewSet,
    CarTechPassportCheckViewSet,
    CarView,
    CityView,
    DriverLicensePhotoCheckViewSet,
    LocationTypeView,
    LocationView,
    MinimumPriceKmView,
    ModelView,
    PlanRequestViewSet,
    PlanView,
    RoutineView,
    # TripView,
)

router = routers.SimpleRouter()

router.register("city", CityView)
router.register("routine", RoutineView)
router.register("routine", RoutineView)
router.register("min_price_for_km", MinimumPriceKmView)
router.register("plan", PlanView)
router.register("location_type", LocationTypeView)
router.register("location", LocationView)
router.register("car", CarView)
router.register("brand", BrandView)
router.register("model", ModelView)
router.register("car_color", CarColorViewSet)
router.register("plan_request", PlanRequestViewSet)
router.register("driver_license_photoCheck", DriverLicensePhotoCheckViewSet)
router.register("car_tech_passport_check", CarTechPassportCheckViewSet)

urlpatterns = router.urls + [
    # path('trip/', TripView.as_view(), name='trip'),
]
