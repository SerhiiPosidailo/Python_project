from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.auto_parks.models import AutoParkModel
from apps.auto_parks.serializers import AutoParkSerializer
from apps.cars_to_auto_park.serializers import CarSerializer

UserModel = get_user_model()


class AutoParkAddCarView(GenericAPIView):
    queryset = AutoParkModel.objects.all()

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_parks=auto_park)
        ap_serializer = AutoParkSerializer(auto_park)
        return Response(ap_serializer.data, status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        auto_park = self.get_object()
        serializer = CarSerializer(auto_park.cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
