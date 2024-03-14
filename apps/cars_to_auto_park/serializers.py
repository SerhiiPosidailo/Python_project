from rest_framework import serializers

from apps.cars_to_auto_park.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'model', 'year', 'price', 'created_at', 'updated_at')