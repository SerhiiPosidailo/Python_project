from rest_framework import serializers

from apps.cars.models import CarOneModel


class CarOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarOneModel
        fields = ('id', 'brand', 'model', 'year', 'price', 'created_at', 'updated_at')
