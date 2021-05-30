"""account 앱 url 라우터 등록"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UniversityViewSet, UserViewSet

router = DefaultRouter()
router.register('user', UserViewSet)
router.register('university',UniversityViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
