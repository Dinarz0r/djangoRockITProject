from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication

from djangoProject import __version__

schema_view = get_schema_view(
    openapi.Info(
        title='RockIT',
        default_version=__version__,
        description='Тестовое задание',
        license=openapi.License(name='BSD License'),
    ),
    patterns=[path('api/', include('api.urls'))],
    authentication_classes=(BasicAuthentication,),
    permission_classes=(permissions.IsAuthenticated,),
    public=False
)
urlpatterns = [
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
