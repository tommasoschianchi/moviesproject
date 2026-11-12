from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
       if request.method in permissions.SAFE_METHODS:
         return True
       return obj.owner == request.user

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.staff or request.user.is_superuser

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.is_staff or request.user.is_superuser
class AllowAny(permissions.BasePermission):
    def has_permission(self, request, view):
        return True