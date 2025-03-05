from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Custom permition
    return Bool(is Owner of comment)
    '''

    def has_object_permission(self, request, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user 