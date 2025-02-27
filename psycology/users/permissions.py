from rest_framework import permissions

class IsSuperuser(permissions.BasePermission):
    """
    Custom Allow access
    Allows access only to superusers.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)