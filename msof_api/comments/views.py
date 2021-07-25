""" comments views"""

from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Comment
from .permissions import CommentEditableOrDestroyablePermission
from .serializers import CommentSerializer


class CommentListView(ListAPIView):
    """## CommentListView
        - Comments#index
        - 모든 질문에 달린 모든 답변이 반환됩니다.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        """### GET METHOD"""
        return self.list(request, *args, **kwargs)


class CommentDetailView(RetrieveAPIView):
    """## CommentDetailView
        - Comments#show
        - 특정 답변을 반환합니다.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    def get(self, request, *args, **kwargs):
        """### GET METHOD"""
        return self.retrieve(request, *args, **kwargs)


class CommentCreateView(CreateAPIView):
    """## CommentCreateView
        - Comments#new
        - 답변을 추가합니다.
    """

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    def perform_create(self, serializer):
        """### perform_create
            - 답변 생성시, 현재 유저를 author로 추가합니다.
        """
        return serializer.save(author = self.request.user)


class CommentUpdateView(UpdateAPIView):
    """## CommentUpdateView
        - Comments#edit
        - 특정 답변을 수정합니다.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, CommentEditableOrDestroyablePermission]
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    def put(self, request, *args, **kwargs):
        """### PUT METHOD"""
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """### PATCH METHOD"""
        return self.partial_update(request, *args, **kwargs)


class CommentDestroyView(DestroyAPIView):
    """## CommentDestroyView
        - Comments#destroy
        - 특정 답변을 삭제합니다.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, CommentEditableOrDestroyablePermission]
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    def delete(self, request, *args, **kwargs):
        """### DELETE METHOD"""
        return self.destroy(request, *args, **kwargs)
