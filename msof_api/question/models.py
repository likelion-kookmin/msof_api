"""Question(질문 게시글)과 Comment(답변) 모델"""
from django.db import models


# T0D0: 16 BaseModel 상속받기
class Question(models.Model):
    """질문 클래스"""
    MAX_TITLE_LENGTH = 200
    STATUS_CHOICES = (
        ('T', "Trash"),  # 삭제된 글
        ('P', "Published"),  # 등록된 글
        ('D', "Draft"),  # 임시 글
        ('A', "Admin"),  # 관리자용 글
    )
    # T0D0: 15 Question, Comment 모델 author 작업
    # author = models.ForeignKey(
    #     User,
    #     verbose_name="글쓴이",
    #     on_delete=models.SET,
    #     related_name="questions",
    #     null=True
    # ) # 글쓴이
    title = models.CharField(
        verbose_name="제목",
        max_length=MAX_TITLE_LENGTH
    )  # 제목
    content = models.TextField(
        verbose_name="내용"
    )  # 내용
    status = models.CharField(
        verbose_name="게시 상태",
        default=0,
        max_length=2,
        choices=STATUS_CHOICES
    )  # 게시 상태

    def __str__(self):
        return f"{self.title}"


# T0D0: 16 BaseModel 상속받기
class Comment(models.Model):
    """답변 클래스"""
    STATUS_CHOICES = (
        ('T', "Trash"),  # 삭제된 글
        ('P', "Published"),  # 등록된 글
        ('D', "Draft"),  # 임시 글
        ('A', "Admin"),  # 관리자용 글
    )

    # T0D0: 15 Question, Comment 모델 author 작업
    # author = models.ForeignKey(
    #     User,
    #     verbose_name="글쓴이",
    #     on_delete=models.SET_NULL,
    #     related_name="answered_comments",
    #     null=True
    # ) # 글쓴이
    question = models.ForeignKey(
        Question,
        verbose_name="질문",
        on_delete=models.SET_NULL,
        related_name='comments',
        null=True,
    )  # 질문
    parent = models.ForeignKey(
        'self',
        verbose_name="상위 덧글",
        on_delete=models.SET_NULL,
        related_name='replied_comments',
        null=True,
        blank=True,
    )  # 덧글
    selected = models.BooleanField(
        verbose_name="채택 여부",
        default=False
    )  # 채택 여부
    content = models.TextField(
        verbose_name="내용"
    )  # 내용
    status = models.CharField(
        verbose_name="게시 상태",
        default=0,
        max_length=2,
        choices=STATUS_CHOICES
    )  # 게시 상태

    def __str__(self):
        # 답글인 경우
        if self.parent:
            # if self.author:
            #     return f"{self.author}님이 {self.parent}에 덧붙인 글"
            return f"{self.parent}에 덧붙인 글"
        # 일반글인 경우
        # if self.author:
        #     return f"{self.author}님이 {self.question}에 답변한 글"
        return f"{self.question}에 답변한 글"

    def select(self):
        """채택: self.selected를 true로 설정"""
        self.selected = True
        self.save()