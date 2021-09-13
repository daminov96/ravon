from django.db import models, transaction


class CityManager(models.Manager):

    def get_total_cities(self):
        return self.all().count()


class CarBrandManager(models.Manager):
    print('dasdadasdadadsd')
    def create_brand(self, data):
        instances = []
        print("data", data)
        print("in", instances)
        for instance in data:
            print(instance)
            instances[self.field.name] = self.instance
            instances.append(self.model(**instance))
            print("das", instances)
        self.bulk_create(instances)


class CarManager(models.Manager):
    def create_car_with_brand(self, data):
        with transaction.atomic():
            brand = data.pop('brand')
            print("brand", brand)
            car = self.create(**data)
            print("car", car)
            car.brand.create_brand(brand)
            print(car)
            return car
