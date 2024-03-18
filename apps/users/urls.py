from django.urls import path

from .views import (
    AdminToUserView,
    UserAddAutoParkView,
    UserBlockView,
    UserCreateCarView,
    UserCreateView,
    UserIsPremiumView,
    UserNotPremiumView,
    UserToAdminView,
    UserUnBlockView,
)

urlpatterns = [
    path('', UserCreateView.as_view(), name='user_create'),
    path('/<int:pk>/autopark', UserAddAutoParkView.as_view(), name='create_auto_park'),
    path('/<int:pk>/cars', UserCreateCarView.as_view(), name='create_car'),
    path('/<int:pk>/to_admin', UserToAdminView.as_view(), name='user_to_admin'),
    path('/<int:pk>/to_user', AdminToUserView.as_view(), name='admin_to_user'),
    path('/<int:pk>/block', UserBlockView.as_view(), name='user_block'),
    path('/<int:pk>/un_block', UserUnBlockView.as_view(), name='user_un_block'),
    path('/<int:pk>/premium', UserIsPremiumView.as_view(), name='user_premium'),
    path('/<int:pk>/not_premium', UserNotPremiumView.as_view(), name='user_not_premium'),

]
