from django.contrib import admin
from .models import Activity, PointRule

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    pass

@admin.register(PointRule)
class PointRuleAdmin(admin.ModelAdmin):
    pass