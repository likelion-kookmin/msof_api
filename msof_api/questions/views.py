"""questions views"""

from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from msof_api.action_trackings.models import ActionTracking

from .models import Question
from .permissions import QuestionEditableOrDestroyablePermission
from .serializers import QuestionSerializer


class QuestionListView(ListAPIView):
    """## QuestionListView
        - Questions#index
        - 모든 질문이 반환됩니다.
    """
    queryset = Question.objects.published()
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class QuestionDetailView(RetrieveAPIView):
    """## QuestionDetailView
        - Questions#show
        - 특정 질문을 반환합니다.
    """
    queryset = Question.objects.published()
    serializer_class = QuestionSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    def get(self, request, *args, **kwargs):
        ActionTracking.create_show_question_action_tracking(
            user=request.user,
            actionable=Question.objects.published().filter(pk=kwargs['pk']).first()
        )
        return self.retrieve(request, *args, **kwargs)


class QuestionCreateView(CreateAPIView):
    """## QuestionCreateView
        - Questions#new
        - 질문을 생성합니다.
    """
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class QuestionUpdateView(UpdateAPIView):
    """## QuestionUpdateView
        - Questions#edit
        - 특정 질문을 수정합니다.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, QuestionEditableOrDestroyablePermission]
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class QuestionDestroyView(DestroyAPIView):
    """## QuestionDestroyView
        - Questions#destroy
        - 특정 질문을 삭제합니다.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, QuestionEditableOrDestroyablePermission]
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
