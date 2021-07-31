"""# comments urls"""

from django.urls import path

from .views import (CommentCreateView, CommentDestroyView, CommentDetailView,
                    CommentListView, CommentUpdateView)

app_name = 'comments'

urlpatterns = [
    path('', CommentListView.as_view()),
    path('new/', CommentCreateView.as_view()),
    path('<int:pk>/', CommentDetailView.as_view()),
    path('<int:pk>/destroy/', CommentDestroyView.as_view()),
    path('<int:pk>/edit/', CommentUpdateView.as_view()),
]
