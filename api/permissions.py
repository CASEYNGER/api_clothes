from rest_framework import permissions


class CanAddClothPermission(permissions.BasePermission):
    """
    Кастомный пермишен.

    Разрешает создание, изменение и удаление одежды только для персонала.
    """

    def has_permission(self, request, view):
        """
        Метод ограничения доступа.

        Предоставляет доступ всем пользователям
        к безопасным методам, а также ограничивает использование
        других методов.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
