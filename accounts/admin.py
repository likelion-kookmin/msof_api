"""
accounts admin
"""
from django.contrib import admin

from .models import Univerisity, User

# Register your models here.
admin.site.register(User)
admin.site.register(Univerisity)
