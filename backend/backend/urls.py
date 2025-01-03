
from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Silant API",
        default_version='v1',
        description="API documentation for Silant Project",
        contact=openapi.Contact(email="contact@mycontact.local"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('silantapp.urls')),  # подключаем маршруты из вашего приложения
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("swagger-ui/",
        schema_view.with_ui
        ('swagger', cache_timeout=0), name='schema-swagger-ui'),
]