""" # history/models.py

History Model을 포함하고 있습니다.
"""

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Sum

from accounts.models import User
from msof_api.base_model import BaseModel


class History(BaseModel):
    """# History Model

    사용자 조회 기록과 조회수를 저장하기 위한 모델입니다.

    contenttype을 활용하여 구성되었습니다.
    """

    viewer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        verbose_name="사용자",
    )

    viewed_type = models.ForeignKey(
        ContentType,
        verbose_name="조회한 모델",
        on_delete=models.CASCADE,
        null=True,
    )
    viewed_id = models.PositiveIntegerField(
        verbose_name="조회한 ID",
        null=True,
    )
    viewed_object = GenericForeignKey(
        "viewed_type",
        "viewed_id",
    )
    viewed_count = models.IntegerField(
        verbose_name="조회수",
        null=False,
        blank=False,
        default=1,
    )

    @property
    def viewed_at(self):
        """# viewed_at

        created_at의 alias 입니다.
        """
        return self.created_at

    @classmethod
    def add_history(cls, viewed_obj, viewer):
        """# add_history

        특정 객체에 조회한 기록을 추가하는 메소드입니다.

        ## params

        viewed_obj: 조회 기록을 추가하려는 레코드 객체
        viwer: 조회한 유저 레코드 객체
        """
        viewed_type = ContentType.objects.get_for_model(viewed_obj)

        history_obj, created = History.objects.get_or_create(
            viewer=viewer, viewed_type=viewed_type, viewed_id=viewed_obj.id
        )
        if not created:
            history_obj.viewed_count += 1
        history_obj.save()

    @classmethod
    def total_viewed_count(cls, viewed_obj):
        """# total_viewed_count

        특정 객체의 전체 조회수를 리턴하는 메서드입니다.

        ## params

        viewed_obj: 전체 조회수를 조회하려는 레코드 객체
        """
        viewed_type_obj = ContentType.objects.get_for_model(viewed_obj)
        total_count = History.objects.filter(
            viewed_type=viewed_type_obj,
            viewed_id=viewed_obj.id,
        ).aggregate(Sum("viewed_count"))

        return total_count

    @classmethod
    def total_viewed_user_count(cls, viewed_obj):
        """# total_viewed_user_count

        특정 객체를 조회한 유저 수를 리턴하는 메서드입니다.

        ## params

        viewed_obj: 전체 조회수를 조회하려는 레코드 객체
        """
        viewed_type_obj = ContentType.objects.get_for_model(viewed_obj)
        total_count = History.objects.filter(
            viewed_type=viewed_type_obj,
            viewed_id=viewed_obj.id,
        ).count()

        return total_count
