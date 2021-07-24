"""
    # Quesion Views

    request에 따른 response를 처리하기 위한 모듈
"""

from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Question
from .permissions import QuestionEditableOrDestroyablePermission
from .serializers import QuestionSerializer, QuestionWriteSerializer


class QuestionListView(ListAPIView):
    """
        ## QuestionListView
    """
    queryset = Question.objects.published()
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class QuestionDetailView(RetrieveAPIView):
    """
        ## QuestionDetailView
    """
    queryset = Question.objects.published()
    serializer_class = QuestionSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class QuestionCreateView(CreateAPIView):
    """
        ## QuestionCreateView
    """
    queryset = Question.objects.published()
    serializer_class = QuestionWriteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class QuestionUpdateView(UpdateAPIView):
    """
        ## QuestionUpdateView
    """
    queryset = Question.objects.all()
    serializer_class = QuestionWriteSerializer
    permission_classes = [IsAuthenticated, QuestionEditableOrDestroyablePermission]
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class QuestionDestroyView(DestroyAPIView):
    """
        ## QuestionDestroyView
    """
    queryset = Question.objects.all()
    serializer_class = QuestionWriteSerializer
    permission_classes = [IsAuthenticated, QuestionEditableOrDestroyablePermission]
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
