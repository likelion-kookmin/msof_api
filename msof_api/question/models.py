"""
Question(질문 게시글)과 Comment(답변) 모델 정의
"""
# from msof_api.users.models import User
from django.db import models

MAX_TITLE_LENGTH = 200

class Question(models.Model):
    '''
    질문 게시글 클래스
    '''
    # author = models.ForeignKey(User, on_delete=models.SET_NULL,
    #           related_name='questions', null=True)
    title = models.CharField(max_length=MAX_TITLE_LENGTH)  # 혹시 몰라 전역으로 빼둠
    content = models.TextField()
    status = models.IntegerField(default=0)

    def __str__(self):
        return str(self.title)

    def count_up(self):
        '''self.status 값을 1 증가'''
        self.status += 1
        self.save()

    def count_down(self):
        '''self.status 1 감소'''
        self.status -= 1
        self.save()


class Comment(models.Model):
    '''
    답변 클래스
    '''
    # 구조에 없었는데 필요해 보여서 일단 넣음
    # author = models.ForeignKey(User, on_delete=models.SET_NULL)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL,
                                 related_name='comments', null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL,
                               related_name='re_comments', null=True)
    selected = models.BooleanField(default=False)
    content = models.TextField()
    status = models.IntegerField(default=0)

    def __str__(self):
        # 답글인 경우
        if self.parent:
            # return f"{self.author}님이 {self.parent}에 덧붙인 글"
            return f"{self.parent}에 덧붙인 글"
        # 일반글인 경우
        # return f"{self.author}님이 {self.question}에 답변한 글"
        return f"{self.question}에 답변한 글"

    def select(self):
        '''채택: self.selected를 true로 설정'''
        self.selected = True
        self.save()

    def reject(self):
        '''취소: self.selected를 false로 설정'''
        self.selected = False
        self.save()

    def count_up(self):
        '''self.status 값 증가(status +1)'''
        self.status += 1
        self.save()

    def count_down(self):
        '''self.status 값 감소(status -1)'''
        self.status -= 1
        self.save()
