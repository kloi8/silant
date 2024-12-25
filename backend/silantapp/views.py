from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from drf_yasg.utils import swagger_auto_schema

from .models import *
from .serializers import *
from .permissions import *
from .filters import *

# Просмотр и содзание объектов "Машина"
class MachineCreateView(APIView):
    permission_classes = [MachinePermissions]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = MachineFilters
    ordering_fields = ['shipmentDate']

# Авторизован или нет
    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return MachineSerializer
        return UnauthenticatedSerializer

# Данные от роли
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

    @swagger_auto_schema(
        operation_description="Получение списка машин",
        responses={200: MachineSerializer(many=True)}
    )
    # Обрабатываем гет
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        queryset = self.paginate_queryset(queryset)
        serializer = self.get_serializer_class()(queryset, many=True)
        return self.get_paginated_response(serializer.data)

    @swagger_auto_schema(
        operation_description="Создание новой машины",
        request_body=MachineSerializer,
        responses={201: MachineSerializer(), 400: "Bad Request"}
    )
    # Обработка ПОСТ (если новая)
    def post(self, request, *args, **kwargs):
        serializer = MachineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Просмотр, удаление, обновление МАШИНА
class MachineView(APIView):
    permission_classes = [MachinePermissions]

    def get_serializer_class(self):
# Авторизация проверка
        if self.request.user.is_authenticated:
            return MachineSerializer
        return UnauthenticatedSerializer

# Вернем по пк
    def get_object(self, pk):
        try:
            return Machine.objects.get(pk=pk)
        except Machine.DoesNotExist:
            return None

    @swagger_auto_schema(
        operation_description="Получение информации о машине",
        responses={200: MachineSerializer(), 404: "Not Found"}
    )

    # обработка запросов ......
    def get(self, request, pk, *args, **kwargs):
        machine = self.get_object(pk)
        if machine:
            serializer = MachineSerializer(machine)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_description="Обновление информации о машине",
        request_body=MachineSerializer,
        responses={200: MachineSerializer(), 400: "Bad Request", 404: "Not Found"}
    )
    # ...........
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
        operation_description="Удаление машины",
        responses={204: "No Content", 404: "Not Found"}
    )
    def delete(self, request, pk, *args, **kwargs):
# .........
        machine = self.get_object(pk)
        if machine:
            machine.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

# ТО
class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
    permission_classes = [MaintenancePermissions]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = MaintenanceFilter
    ordering_fields = ['maintDate']

    def get_queryset(self):
# ............
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
        operation_description="Получение информации о ТО",
        responses={200: MaintenanceSerializer(), 404: "Not Found"}
    )
    def retrieve(self, request, *args, **kwargs):
# Обработка запросов разных
        instance = self.get_object()
        serializer = MaintenanceSerializer(instance)
        return Response(serializer.data)

# Рекламация
class ReclamationViewSet(viewsets.ModelViewSet):
    queryset = Reclamation.objects.all()
    serializer_class = ReclamationSerializer
    permission_classes = [ReclamationPermissions]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ReclamationFilter
    ordering_fields = ['refusalDate']

    def get_queryset(self):
# ..........
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
        operation_description="Получение информации о рекламации",
        responses={200: ReclamationSerializer(), 404: "Not Found"}
    )
    def retrieve(self, request, *args, **kwargs):
# Обработка запросов
        instance = self.get_object()
        serializer = ReclamationSerializer(instance)
        return Response(serializer.data)

# .............
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [ListPermissions]

