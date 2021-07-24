"""msof_api project urls"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from msof_api.renderer import JSONResponseRenderer

openapi_info = openapi.Info(
   title="MSOF API",
   default_version='v1',
   description="API description",
   terms_of_service="https://www.google.com/policies/terms/",
   contact=openapi.Contact(email="singun11@kookmin.ac.kr"),
   license=openapi.License(name="MIT License"),
)

schema_view = get_schema_view(
   openapi_info,
   public=True,
   permission_classes=(permissions.AllowAny,),
)

class CustomSchemaView(schema_view):
   renderer_classes = (
      JSONResponseRenderer,
   )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('questions/', include('msof_api.questions.urls')),
    path('comments/', include('msof_api.comments.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', CustomSchemaView.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', CustomSchemaView.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', CustomSchemaView.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
