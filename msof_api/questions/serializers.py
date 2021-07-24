"""
    # Question Serializers
"""
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from msof_api.comments.models import Comment
from msof_api.comments.serializers import CommentSerializer

from .models import Question


class QuestionSerializer(ModelSerializer):
    """
        ## QuestionSerializer

        기본적으로 모든 정보를 보여주는 Serializer입니다.
    """
    comments = serializers.SerializerMethodField()

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

    def get_comments(self, obj):
        comments = Comment.objects.filter(question=obj, parent=None)
        serializers = CommentSerializer(comments, many=True)
        return serializers.data
