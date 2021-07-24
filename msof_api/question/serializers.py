"""
    # Question Serializers
"""
from rest_framework.serializers import ModelSerializer

from .models import Question


class QuestionSerializer(ModelSerializer):
    """
        ## QuestionSerializer

        기본적으로 모든 정보를 보여주는 Serializer입니다.
    """
    class Meta:
        """### QuestionSerializer.Meta"""
        model = Question
        fields = '__all__'

class QuestionWriteSerializer(ModelSerializer):
    """
        ## QuestionWriteSerializer

        사용자가 입력할 수 있는 정보와 관련된 Serializer입니다.
    """
    class Meta:
        """### QuestionWriteSerializer.Meta"""
        model = Question
        fields = [
            'id',
            'title',
            'content'
        ]
