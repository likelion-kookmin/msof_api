"""account app ViewSet
request에 따른 response를 처리하기 위한 모듈
"""
from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import University
from .serializers import UniversitySerializer

class UniversityViewSet(viewsets.ModelViewSet):  # pylint: disable=R0901&R0903
    """UserViewSet
    User 모델에 대한 기본적인 GET,POST,PUT,DELETE 메소드 지원
    ModelViewSet 자체가 많은 view 관련 class를 상속받기 때문에
    pylint: disable=R0901를 안 걸어주면 pylint에서 many ancenstor 걸림
    """
    queryset = University.objects.all() # pylint: disable=E1101
    serializer_class = UniversitySerializer
