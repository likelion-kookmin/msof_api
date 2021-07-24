"""
    # action_trackings models

    - Action : 사전에 정의된 트래킹되는 액션
    - ActionTracking: 사용자 트래킹 액션
    - PointRule: 액션에 따라 정해진 포인트(점수) 규칙
"""
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from msof_api import action_trackings
from msof_api.base_model import BaseModel


class Action(models.TextChoices):
    """행동을 정의해놓은 클래스"""

    SIGNUP = "회원가입", _("signup")

    ADD_QUESTION = "질문 등록", _("register_question")
    LIKED_QUESTION = "좋아요 받은 질문", _("liked_question")
    CANCEL_LIKED_QUESTION = "질문에 대한 좋아요 취소", _("cancle_liked_question")

    SHOW_QUESTION = "질문 조회", _("show_question")

    LIKED_COMMENT = "좋아요 받은 댓글", _("liked_comment")
    SELECT_COMMENT = "댓글 채택", _("select_comment")
    SELECTED_COMMENT = "채택받은 댓글", _("selected_comment")
    CANCEL_LIKED_COMMENT = "댓글에 대한 좋아요 취소", _("cancle_liked_comment")


class PointRule(BaseModel):
    """행동에 따른 점수를 정하는 모델"""

    point = models.IntegerField(default=0, verbose_name="점수")
    name = models.CharField(
        max_length=20, choices=Action.choices, default=Action.ADD_QUESTION, verbose_name="행동"
    )

    def __str__(self):
        return str(self.name)


class ActionTracking(BaseModel):
    """사용자의 행동을 기록하는 모델"""
    ACTION_RELATED_HISTORY = [Action.SHOW_QUESTION]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="유저")
    point_rule = models.ForeignKey(PointRule, on_delete=models.CASCADE, verbose_name="규칙")

    actionable_type = models.ForeignKey(
        ContentType,
        verbose_name="액션 관련 모델",
        on_delete=models.CASCADE,
        null=True,
    )
    actionable_id = models.PositiveIntegerField(
        verbose_name="액션 관련 객체 id",
        null=True,
    )
    actionable = GenericForeignKey(
        'actionable_type',
        'actionable_id',
    )
    count = models.IntegerField(
        verbose_name="액션 횟수",  # 조회수에만 사용할 것
        null=False,
        blank=False,
        default=1,
    )

    def __str__(self):
        # pylint: disable=E1101
        return "{0}님이 {1} 행동을 통해 {2}점을 얻었습니다.{3}/{4}".format(
            self.user.username,
            self.point_rule.name,
            self.point_rule.point,
            self.created_at,
            self.updated_at,
        )

    @property
    def viewed_at(self):
        return self.created_at

    @classmethod
    def create_user_action_tracking(cls, user, rule_name, actionable=None):
        if not user.is_authenticated:
            return

        rule = PointRule.objects.get_or_create(name=rule_name)[0]
        if actionable:
            actionable_type = ContentType.objects.get_for_model(actionable)
            action_tracking_obj, created = cls.objects.get_or_create(
                user = user,
                point_rule = rule,
                actionable_type = actionable_type,
                actionable_id = actionable.id
            )
            if not created and rule_name in cls.ACTION_RELATED_HISTORY:
                action_tracking_obj.count += 1
                action_tracking_obj.save()
        else:
            cls.objects.create(user=user, point_rule=rule)

    @classmethod
    def create_show_question_action_tracking(cls, user, actionable):
        cls.create_user_action_tracking(user, Action.SHOW_QUESTION, actionable)

    @classmethod
    def total_viewed_count(cls, viewed_obj):
        """# total_viewed_count

        특정 객체의 전체 조회수를 리턴하는 메서드입니다.

        ## params

        viewed_obj: 전체 조회수를 조회하려는 레코드 객체
        """
        viewed_type_obj = ContentType.objects.get_for_model(viewed_obj)
        total_count = ActionTracking.objects.filter(
            actionable_type=viewed_type_obj,
            actionable_id=viewed_obj.id,
            point_rule__name=Action.SHOW_QUESTION,
        ).aggregate(Sum("count"))

        return total_count

    @classmethod
    def total_viewed_user_count(cls, viewed_obj):
        """# total_viewed_user_count

        특정 객체를 조회한 유저 수를 리턴하는 메서드입니다.

        ## params

        viewed_obj: 전체 조회수를 조회하려는 레코드 객체
        """
        viewed_type_obj = ContentType.objects.get_for_model(viewed_obj)
        total_count = ActionTracking.objects.filter(
            actionable_type=viewed_type_obj,
            actionable_id=viewed_obj.id,
            point_rule__name=Action.SHOW_QUESTION,
        ).count()

        return total_count
