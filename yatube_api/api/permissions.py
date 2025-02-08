from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение: изменение/удаление объекта разрешено только автору.
    Остальные запросы – только для чтения.
    """
    def has_object_permission(self, request, view, obj):
        # Безопасные методы (GET, HEAD, OPTIONS) разрешены всем
        if request.method in permissions.SAFE_METHODS:
            return True
        # Изменять можно только если пользователь – автор
        return obj.author == request.user
