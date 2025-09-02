# permissions.py
from rest_framework import permissions


class IsOwnerOrAdminToEdit(permissions.BasePermission):
    """
    Allow create for authenticated users,
    allow update/delete only if user is owner or admin.
    """

    def has_permission(self, request, view):
        # Allow GET for everyone, POST only for logged-in users
        if request.method == "POST":
            return request.user.is_authenticated
        return True  # Read methods (GET, HEAD, OPTIONS) are always allowed

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS: GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only allow update/delete if owner or admin
        return obj.author == request.user or request.user.is_staff


class IsAdminOnly(permissions.BasePermission):
    """
    Allow access only to admin users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff
