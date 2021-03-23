from django.db import models
# from msof_api.base_model import BaseModel
from msof_api.users.models import User

# ACTION_CHOICE = (
#         ('질문 등록', 'Add_Question'),
#         ('댓글 작성', 'Add_Comment'),
#         ('댓글 채택', 'Select_Comment'),
#         ('채택받은 댓글', 'Selected_Commend'),
#         ('회원가입', 'SignUp'),
#         ('좋아요받은 질문', 'Liked_Question'),
#         ('error', 'error')
#     )

class PointRule(models.Model):
    point = models.IntegerField()
    name = models.CharField()

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    point_rule = models.ForeignKey(PointRule, on_delete = models.CASCADE)

    # TODO: str에 created를 추가해줘야함. 
    def __str__(self):
        return "{0}님이 {1} 행동을 통해 {2}점을 얻었습니다.".format(self.user.username, self.point_rule.name, self.point_rule.point)