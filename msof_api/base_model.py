import datetime

from django.db import models


class BaseModelManager(models.Manager):
    # NOTE: 해당 옵션은 기본 매니저로 이 매니저를 정의한 모델이 있을 때 이 모델을 가리키는 모든 관계 참조에서 모델 매니저를 사용할 수 있도록 한다.
    # 참고링크: https://velog.io/@kim6515516/장고에서-모델-소프트-삭제-구현하기
    use_for_related_fields = True

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class BaseModel(models.Model):
    objects = BaseModelManager()

    created_at = models.DateTimeField(
        verbose_name='추가된 일시',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='수정된 일시',
        auto_now=True
    )
    deleted_at = models.DateTimeField(
        verbose_name='삭제된 일시',
        blank=True,
        null=True,
        default=None
    )

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = datetime.datetime.now()
        self.save(update_fields=['deleted_at'])

    def restore(self):
        self.deleted_at = None
        self.save(update_fields=['deleted_at'])
