"""# question serializers"""
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from msof_api.comments.models import Comment
from msof_api.comments.serializers import CommentSerializer

from .models import Question


class QuestionSerializer(ModelSerializer):
    """## QuestionSerializer
        - Question Model serializer입니다.
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
        """### get_comments
            - 현재 글에 달린 상위(parent가 없는) 답변이 담겨 내려가도록 합니다.
        """
        comments = Comment.objects.filter(question=obj, parent=None)
        comment_serializers = CommentSerializer(comments, many=True)
        return comment_serializers.data
