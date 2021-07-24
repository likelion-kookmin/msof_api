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
        read_only_fields = [
            'author',
            'viewed_count',
            'liked_count',
            'disliked_count',
            'created_at',
            'updated_at',
            'deleted_at',
        ]
