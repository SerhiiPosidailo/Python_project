from django.db import models

from core.models import BaseModel

from apps.auto_parks.models import AutoParkModel
from apps.cars_to_auto_park.managers import CarToAutoParkManager


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars_to_auto_park'

    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField()
    price = models.IntegerField()
    auto_parks = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')

    objects = CarToAutoParkManager()
