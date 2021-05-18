"""activity App"""
from django.apps import AppConfig


class ActivityConfig(AppConfig):
    """activity 기본 설정 클래스"""

    name = "msof_api.activity"

    # pylint: disable=W0611, C0415
    def ready(self):
        import msof_api.activity.signals
