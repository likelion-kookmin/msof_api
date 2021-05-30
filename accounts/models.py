""" account 앱의 데이터베이스 모델 User,Unversity"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class University(models.Model):
    """대학교 모델<br>

    나중에 다른 대학까지 퍼질 가능성을 열어두고 만든 모델
    """
    name = models.CharField(
        verbose_name="대학이름",
        max_length=20,
    )


class User(AbstractUser):
    """유저모델<br>

    1. 기존 장고 모델의 name, total_point 추가
    2. University 모델과 forienkey 연결
    """
    name = models.CharField(max_length=20, verbose_name = "이름")
    university = models.ForeignKey(
        University,
        verbose_name ="대학",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name= 'user',
    )
    total_point = models.PositiveIntegerField(
        verbose_name="총점수",
        default=0,
    )
