"""# comment serializers"""
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Comment


class CommentSerializer(ModelSerializer):
    """## CommentSerializer
        - Comment model serializer입니다.
    """
    re_comments = serializers.SerializerMethodField()

    class Meta:
        """### CommentSerializer.Meta"""
        model = Comment
        fields = '__all__'
        read_only_fields = [
            'author',
            'liked_count',
            'disliked_count',
            'created_at',
            'updated_at',
            'deleted_at',
        ]

    def get_re_comments(self, obj):
        """### get_re_comments
            - 대댓글 데이터가 담겨 내려가도록 하였습니다.
        """
        comments = Comment.objects.filter(parent=obj)
        comment_serializers = CommentSerializer(comments, many=True)
        return comment_serializers.data

# TODO: selected는 author만 수정 가능하도록 하기
