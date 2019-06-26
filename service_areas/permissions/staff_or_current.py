from rest_framework import permissions


class IsStaffOrCurrentUser(permissions.BasePermission):
    """Permission that allow access to create functionality for everyone
    but limits edit only for current user. Admin user still have all rights"""
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.provider.user == request.user
