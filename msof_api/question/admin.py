"""admin 페이지에서 관리할 모델 추가 및 정의 설정 파일"""
from django.contrib import admin

from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Admin에서 설정할 Question 정의"""
