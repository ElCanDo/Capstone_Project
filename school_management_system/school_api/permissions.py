from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
    

class IsTeacherReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and not request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return True


class IsStudentReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user and not request.user.is_staff
    
    def has_object_permission(self, request, view, obj):
        return True