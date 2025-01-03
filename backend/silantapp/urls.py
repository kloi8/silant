from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
# from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token
# from .views import current_user

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Silant API",
#         default_version='v1',
#         description="API documentation for Silant Project",
#         contact=openapi.Contact(email="contact@mycontact.local"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'managers', ManagerViewSet, basename='manager')

# router.register(r'machines', MachineApiView, basename='machines')
router.register(r'maintenances', MaintenanceViewSet, basename='maintenance')
router.register(r'reclamations', ReclamationViewSet, basename='reclamation')
router.register(r'service-companies', ServiceCompanyViewSet, basename='service-company')
router.register(r'engine-models', EngineModelViewSet, basename='engine-model')
router.register(r'equipment-models', EquipmentModelViewSet, basename='equipment-model')
router.register(r'drive-bridge-models', DriveBridgeModelViewSet, basename='drive-bridge-model')
router.register(r'controlled-bridge-models', ControlledBridgeModelViewSet, basename='controlled-bridge-model')
router.register(r'maintenance-types', MaintenanceTypeViewSet, basename='maintenance-type')
router.register(r'refusal-points', RefusalPointViewSet, basename='refusal-point')
router.register(r'recovery-methods', RecoveryMethodViewSet, basename='recovery-method')

urlpatterns = [
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Для получения токена
    path('machines/', MachineView.as_view(), name='machine-create'),
    path('machines/<int:pk>/', MachineView.as_view(), name='machine-detail'),
    path('', include(router.urls)),
]