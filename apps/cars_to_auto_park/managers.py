from django.db import models


class CarToAutoParkManager(models.Manager):
    def get_only_audi(self, name):
        return self.filter(brand=name)
