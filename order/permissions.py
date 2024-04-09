from rest_framework.permissions import BasePermission


class IsOrderOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the order
        return obj.user == request.user