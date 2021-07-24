"""app 설정 파일"""
from django.apps import AppConfig


class QuestionsConfig(AppConfig):
    """Questions 앱 설정"""
    name = "msof_api.questions"

    def ready(self):
        import msof_api.questions.signals
