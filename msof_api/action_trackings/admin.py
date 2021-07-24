"""admin페이지에서 ActionTracking, PointRule 모델을 관리"""
from django.contrib import admin

from .models import ActionTracking, PointRule


@admin.register(ActionTracking)
class ActionTrackingAdmin(admin.ModelAdmin):
    """admin페이지에서 관리할 ActionTracking 모델 설정"""


@admin.register(PointRule)
class PointRuleAdmin(admin.ModelAdmin):
    """admin페이지에서 관리할 PointRule모델을 설정"""
