"""# comments admin
- CommentAdmin
"""
from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """## CommentAdmin
        - admin에서 관리할 Comment 모델 설정
    """

    list_display = [
        'author',
        'question',
        'parent',
        'selected',
        'content',
        'status',
        'liked_count',
        'disliked_count',
    ]

    list_editable = [
        'status',
    ]

    list_filter = [
        'author',
        'question',
        'parent',
        'selected',
        'status',
    ]

    search_fields = [
        'content',
        'author__name',
        'question__title',
        'question__content',
    ]

    ordering = [
        '-updated_at',
    ]
