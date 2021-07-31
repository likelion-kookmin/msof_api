"""# questions admin"""
from django.contrib import admin

from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """ ## QuestionAdmin
        - admin에서 관리할 Question 모델 설정
    """

    list_display = [
        'author',
        'title',
        'content',
        'status',
        'viewed_count',
        'liked_count',
        'disliked_count',
    ]

    list_editable = [
        'status',
    ]

    search_fields = [
        'author__name',
        'title',
        'content',
    ]
