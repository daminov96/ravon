from django.db import models, transaction
from django.db.models import F, Q


class CityManager(models.Manager):
    def get_total_cities(self):
        return self.all().count()


class CarBrandManager(models.Manager):
    def create_brand(self, data):
        instances = []
        for instance in data:
            instances[self.field.name] = self.instance
            instances.append(self.model(**instance))
        self.bulk_create(instances)


class CarManager(models.Manager):
    def create_car_with_brand(self, data):
        with transaction.atomic():
            brand = data.pop("brand")
            model = data.pop("model")
            car = self.create(**data)
            car.brand = brand
            car.model = model
            car.save()
            return car

    def get_car_detail(self):
        query = self.select_related("brand").all()
        print("query", query)
        return query
        # return self.get_queryset().all()

    def get_cars(self):
        print('get carsssss')
        return self.select_related("brand")


# class RoutineManager(models.Manager):
#     def get_routine(self, routine):
#         queryset =
