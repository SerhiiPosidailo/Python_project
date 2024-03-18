from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsAdminOrWriteOnlyPermission(BasePermission):
    def has_permission(self, request: Request, view):
        user = request.user
        if request.method == 'POST':
            return True or user.is_staff
        return user.is_staff
