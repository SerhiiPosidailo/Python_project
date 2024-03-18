from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseModel

UserModel = get_user_model()


class CarOneModel(BaseModel):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField()
    price = models.IntegerField()
    auth_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='car')
