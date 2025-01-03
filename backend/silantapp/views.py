from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend #OrderingFilter
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema
from .models import *
from .serializers import *
from .permissions import *
from .filters import *
from rest_framework.decorators import action
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, login, logout

# Представление для пользователей
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful', 'role': self.get_user_role(user)})
        else:
            return Response({'message': 'Неверный логин или пароль.'}, status=status.HTTP_400_BAD_REQUEST)

    def get_user_role(self, user):
        if hasattr(user, 'client'):
            return 'client'
        elif hasattr(user, 'service'):
            return 'service'
        elif hasattr(user, 'manager'):
            return 'manager'
        return None

# Представление для Клиентов
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

# Представление для Сервисных компаний
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Serviсe.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

# Представление для Менеджеров
class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

# Представление для "Машина"
class MachineView(APIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = [MachinePermissions]  # доступ по настройке
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MachineFilters
    search_fields = ['machineSerialNumber']
    ordering_fields = ['shipmentDate']

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return MachineSerializer
        return UnauthenticatedSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if hasattr(user, 'client'):
                return Machine.objects.filter(client=user.client)
            elif hasattr(user, 'service'):
                return Machine.objects.filter(serviceCompany=user.service)
            elif hasattr(user, 'manager'):
                return Machine.objects.all()
        return Machine.objects.none()

    def filter_queryset(self, queryset):
        # Применяем фильтры и сортировку
        for backend in self.filter_backends:
            queryset = backend().filter_queryset(self.request, queryset, self)
    # Сортировка
        ordering = self.request.query_params.get('ordering')
        if ordering:
            ordering_fields = [field.strip() for field in ordering.split(',')]
            queryset = queryset.order_by(*ordering_fields)
        return queryset
    
# Настройки пагинации
    def paginate_queryset(self, queryset):
        paginator = PageNumberPagination()
        paginator.page_size = 15  # Размер страницы
        paginated_queryset = paginator.paginate_queryset(queryset, self.request)
        return paginated_queryset, paginator
    
    @swagger_auto_schema(
            operation_description='Получение списка машин',
            responses={200: MachineSerializer(many=True)}
        )
 
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        paginated_queryset, paginator = self.paginate_queryset(queryset)
        serializer = self.serializer_class(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)


    @swagger_auto_schema(
        operation_description='Создание новой машины',
        request_body=MachineSerializer,
        responses={201: MachineSerializer(), 400: 'Машина не найдена, повторите попытку'}
    )
    def post(self, request, *args, **kwargs):
        serializer = MachineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Представление для Машина подробное
class MachineDetailView(APIView):
    permission_classes = [MachinePermissions]
    authentication_classes = [TokenAuthentication]

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return MachineSerializer
        return UnauthenticatedSerializer

    def get_object(self, pk):
        try:
            return Machine.objects.get(pk=pk)
        except Machine.DoesNotExist:
            return None

    @swagger_auto_schema(
        operation_description='Получение информации о машине',
        responses={200: MachineSerializer(), 404: 'Страница не найдена'}
    )
    def get(self, request, pk, *args, **kwargs):
        machine = self.get_object(pk)
        if machine:
            serializer = MachineSerializer(machine)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_description='Обновление информации о машине',
        request_body=MachineSerializer,
        responses={200: MachineSerializer(), 400: 'Машина не найдена, повторите попытку', 404: 'Страница не найдена'}
    )
    def put(self, request, pk, *args, **kwargs):
        machine = self.get_object(pk)
        if machine:
            serializer = MachineSerializer(machine, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_description='Удаление машины',
        responses={204: 'No Content', 404: 'Страница не найдена'}
    )
    def delete(self, request, pk, *args, **kwargs):
        machine = self.get_object(pk)
        if machine:
            machine.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)



# Представление для ТО
class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
    permission_classes = [MaintenancePermissions]
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = MaintenanceFilter
    ordering_fields = ['maintDate']

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if hasattr(user, 'client'):
                return Maintenance.objects.filter(machine__client=user.client)
            elif hasattr(user, 'service'):
                return Maintenance.objects.filter(serviceCompany=user.service)
            elif hasattr(user, 'manager'):
                return Maintenance.objects.all()
        return Maintenance.objects.none()

    @swagger_auto_schema(
        operation_description='Получение информации о ТО',
        responses={200: MaintenanceSerializer(), 404: 'Страница не найдена'}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MaintenanceSerializer(instance)
        return Response(serializer.data)



# Представление для Рекламаций
class ReclamationViewSet(viewsets.ModelViewSet):
    queryset = Reclamation.objects.all()
    serializer_class = ReclamationSerializer
    permission_classes = [ReclamationPermissions]
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ReclamationFilter
    ordering_fields = ['refusalDate']

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if hasattr(user, 'client'):
                return Reclamation.objects.filter(machine__client=user.client)
            elif hasattr(user, 'service'):
                return Reclamation.objects.filter(serviceCompany=user.service)
            elif hasattr(user, 'manager'):
                return Reclamation.objects.all()
        return Reclamation.objects.none()

    @swagger_auto_schema(
        operation_description='Получение информации о рекламации',
        request_body=ReclamationSerializer,
        responses={200: ReclamationSerializer(), 404: 'Страница не найдена'}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ReclamationSerializer(instance)
        return Response(serializer.data)



# Представления для справочников
class ServiceCompanyViewSet(viewsets.ModelViewSet):
    queryset = ServiceCompany.objects.all()
    serializer_class = ServiceCompanySerializer
    permission_classes = [ListPermissions]
    authentication_classes = [TokenAuthentication]

class EngineModelViewSet(viewsets.ModelViewSet):
    queryset = EngineModel.objects.all()
    serializer_class = EngineModelSerializer
    permission_classes = [ListPermissions]
    authentication_classes = [TokenAuthentication]

class EquipmentModelViewSet(viewsets.ModelViewSet):
    queryset = EquipmentModel.objects.all()
    serializer_class = EquipmentModelSerializer
    permission_classes = [ListPermissions]
    authentication_classes = [TokenAuthentication]

class DriveBridgeModelViewSet(viewsets.ModelViewSet):
    queryset = DriveBridgeModel.objects.all()
    serializer_class = DriveBridgeModelSerializer
    permission_classes = [ListPermissions]
    authentication_classes = [TokenAuthentication]

class ControlledBridgeModelViewSet(viewsets.ModelViewSet):
    queryset = ControlledBridgeModel.objects.all()
    serializer_class = ControlledBridgeModelSerializer
    permission_classes = [ListPermissions]
    authentication_classes = [TokenAuthentication]

class MaintenanceTypeViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceType.objects.all()
    serializer_class = MaintenanceTypeSerializer
    permission_classes = [ListPermissions]
    authentication_classes = [TokenAuthentication]

class RefusalPointViewSet(viewsets.ModelViewSet):
    queryset = RefusalPoint.objects.all()
    serializer_class = RefusalPointSerializer
    permission_classes = [ListPermissions]
    authentication_classes = [TokenAuthentication]

class RecoveryMethodViewSet(viewsets.ModelViewSet):
    queryset = RecoveryMethod.objects.all()
    serializer_class = RecoveryMethodSerializer
    permission_classes = [ListPermissions]
    authentication_classes = [TokenAuthentication]
