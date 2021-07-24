"""Quetion App url 라우터 등록"""

from django.urls import path

from .views import (QuestionCreateView, QuestionDestroyView,
                    QuestionDetailView, QuestionListView, QuestionUpdateView)

app_name = 'questions'


urlpatterns = [
    path('', QuestionListView.as_view()),
    path('new/', QuestionCreateView.as_view()),
    path('<int:pk>/', QuestionDetailView.as_view()),
    path('<int:pk>/destroy/', QuestionDestroyView.as_view()),
    path('<int:pk>/edit/', QuestionUpdateView.as_view()),
]
