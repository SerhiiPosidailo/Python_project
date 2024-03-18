from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser

from apps.cars_to_auto_park.models import CarModel
from apps.cars_to_auto_park.serializers import CarSerializer


class CarsRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAdminUser,)
