"""
    # Comment Serializers
"""
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Comment


class CommentSerializer(ModelSerializer):
    """
        ## CommentSerializer

        기본적으로 모든 정보를 보여주는 Serializer입니다.
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
        comments = Comment.objects.filter(parent=obj)
        serializers = CommentSerializer(comments, many=True)
        return serializers.data

# TODO: selected는 author만 수정 가능하도록 하기
