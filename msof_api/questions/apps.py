"""questions apps"""
from django.apps import AppConfig


class QuestionsConfig(AppConfig):
    """## questions 기본 설정 클래스"""
    name = "msof_api.questions"

    def ready(self):
        import msof_api.questions.signals
