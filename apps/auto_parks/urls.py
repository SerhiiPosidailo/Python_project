from django.urls import path

from apps.auto_parks.views import AutoParkAddCarView, AutoParksListCreateView

urlpatterns = [
    path('', AutoParksListCreateView.as_view(), name='auto_parks_list_create'),
    path('/<int:pk>/cars', AutoParkAddCarView.as_view(), name='auto_parks_add_car'),
]