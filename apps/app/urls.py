from django.urls import path
from rest_framework import routers

from .views import (
    BrandView,
    CarView,
    CityView,
    LocationTypeView,
    LocationView,
    MinimumPriceKmView,
    ModelView,
    PlanView,
    RoutineView,
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

urlpatterns = router.urls + [
]
