"""perform 클래스 관련 파일입니다."""
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from accounts.models import User
from msof_api.base_model import BaseModel


class PerformCategoryChoice(models.IntegerChoices):
    """perform 클래스의 category 컬럼의 value 종류를 정의하는 enum 클래스입니다."""
    NONE = 0, 'none'
    LIKE = 1, 'like'
    DISLIKE = 2, 'dislike'

class Perform(BaseModel):
    """사용자가 행한 perform을 기록하는 모델 클래스입니다."""
    CATEGORY_CHOICES = (
        ('like', '좋아요'),
        ('dislike', '싫어요'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    performed_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        null=True,
    )
    performed_id = models.PositiveIntegerField(
        null=True,
    )
    performed_object = GenericForeignKey(
        'performed_type',
        'performed_id',
    )
    category = models.IntegerField(
        verbose_name="종류",
        default=PerformCategoryChoice.NONE,
        choices=PerformCategoryChoice.choices
    )
