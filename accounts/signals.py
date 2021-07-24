"""
    # accounts signal module
"""
from django.db.models.signals import post_save
from django.dispatch import receiver

from msof_api.action_trackings.models import Action, ActionTracking, PointRule


@receiver(post_save, sender=ActionTracking)
def add_total_point(sender, **kwargs):
    action_tracking = kwargs['instance']
    user = action_tracking.user
    user.total_point += action_tracking.point_rule.point
    user.save()
