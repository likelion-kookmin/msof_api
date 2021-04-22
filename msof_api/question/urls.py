"""Quetion App url 라우터 등록"""

from django.urls import path

from .views import QuestionCreateView, QuestionIndexView, QuestionShowView

app_name = 'question'

urlpatterns = [
    path('', QuestionIndexView.as_view()),
    path('new/', QuestionCreateView.as_view()),
    path('<int:id>/', QuestionShowView.as_view()),
]
