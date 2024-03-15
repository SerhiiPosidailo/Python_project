from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from core.permissions.is_admin_or_write_only_permission import IsAdminOrWriteOnlyPermission

from apps.cars.models import CarOneModel
from apps.cars.serializer import CarOneSerializer

#
#
# class CarsListCreateView(ListCreateAPIView):
#     queryset = CarOneModel.objects.all()
#     serializer_class = CarOneSerializer
#     permission_classes = (IsAuthenticated,)
#
#
# class CarsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
#     queryset = CarOneModel.objects.all()
#     serializer_class = CarOneSerializer
#     permission_classes = (IsAuthenticated, )
