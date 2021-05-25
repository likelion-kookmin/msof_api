""" # history/apps.py

    history 앱의 기본 설정을 포함하고 있습니다.
"""
from django.apps import AppConfig


class HistoryConfig(AppConfig):
    """ # HistoryConfig """

    name = "msof_api.history"

    # pylint: disable=W0611, C0415
    def ready(self):
        from . import signals
