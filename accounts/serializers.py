"""
account serializers
"""

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

"""
User serailizer입니다. password가 보이니까 field 관련 부분 수정해야됩니당
"""
class UserSerializer(serializers.ModelSerializer):
    """
    meta class
    """
    class Meta:  # pylint: disable=R0903,C0115
        model = User
        fields = '__all__'
