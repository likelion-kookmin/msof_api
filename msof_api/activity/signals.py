"""activity signal module"""
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from msof_api.activity.models import Activity, PointRule
from msof_api.perform.models import Perform
from msof_api.question.models import Comment, Question

User = get_user_model()

# pylint: disable=W0613
@receiver(pre_save, sender=Question)
def create_question_activity(sender, **kwargs):
    """add_question 했을 때 activity를 생성합니다."""
    instance = kwargs["instance"]

    user = instance.author
    rule = PointRule.objects.get(name="질문 등록")

    if instance.id is not None:
        return

    activity = Activity.objects.create(user=user, point_rule=rule)
    user.total_point += activity.point_rule.point
    user.save()


@receiver(post_save, sender=User)
def create_user_activity(sender, **kwargs):
    """signup 했을 때 activity를 생성합니다."""
    user = kwargs["instance"]
    rule = PointRule.objects.get(name="회원가입")

    if not kwargs["created"]:
        return

    Activity.objects.create(user=user, point_rule=rule)
    user.total_point += 10
    user.save(update_fields=["total_point"])


@receiver(pre_save, sender=Comment)
def selected_comment_activity(sender, **kwargs):
    """Comment 관련 Activity
    comment 가 selected 되었을 때 acitivity를 생성합니다.
    comment 를 select 했을 때 acitivity를 생성합니다.
    """
    instance = kwargs["instance"]
    comment_user = instance.author
    comment_rule = PointRule.objects.get(name="채택받은 댓글")
    question_user = instance.question.author
    question_rule = PointRule.objects.get(name="댓글 채택")

    if instance.selected and not Comment.objects.get(id=instance.id).selected:
        comment_activity = Activity.objects.create(user=comment_user, point_rule=comment_rule)
        comment_user.total_point += comment_activity.point_rule.point
        comment_user.save()

        question_activity = Activity.objects.create(user=question_user, point_rule=question_rule)
        question_user.total_point += question_activity.point_rule.point
        question_user.save()

    else:
        return


@receiver(pre_save, sender=Perform)
def create_like_activity(sender, **kwargs):
    """like 관련 Activity
    question가 like되었을 때 activity를 생성합니다.
    comment가 like되었을 때 activity를 생성합니다.
    """
    instance = kwargs["instance"]
    # user = instance.user
    # comment_rule = PointRule.objects.get(name="좋아요받은 댓글")
    # question_rule = PointRule.objects.get(name="좋아요받은 질문")

    performed_type = instance.performed_type
    # performed_id = instance.performed_id
    category = instance.category

    if instance.id is None:
        return

    prev_instacne = Perform.objects.get(id=instance.id)
    prev_category = prev_instacne.category if prev_instacne else "None"

    print(category, prev_category)
    if category == 1 and prev_category != 1:
        if performed_type == ContentType.objects.get_for_model(Comment):
            print("comment")
            # activity = Activity.objects.create(user=user, point_rule=question_rule)

        if performed_type == ContentType.objects.get_for_model(Question):
            print("question")
            # activity = Activity.objects.create(user=user, point_rule=comment_rule)

    else:
        return
