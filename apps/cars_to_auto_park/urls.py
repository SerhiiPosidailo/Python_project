from django.urls import path

from apps.cars_to_auto_park.views import CarsRetrieveUpdateDeleteView

urlpatterns = [
    path('/<int:pk>', CarsRetrieveUpdateDeleteView.as_view(), name='cars_retrieve_update_delete')
]
