"""accounts serializers
User 모델의 Serializers json 직렬화 관련 모듈
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """UserSeializer
     fields 등록 수정 password보이면 안됌"""
    class Meta:  # pylint: disable=R0903,C0115
        model = User
        fields = ['id','username','university','total_point','name']
