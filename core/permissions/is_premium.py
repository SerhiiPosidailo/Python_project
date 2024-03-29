from rest_framework.permissions import BasePermission


class IsPremium(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_premium)
