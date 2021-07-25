"""# action_trackings apps"""
from django.apps import AppConfig


class ActionTrackingConfig(AppConfig):
    """## action_trackings 기본 설정 클래스"""

    name = "msof_api.action_trackings"

    def ready(self):
        import msof_api.action_trackings.signals
