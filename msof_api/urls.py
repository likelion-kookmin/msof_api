"""msof_api project urls"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('account/', include('allauth.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('user/', include('accounts.urls')),
    path('question/', include('msof_api.question.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
