from django.db import models

from core.models import BaseModel

from apps.cars.managers import CarManager


class CarOneModel(BaseModel):

    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField()
    price = models.IntegerField()

    objects = CarManager()
