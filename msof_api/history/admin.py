""" # history/admin.py

    history 앱의 어드민 사이트 관련 구현 사항을 포함하고 있습니다.
"""
from django.contrib import admin

from .models import History


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    """ History 어드민 설정 클래스입니다. """
    list_display = [
        "viewed_type",
        "viewed_id",
        "viewed_object",
        "viewer",
        "viewed_count",
        "created_at",
        "updated_at"
    ]
    list_filter = [
        "viewed_type",
        "viewed_id",
        "viewer",
        "viewed_count"
    ]
