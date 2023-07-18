from rest_framework import permissions


# Allows you to only edit your profile if you're logged-in.
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
    return obj.owner == request.user
