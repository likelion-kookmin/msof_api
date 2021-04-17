"""perfom 모델의 어드민 사이트 설정 파일입니다."""
from django.contrib import admin

from .models import Perform


@admin.register(Perform)
class PerformAdmin(admin.ModelAdmin):
    """perform의 어드민 사이트 설정이 담긴 클래스입니다."""
    pass
