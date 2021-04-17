"""account 앱, User,University model 등록"""
from django.contrib import admin

from .models import Univerisity, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """아직 어떤거 customizing 해야 할지 모르겠음
    일단 만들어 놓음
    """


@admin.register(Univerisity)
class UniverisityAdmin(admin.ModelAdmin):
    """아직 어떤거 customizing 해야 할지 모르겠음
    일단 만들어 놓음
    """
