"""account appconfig 모듈"""
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """accounts 기본 설정 클래스"""
    name = 'accounts'

    def ready(self):
        import accounts.signals
