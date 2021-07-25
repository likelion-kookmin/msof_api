"""# questions models
    - Question
"""
from django.db import models

from accounts.models import User
from msof_api.base_model import BaseModel, BaseModelManager


class QuestionQuerySet(models.QuerySet):
    """# QuestionQuerySet
        - Quesion 모델의 커스텀 쿼리셋
        - Use like `Quesition.objects.published()`
    """

    def published(self):
        """## published
            - 등록된 질문만 리턴합니다.
        """
        return self.filter(status='P')

    def admin(self):
        """## admin
            - 관리자용 질문만 리턴합니다.
        """
        return self.filter(status='A')

    def recent_updated(self):
        """## recent_updated
            - 최근 수정된 질문부터 리턴합니다.
        """
        return self.order_by("-updated_at")

    def recent_created(self):
        """## recnet_creaeted
            - 최근 생성된 질문부터 리턴합니다.
        """
        return self.order_by("-created_at")


class Question(BaseModel):
    """## Question
        - 질문 클래스
    """

    objects = BaseModelManager.from_queryset(QuestionQuerySet)()

    MAX_TITLE_LENGTH = 200
    STATUS_CHOICES = (
        ('T', 'Trash'),  # 삭제된 글
        ('P', 'Published'),  # 등록된 글
        ('D', 'Draft'),  # 임시 글
        ('A', 'Admin'),  # 관리자용 글
    )
    author = models.ForeignKey(
        User,
        verbose_name="글쓴이",
        on_delete=models.SET,
        related_name="questions",
        null=True
    )  # 글쓴이
    title = models.CharField(
        verbose_name="제목",
        max_length=MAX_TITLE_LENGTH
    )  # 제목
    content = models.TextField(
        verbose_name="내용"
    )  # 내용
    status = models.CharField(
        verbose_name="게시 상태", default="P", max_length=2, choices=STATUS_CHOICES
    )  # 게시 상태
    viewed_count = models.PositiveIntegerField(
        verbose_name="조회 수", default=0, null=False, blank=True
    )  # 조회 수
    liked_count = models.PositiveIntegerField(
        verbose_name="좋아요 수", default=0, null=False, blank=True
    )  # 좋아요 수
    disliked_count = models.PositiveIntegerField(
        verbose_name="싫어요 수", default=0, null=False, blank=True
    )  # 싫어요 수

    def __str__(self):
        return f"{self.title}"
