"""
admin페이지에서 Activity, PointRule 모델을 관리
"""
from django.contrib import admin

from .models import Activity, PointRule


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """
    admin페이지에서 관리할 Activity모델을 설정
    """


@admin.register(PointRule)
class PointRuleAdmin(admin.ModelAdmin):
    """
    admin페이지에서 관리할 PointRule모델을 설정
    """
