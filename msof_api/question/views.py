"""Quesion app ViewSet
request에 따른 response를 처리하기 위한 모듈
"""

from rest_framework import viewsets

from .models import Question
from .serializers import (QuestionCreateSerializer, QuestionDestroySerializer,
                          QuestionListSerializer, QuestionRetrieveSerializer,
                          QuestionUpdateSerializer)


class QuestionViewSet(viewsets.ModelViewSet):  # pylint: disable=R0901&R0903
    """QuestionViewSet
    Question 모델에 대한 기본적인 GET, POST, PUT, DELETE 메소드 지원
    """
    serializer_class = QuestionListSerializer
    queryset = Question.objects.published().recent_updated()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serializer_action_class = {
            'list': QuestionListSerializer,
            'create': QuestionCreateSerializer,
            'retrieve': QuestionRetrieveSerializer,
            'update': QuestionUpdateSerializer,
            'destroy': QuestionDestroySerializer,
        }
