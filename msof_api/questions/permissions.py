"""Question Permission Class Module"""
from rest_framework import permissions


class QuestionEditableOrDestroyablePermission(permissions.BasePermission):
    """QuestionEditableOrDestroyablePermission<br>

    Custom Permisson Class to allow owners and admin of an object to edit or destroy it.
    """

    def has_object_permission(self, request, view, obj):
        """has_object_permission<br>

        Read permissions are allowed to any request.
        Write permissions are only allowed to the owner or staff.
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and (obj.author == request.user or request.user.is_staff)
