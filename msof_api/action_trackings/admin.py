"""# action_trackings admin
- ActionTrackingAdmin
- PointRuleAdmin
"""
from django.contrib import admin

from .models import ActionTracking, PointRule


@admin.register(ActionTracking)
class ActionTrackingAdmin(admin.ModelAdmin):
    """ ## ActionTrackingAdmin
        - admin페이지에서 관리할 ActionTracking 모델 설정
    """

    list_display = [
        'user',
        'point_rule',
        'actionable_type',
        'actionable_id',
        'count',
        'point'
    ]

    list_filter = [
        'user',
        'point_rule',
        'actionable_type',
        'actionable_id',
        'count',
    ]

    search_fields = [
        'user__name',
        'point_rule__name',
    ]

    ordering = [
        '-updated_at',
    ]



@admin.register(PointRule)
class PointRuleAdmin(admin.ModelAdmin):
    """## PointRuleAdmin
        - admin페이지에서 관리할 PointRule모델을 설정
    """

    list_display = [
        'name',
        'point',
    ]
