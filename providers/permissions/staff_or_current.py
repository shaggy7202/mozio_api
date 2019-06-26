from rest_framework import permissions


class IsStaffOrCurrentUser(permissions.BasePermission):
    """Permission that allow access to create functionality for everyone
    but limits edit only for current user. Admin user still have all rights"""
    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_staff
        elif view.action == 'create':
            return True
        else:
            return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user
