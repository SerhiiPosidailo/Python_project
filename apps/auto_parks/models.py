from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseModel

UserModel = get_user_model()


class AutoParkModel(BaseModel):
    class Meta:
        db_table = 'auto_parks'

    name = models.CharField(max_length=20)
    auth_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auto_park')

