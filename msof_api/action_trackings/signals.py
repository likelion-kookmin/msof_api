"""
    # action trackings signal module
"""
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from msof_api.action_trackings.models import Action, ActionTracking
from msof_api.comments.models import Comment
from msof_api.perform.models import Perform, PerformCategoryChoice
from msof_api.questions.models import Question

User = get_user_model()

# pylint: disable=W0613
@receiver(post_save, sender=Question)
def create_question_action_tracking(sender, **kwargs):
    """ ## create_question_action_tracking
        - add_question action을 tracking합니다.
    """
    instance = kwargs["instance"]

    user = instance.author

    if not kwargs["created"]:
        return

    ActionTracking.create_user_action_tracking(
        user=user,
        rule_name=Action.ADD_QUESTION,
        actionable=instance
    )


@receiver(post_save, sender=User)
def create_user_action_tracking(sender, **kwargs):
    """## create_user_action_tracking
        - signup action을 tracking합니다.
    """
    user = kwargs["instance"]

    if not kwargs["created"]:
        return

    ActionTracking.create_user_action_tracking(
        user=user,
        rule_name=Action.SIGNUP
    )


@receiver(post_save, sender=Comment)
def selected_comment_action_tracking(sender, **kwargs):
    """## selected_comment_action_tracking
        - comment 가 selected 되었을 때를 트랙킹합니다.
        - comment 를 select 했을 때를 트랙킹합니다.
    """
    instance = kwargs["instance"]
    comment_user = instance.author
    question_user = instance.question.author

    if instance.selected and not Comment.objects.get(id=instance.id).selected:
        ActionTracking.create_user_action_tracking(
            user=comment_user,
            rule_name=Action.SELECTED_COMMENT,
            actionable=instance,
        )
        ActionTracking.create_user_action_tracking(
            user=question_user,
            rule_name=Action.SELECT_COMMENT,
            actionable=instance,
        )

    else:
        return


# pylint: disable=W0702
@receiver(pre_save, sender=Perform)
def create_like_action_tracking(sender, **kwargs):
    """## like 관련 action_tracking
        - question가 like되었을 때 action_tracking를 생성합니다.
        - comment가 like되었을 때 action_tracking를 생성합니다.
    """
    comment_type = ContentType.objects.get_for_model(Comment)
    question_type = ContentType.objects.get_for_model(Question)

    instance = kwargs["instance"]
    category = instance.category

    prev_instacne = Perform.objects.filter(id=instance.id).first()
    prev_category = prev_instacne.category if prev_instacne else "None"

    performed_type = instance.performed_type
    performed_id = instance.performed_id
    performed_obj = performed_type.get_object_for_this_type(id=performed_id)
    user = performed_obj.author

    if category == PerformCategoryChoice.LIKE and prev_category != PerformCategoryChoice.LIKE:
        try:
            if performed_type == comment_type:
                ActionTracking.create_user_action_tracking(
                    user=user,
                    rule_name=Action.LIKED_COMMENT,
                    actionable=performed_obj,
                )

            if performed_type == question_type:
                ActionTracking.create_user_action_tracking(
                    user=user,
                    rule_name=Action.LIKED_QUESTION,
                    actionable=performed_obj,
                )

        except Exception as e:
            print(e)
            return

    elif category != PerformCategoryChoice.LIKE and prev_category == PerformCategoryChoice.LIKE:
        try:
            if performed_type == comment_type:
                ActionTracking.create_user_action_tracking(
                    user=user,
                    rule_name=Action.CANCEL_LIKED_COMMENT,
                    actionable=performed_obj,
                )

            if performed_type == question_type:
                ActionTracking.create_user_action_tracking(
                    user=user,
                    rule_name=Action.CANCEL_LIKED_QUESTION,
                    actionable=performed_obj,
                )

        except Exception as e:
            print(e)
            return
