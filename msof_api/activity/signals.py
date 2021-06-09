"""activity signal module"""
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from msof_api.activity.models import Action, Activity, PointRule
from msof_api.perform.models import Perform, PerformCategoryChoice
from msof_api.question.models import Comment, Question

User = get_user_model()

# pylint: disable=W0613
@receiver(pre_save, sender=Question)
def create_question_activity(sender, **kwargs):
    """add_question 했을 때 activity를 생성합니다."""
    instance = kwargs["instance"]

    user = instance.author

    if instance.id is not None:
        return

    create_like_activity_and_reset_user_total_point(user=user, rule_name=Action.ADD_QUESTION)


@receiver(post_save, sender=User)
def create_user_activity(sender, **kwargs):
    """signup 했을 때 activity를 생성합니다."""
    user = kwargs["instance"]

    if not kwargs["created"]:
        return

    create_like_activity_and_reset_user_total_point(user=user, rule_name=Action.SIGNUP)


@receiver(pre_save, sender=Comment)
def selected_comment_activity(sender, **kwargs):
    """Comment 관련 Activity
    comment 가 selected 되었을 때 acitivity를 생성합니다.
    comment 를 select 했을 때 acitivity를 생성합니다.
    """
    instance = kwargs["instance"]
    comment_user = instance.author
    question_user = instance.question.author

    if instance.selected and not Comment.objects.get(id=instance.id).selected:
        create_like_activity_and_reset_user_total_point(
            user=comment_user, rule_name=Action.SELECTED_COMMENT
        )
        create_like_activity_and_reset_user_total_point(
            user=question_user, rule_name=Action.SELECT_COMMENT
        )

    else:
        return


# pylint: disable=W0702
@receiver(pre_save, sender=Perform)
def create_like_activity_and_reset_liked_count(sender, **kwargs):
    """like 관련 Activity
    question가 like되었을 때 activity를 생성합니다.
    comment가 like되었을 때 activity를 생성합니다.
    liked_count 수를 갱신합니다.
    """
    comment_type = ContentType.objects.get_for_model(Comment)
    question_type = ContentType.objects.get_for_model(Question)

    instance = kwargs["instance"]
    category = instance.category

    prev_instacne = Perform.objects.filter(id=instance.id).first()
    prev_category = prev_instacne.category if prev_instacne else "None"

    performed_type = instance.performed_type
    performed_id = instance.performed_id
    user = performed_type.get_object_for_this_type(id=performed_id).author

    # 좋아요를 눌렀을 때
    if category == PerformCategoryChoice.LIKE and prev_category != PerformCategoryChoice.LIKE:
        try:
            if performed_type == comment_type:
                create_like_activity_and_reset_user_total_point(
                    user=user, rule_name=Action.LIKED_COMMENT
                )
                comment_object = performed_type.get_object_for_this_type(pk=performed_id)
                comment_object.liked_count += 1
                comment_object.save()

            if performed_type == question_type:
                create_like_activity_and_reset_user_total_point(
                    user=user, rule_name=Action.LIKED_QUESTION
                )
                question_object = performed_type.get_object_for_this_type(pk=performed_id)
                question_object.liked_count += 1
                question_object.save()

        except Exception as e:
            print(e)
            return

    # 좋아요를 취소했을 때
    elif category != PerformCategoryChoice.LIKE and prev_category == PerformCategoryChoice.LIKE:
        try:
            if performed_type == comment_type:
                create_like_activity_and_reset_user_total_point(
                    user=user, rule_name=Action.CANCEL_LIKED_COMMENT
                )
                comment_object = performed_type.get_object_for_this_type(pk=performed_id)
                comment_object.liked_count -= 1
                comment_object.save()

            if performed_type == question_type:
                create_like_activity_and_reset_user_total_point(
                    user=user, rule_name=Action.CANCEL_LIKED_QUESTION
                )
                question_object = performed_type.get_object_for_this_type(pk=performed_id)
                question_object.liked_count -= 1
                question_object.save()

        except Exception as e:
            print(e)
            return


@receiver(pre_save, sender=Perform)
def reset_disliked_count(sender, **kwargs):
    """disliked_count 수를 갱신합니다."""
    comment_type = ContentType.objects.get_for_model(Comment)
    question_type = ContentType.objects.get_for_model(Question)

    instance = kwargs["instance"]
    category = instance.category

    prev_instacne = Perform.objects.filter(id=instance.id).first()
    prev_category = prev_instacne.category if prev_instacne else "None"

    performed_type = instance.performed_type
    performed_id = instance.performed_id

    # 싫어요를 눌렀을 때
    if category == PerformCategoryChoice.DISLIKE and prev_category != PerformCategoryChoice.DISLIKE:
        try:
            if performed_type == comment_type:
                comment_object = performed_type.get_object_for_this_type(pk=performed_id)
                comment_object.disliked_count += 1
                comment_object.save()

            if performed_type == question_type:
                question_object = performed_type.get_object_for_this_type(pk=performed_id)
                question_object.disliked_count += 1
                question_object.save()

        except Exception as e:
            print(e)
            return

    # 싫어요를 취소했을 때
    elif (
            category != PerformCategoryChoice.DISLIKE and
            prev_category == PerformCategoryChoice.DISLIKE
        ):
        try:
            if performed_type == comment_type:
                comment_object = performed_type.get_object_for_this_type(pk=performed_id)
                comment_object.disliked_count -= 1
                comment_object.save()

            if performed_type == question_type:
                question_object = performed_type.get_object_for_this_type(pk=performed_id)
                question_object.disliked_count -= 1
                question_object.save()

        except Exception as e:
            print(e)
            return


def create_like_activity_and_reset_user_total_point(user, rule_name):
    """activity 생성 및 user total_point 재설정"""
    rule = PointRule.objects.get_or_create(name=rule_name)[0]
    activity = Activity.objects.create(user=user, point_rule=rule)
    user.total_point += activity.point_rule.point
    user.save()
