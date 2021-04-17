""" Question Serializers
Question 모델의 Serializers json 직렬화 모듈
"""

from rest_framework import serializers

from .models import Question


class QuestionListSerializer(serializers.ModelSerializer):
    """QuestionListSerializer"""

    class Meta:  # pylint: disable=missing-docstring
        model = Question
        fields = [
            'id',
            'title',
            'content',
            'created_at',
            'updated_at'
        ]

class QuestionCreateSerializer(serializers.ModelSerializer):
    """QuestionCreateSerializer"""

    class Meta:  # pylint: disable=missing-docstring
        model = Question
        fields = [
            'title',
            'content',
            'created_at',
            'updated_at'
        ]


class QuestionRetrieveSerializer(serializers.ModelSerializer):
    """QuestionRetrieveSerializer"""
    class Meta:  # pylint: disable=missing-docstring
        model = Question
        fields = [
            'title',
            'content',
            'created_at',
            'updated_at'
        ]

class QuestionUpdateSerializer(serializers.ModelSerializer):
    """QuestionUpdateSerializer"""
    class Meta:  # pylint: disable=missing-docstring
        model = Question
        fields = [
            'title',
            'content',
            'created_at',
            'updated_at'
        ]


class QuestionDestroySerializer(serializers.ModelSerializer):
    """QuestionDestroySerializer"""
    class Meta:  # pylint: disable=missing-docstring
        model = Question
        fields = [
            'title',
            'content',
            'created_at',
            'updated_at'
        ]
