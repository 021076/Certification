from rest_framework.permissions import BasePermission


class IsActive(BasePermission):
    """ Разрешение для активных пользователей"""

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        else:
            return False
