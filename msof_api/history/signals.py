# """history signal module"""
# from django.db.models.signals import pre_save
# from django.dispatch import receiver

# from msof_api.history.models import History
# from msof_api.question.models import Question


# pylint: disable=W0613
# @receiver(pre_save, sender=History)
# def reset_question_viewed_count(sender, **kwargs):
#     """질문의 viewed_count를 재설정합니다."""
#     instance = kwargs["instance"]
#     viewed_model = instance.viewed_type.model_class()
#     viewed_id = instance.viewed_id

#     if viewed_model != Question:
#         return

#     question = viewed_model.get_object_for_this_type(pk=viewed_id)
#     history = History.objects.filter(id=instance.id).first()

#     if not history:
#         question.viewed_count += instance.viewed_count

#     else:
#         delta = instance.viewed_count - history.viewed_count
#         question.viewed_count += delta

#     question.save()
