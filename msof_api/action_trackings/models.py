"""
    # action_trackings models

    - Action : 사전에 정의된 트래킹되는 액션
    - ActionTracking: 사용자 트래킹 액션
    - PointRule: 액션에 따라 정해진 포인트(점수) 규칙
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from msof_api.base_model import BaseModel


class Action(models.TextChoices):
    """행동을 정의해놓은 클래스"""

    ADD_QUESTION = "질문 등록", _("register_question")
    SELECT_COMMENT = "댓글 채택", _("select_comment")
    SELECTED_COMMENT = "채택받은 댓글", _("selected_comment")
    SIGNUP = "회원가입", _("signup")
    LIKED_COMMENT = "좋아요받은 댓글", _("liked_comment")
    LIKED_QUESTION = "좋아요받은 질문", _("liked_question")
    CANCEL_LIKED_COMMENT = "댓글에 대한 좋아요 취소", _("cancle_liked_comment")
    CANCEL_LIKED_QUESTION = "질문에 대한 좋아요 취소", _("cancle_liked_question")


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

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="유저")
    point_rule = models.ForeignKey(PointRule, on_delete=models.CASCADE, verbose_name="규칙")


    def __str__(self):
        return "{0}님이 {1} 행동을 통해 {2}점을 얻었습니다.{3}/{4}".format(
            self.user.username,
            self.point_rule.name,
            self.point_rule.point,
            self.created_at,
            self.updated_at,
        )
