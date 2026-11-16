from rest_framework import permissions



class IsUserOwnerOrGetAndPostOnly(permissions.BasePermission):

    """
    Custom permission for UserViewset to only allow users to edit their profile, otherwise get and only post only"""
    def has_permission(self, request, view):
        return True
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_anonymous:
            return request.user == obj
        return False
