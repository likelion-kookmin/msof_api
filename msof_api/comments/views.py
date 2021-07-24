from django.shortcuts import render
# Create your views here.
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from msof_api.action_trackings.models import ActionTracking

from .models import Comment
# from .permissions import QuestionEditableOrDestroyablePermission
from .serializers import CommentSerializer


class CommentListView(ListAPIView):
    """
        ## CommentListView
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class CommentCreateView(CreateAPIView):
    """
        ## CommentCreateView
    """

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    def perform_create(self, serializer):
        return serializer.save(author = self.request.user)
