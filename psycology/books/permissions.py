from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Custom permition
    return Bool(is Owner of commnet)
    '''

    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user 