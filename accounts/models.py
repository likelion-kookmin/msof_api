"""
model account
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class Univerisity(models.Model):
    """
    대학모델
    """
    name = models.CharField(max_length=100)


class User(AbstractUser):
    """
    유저모델
    """
    name = models.CharField(max_length=100)
    univerisity = models.ForeignKey(Univerisity, on_delete=models.CASCADE, null=True, blank=True)
    total_point = models.PositiveIntegerField(default=0)
