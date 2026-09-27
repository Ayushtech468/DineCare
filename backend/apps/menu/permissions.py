from rest_framework.permissions import BasePermission


class MenuCategoryPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        role = request.user.role

        if view.action in ["list", "retrieve"]:
            return role in ["customer", "admin", "staff"]

        if view.action in ["create", "update", "partial_update"]:
            return role in ["staff", "admin"]

        if view.action == "destroy":
            return role == "admin"

        return False
