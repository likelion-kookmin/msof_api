from django.db.models.signals import pre_save
from django.dispatch import receiver

from msof_api.action_trackings.models import ActionTracking
from msof_api.questions.models import Question


@receiver(pre_save, sender=ActionTracking)
def reset_question_viewed_count(sender, **kwargs):
    """질문의 viewed_count를 재설정합니다."""
    instance = kwargs["instance"]  # class: ActionTracking
    prev_instance = ActionTracking.objects.filter(pk=instance.id).first()

    viewed_model = instance.actionable_type.model_class()
    viewed_id = instance.actionable_id

    if viewed_model != Question:
        return

    question = viewed_model.objects.get(pk=viewed_id)

    if not prev_instance:
        question.viewed_count += instance.count

    else:
        delta = instance.count - prev_instance.count
        question.viewed_count += delta

    question.save()
