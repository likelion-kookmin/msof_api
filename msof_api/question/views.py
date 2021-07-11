"""Quesion app ViewSet
request에 따른 response를 처리하기 위한 모듈
"""

import json

from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Question
from .permissions import QuestionEditableOrDestroyablePermission


class QuestionIndexView(ListAPIView):
    """QuestionIndexView<br>
    """
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    def get(self, request, *args, **kwargs):
        """GET: /qustion/"""
        try:
            questions = list(Question.objects.published().values())
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'Question list feteched successfully',
                'data': questions
            }
        except Exception as e:  # pylint: disable=W0703
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status_code,
                'message': 'Questions do not exists',
                'error': str(e)
            }
        return Response(response, status=status_code)

class QuestionShowView(RetrieveAPIView):
    """QuestionShowView<br>"""
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]


    def get(self, request, *args, **kwargs):
        """GET: /question/<int:id>/"""
        try:
            question = Question.objects.published().filter(pk=kwargs['id']).values()[0]
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'Question feteched successfully',
                'data': question
            }
        except Exception as e:  # pylint: disable=W0703
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status_code,
                'message': 'Question does not exists',
                'error': str(e)
            }
        return Response(response, status=status_code)

class QuestionCreateView(CreateAPIView):
    """QuestionCreateView<br>

    To use this API, send request like this.

    In Header,`{Authorization: "JWT BLAHBLAH" }`

    In body `{title: "str", content: "str"}`
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    def post(self, request, *args, **kwargs):
        """POST: /question/new/"""
        try:
            title = request.POST.get('title')
            content = request.POST.get('content')

            question = Question(title=title, content=content)
            question.author = request.user
            question.save()
            question = model_to_dict(question)

            status_code = status.HTTP_201_CREATED
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'Question is created successfully',
                'data': question
            }
        except Exception as e:  # pylint: disable=W0703
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status_code,
                'message': 'Question is not created',
                'error': str(e)
            }
        return Response(response, status=status_code)

class QuestionUpdateView(UpdateAPIView):
    """QuestionUpdateView<br>"""

    permission_classes = [IsAuthenticated, QuestionEditableOrDestroyablePermission]
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    def get_object(self, question_id):  # pylint: disable=W0221
        try:
            question = Question.objects.get(pk=question_id)
            self.check_object_permissions(self.request, question)
            return question
        except Question.DoesNotExist:  # pylint: disable=no-member
            return None

    def put(self, request, *args, **kwargs):
        """PUT: /quetion/<int:id>"""
        try:
            put_params = json.loads(request.body.decode("utf-8"), strict=False)
            question = self.get_object(kwargs['id'])
            title = put_params['title']
            content = put_params['content']

            if title is None or content is None:
                raise Exception

            question.title = title
            question.content = content
            question.save()
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'Question is updated successfully',
            }
        except Exception as e:  # pylint: disable=W0703
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status_code,
                'message': 'Question is not updated',
                'error': str(e)
            }
        return Response(response, status=status_code)

    def patch(self, request, *args, **kwargs):
        """PUT: /quetion/<int:id>"""
        try:
            patch_params = json.loads(request.body.decode("utf-8"), strict=False)
            question = self.get_object(kwargs['id'])
            if 'title' in patch_params:
                question.title = patch_params['title']
            if 'content' in patch_params:
                question.content = patch_params['content']
            question.save()
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'Question is updated successfully',
            }
        except Exception as e:  # pylint: disable=W0703
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status_code,
                'message': 'Question is not updated',
                'error': str(e)
            }
        return Response(response, status=status_code)


class QuestionDestroyView(DestroyAPIView):
    """QuestionDestroyView<br>"""

    permission_classes = [IsAuthenticated, QuestionEditableOrDestroyablePermission]
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    def get_object(self, question_id):  # pylint: disable=W0221
        try:
            question = Question.objects.get(pk=question_id)
            self.check_object_permissions(self.request, question)
            return question
        except Question.DoesNotExist:  # pylint: disable=no-member
            return None

    def delete(self, request, *args, **kwargs):
        """DELETE: /quetion/<int:id>"""
        try:
            question = self.get_object(kwargs['id'])
            question.delete()
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'Question is destroyed successfully',
            }
        except Exception as e:  # pylint: disable=W0703
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status_code,
                'message': 'Question is not destroyed',
                'error': str(e)
            }
        return Response(response, status=status_code)
