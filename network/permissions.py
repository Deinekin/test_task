from rest_framework.permissions import BasePermission


class UserIsActive(BasePermission):
    """Проверка активен ли пользователь и выдача доступа, если активен"""

    def has_permission(self, request, view) -> bool:
        return request.user.is_authenticated and request.user.is_active
