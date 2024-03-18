from django.urls import path

from apps.auto_parks.views import AutoParkAddCarView

urlpatterns = [
    path('/<int:pk>/cars', AutoParkAddCarView.as_view(), name='auto_parks_add_car'),
]
