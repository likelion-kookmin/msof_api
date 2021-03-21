from django.db import models
# from msof_api.base_model import BaseModel
from msof_api.users.models import User

class Activity(models.Model):
    
    ACTION_CHOICE = (
        ('질문 등록', 'Add_Question'),
        ('댓글 작성', 'Add_Comment'),
        ('댓글 채택', 'Select_Comment'),
        ('채택받은 댓글', 'Selected_Commend'),
        ('회원가입', 'SignUp'),
        ('좋아요받은 질문', 'Liked_Question'),
        ('error', 'error')
    )

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    point = models.IntegerField(default=0)
    activity = models.CharField(max_length = 20, choices=ACTION_CHOICE, default='error')

    # TODO: str에 created를 추가해줘야함. 
    def __str__(self) :
        return "{0}님이 {1} 행동을 통해 {2}점을 얻었습니다.".format(self.user.username, self.activity, self.point)

    def save(self, *args, **kwargs):
        if self.activity == "질문 등록" :
            self.point = 5
        elif self.activity == "댓글 작성" :
            self.point = 1
        elif self.activity == "댓글 채택" :
            self.point = 1
        elif self.activity == "채택받은 댓글" :
            self.point = 5
        elif self.activity == "회원가입" :
            self.point = 10
        elif self.activity == "좋아요받은 질문" :
            self.point = 0.5
        elif self.activity == "error" :
            self.point = 0
        return super().save(*args, **kwargs)
    # 