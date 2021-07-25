"""# comments permissions"""
from rest_framework import permissions


class CommentEditableOrDestroyablePermission(permissions.BasePermission):
    """## CommentEditableOrDestroyablePermission
        - 댓글을 수정 혹은 삭제할 수 있는 권한을 명시하는 클래스
    """

    def has_object_permission(self, request, view, obj):
        """### has_object_permission"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and (obj.author == request.user or request.user.is_staff)
