from rest_framework import permissions

class EmployeePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve', 'create', 'destroy', 'partial_update']:
            return True
        else:
            return False

class ManagerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve', 'create', 'destroy', 'partial_update']:
            return True
        else:
            return False

class ProjectPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve', 'create', 'destroy', 'partial_update']:
            return True
        else:
            return False