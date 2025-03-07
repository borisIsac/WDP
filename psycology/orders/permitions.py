from rest_framework import permissions

class IsNotAllowDeletePut(permissions.BasePermission):
    '''
    Custom permition
    return Bool(HTML Method is DELETE, PUT, PATCH)
    '''

    def has_object_permission(self, request,view, obj):
        
        ALLOWED_METHODS = ['POST', 'GET']        
        return bool(request.method in ALLOWED_METHODS)
        