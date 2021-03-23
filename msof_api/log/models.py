from django.db import models
# from msof_api.base_model import BaseModel
from msof_api.users.models import User
from django.utils.translation import gettext_lazy as _

class PointRule(models.Model):

    class Action(models.TextChoices):
        ADD_QUESTION = 'AQ', _('Add_qeustion')
        ADD_COMMENT = 'AC', _('Add_comment')
        SELECT_COMMENT = 'SC', _('Select_comment')
        SELECTED_COMMENT = 'SDC', _('Selected_comment')
        SIGNUP = 'SU', _('SignUp')
        LIKED_QUESTION = 'LQ', _('Liked_question')

    point = models.IntegerField(default=0)
    name = models.CharField(
        max_length = 3,
        choices=Action.choices,
        default=Action.ADD_QUESTION )

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    point_rule = models.ForeignKey(PointRule, on_delete = models.CASCADE)

    # TODO: str에 created를 추가해줘야함. 
    def __str__(self):
        return "{0}님이 {1} 행동을 통해 {2}점을 얻었습니다.".format(self.user.username, self.point_rule.name, self.point_rule.point)
        