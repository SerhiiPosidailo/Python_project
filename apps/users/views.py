from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from core.permissions.is_auto_park import IsAutoPark
from core.permissions.is_seperuser import IsSeperuser

from apps.auto_parks.serializers import AutoParkSerializer
from apps.cars.serializer import CarOneSerializer
from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer

UserModel = get_user_model()


class UserCreateView(ListCreateAPIView):
    serializer_class = UserSerializer


class UserAddAutoParkView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsAutoPark,)

    def post(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, id=pk)
        data = self.request.data
        serializer = AutoParkSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auth_user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        user = self.get_object()
        serializer = AutoParkSerializer(user.auto_park, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserCreateCarView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        user = get_object_or_404(UserModel, id=pk)

        if not user.is_premium and user.car_count >= 1:
            return Response({"error": "Only premium users can create multiple cars"},
                            status=status.HTTP_403_FORBIDDEN)
        data = self.request.data
        serializer = CarOneSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auth_user=user)
        user.car_count += 1
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        user = self.get_object()
        serializer = CarOneSerializer(user.car, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class UserToAdminView(GenericAPIView):
    permission_classes = (IsSeperuser,)

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def put(self, *args, **kwargs):
        user: User = self.get_object()

        if not user.is_staff:
            user.is_staff = True
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class AdminToUserView(GenericAPIView):
    permission_classes = (IsSeperuser,)

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def put(self, *args, **kwargs):
        user: User = self.get_object()

        if user.is_staff:
            user.is_staff = False
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserBlockView(GenericAPIView):
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def put(self, *args, **kwargs):
        user: User = self.get_object()

        if user.is_active:
            user.is_active = False
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserUnBlockView(GenericAPIView):
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def put(self, *args, **kwargs):
        user: User = self.get_object()

        if not user.is_active:
            user.is_active = True
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserIsPremiumView(GenericAPIView):
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def put(self, *args, **kwargs):
        user: User = self.get_object()

        if not user.is_premium:
            user.is_premium = True
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserNotPremiumView(GenericAPIView):
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def put(self, *args, **kwargs):
        user: User = self.get_object()

        if user.is_premium:
            user.is_premium = False
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)
