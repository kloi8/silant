from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
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

router = DefaultRouter()
router.register(r'maintenances', MaintenanceViewSet, basename='maintenance')
router.register(r'reclamations', ReclamationViewSet, basename='reclamation')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('machines/', MachineCreateView.as_view(), name='machine-create'),
    path('machines/<int:pk>/', MachineView.as_view(), name='machine-detail'),
    path('', include(router.urls)),
]