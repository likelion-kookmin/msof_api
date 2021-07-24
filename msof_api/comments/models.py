from django.db import models

from accounts.models import User
from msof_api.base_model import BaseModel, BaseModelManager
from msof_api.questions.models import Question


class Comment(BaseModel):
    """답변 클래스"""

    STATUS_CHOICES = (
        ('T', 'Trash'),  # 삭제된 글
        ('P', 'Published'),  # 등록된 글
        ('D', 'Draft'),  # 임시 글
        ('A', 'Admin'),  # 관리자용 글
    )

    author = models.ForeignKey(
        User,
        verbose_name="글쓴이",
        on_delete=models.SET_NULL,
        related_name="answered_comments",
        null=True,
    )  # 글쓴이
    question = models.ForeignKey(
        Question,
        verbose_name="질문",
        on_delete=models.SET_NULL,
        related_name="comments",
        null=True,
    )  # 질문
    parent = models.ForeignKey(
        "self",
        verbose_name="상위 덧글",
        on_delete=models.SET_NULL,
        related_name="replied_comments",
        null=True,
        blank=True,
    )  # 덧글
    selected = models.BooleanField(verbose_name="채택 여부", default=False)  # 채택 여부
    content = models.TextField(verbose_name="내용")  # 내용
    status = models.CharField(
        verbose_name="게시 상태", default='P', max_length=2, choices=STATUS_CHOICES
    )  # 게시 상태
    liked_count = models.PositiveIntegerField(
        verbose_name="좋아요 수", default=0, null=False, blank=True
    )  # 좋아요 수
    disliked_count = models.PositiveIntegerField(
        verbose_name="싫어요 수", default=0, null=False, blank=True
    )  # 싫어요 수

    def __str__(self):
        # 답글인 경우
        if self.parent:
            if self.author:
                return f"{self.author}님이 {self.parent}에 덧붙인 글"
            return f"{self.parent}에 덧붙인 글"
        if self.author:
            return f"{self.author}님이 {self.question}에 답변한 글"
        return f"{self.question}에 답변한 글"

    def select(self):
        """채택: self.selected를 true로 설정"""
        self.selected = True
        self.save()
