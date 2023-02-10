from rest_framework.permissions import BasePermission

from users.constants import Role
from users.models import User


class RoleIsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.ADMIN


class IsSpecificUser(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj: User):
        return obj.email == request.user.email
