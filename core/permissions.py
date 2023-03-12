from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from modules.user.models import Role


class LecturerAndHigher(BasePermission):
    def __init__(self, allowed_methods) -> None:
        super().__init__()
        self.allowed_methods = allowed_methods

    def has_permission(self, request: Request, view):
        role = Role.objects.get(name="LECTURER")
        try:
            return role.int_level <= request.user.role.int_level
        except Exception:
            return False


class SupportAndHigher(BasePermission):
    def __init__(self, allowed_methods) -> None:
        super().__init__()
        self.allowed_methods = allowed_methods

    def has_permission(self, request: Request, view):
        role = Role.objects.get(name="SUPPORT")
        try:
            return role.int_level <= request.user.role.int_level
        except Exception:
            return False


class ModeratorAndHigher(BasePermission):
    def __init__(self) -> None:
        super().__init__()

    def has_permission(self, request: Request, view):
        role = Role.objects.get(name="MODERATOR")
        try:
            return role.int_level <= request.user.role.int_level
        except Exception:
            return False


class AdminAndHigher(BasePermission):
    def __init__(self) -> None:
        super().__init__()

    def has_permission(self, request: Request, view):
        role = Role.objects.get(name="ADMIN")
        try:
            return role.int_level <= request.user.role.int_level
        except Exception:
            return False
