"""account appconfig 모듈"""
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """appconfig class
    name을 통해 setting에 등록 가능
    """
    name = 'accounts'
