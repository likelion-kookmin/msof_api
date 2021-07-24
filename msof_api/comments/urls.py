"""Quetion App url 라우터 등록"""

from django.urls import path

from .views import CommentCreateView, CommentListView

app_name = 'comments'

urlpatterns = [
    path('', CommentListView.as_view()),
    path('new/', CommentCreateView.as_view()),
    # path('<int:pk>/', QuestionDetailView.as_view()),
    # path('<int:pk>/destroy/', QuestionDestroyView.as_view()),
    # path('<int:pk>/edit/', QuestionUpdateView.as_view()),
]
