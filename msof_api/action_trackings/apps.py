"""action_trackings App"""
from django.apps import AppConfig


class ActionTrackingConfig(AppConfig):
    """action_trackings 기본 설정 클래스"""

    name = "msof_api.action_trackings"

    # pylint: disable=W0611, C0415
    def ready(self):
        import msof_api.action_trackings.signals
