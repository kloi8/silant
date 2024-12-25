from rest_framework import serializers
from .models import *

from rest_framework import serializers
from .models import Machine, Maintenance, Reclamation

# Сериализатор для неавторизованных пользователей
# Включает только ограниченный набор полей из "Машина"
class UnauthenticatedSerializer(serializers.ModelSerializer):
    machineModel = serializers.StringRelatedField(source = 'machineModel.title')
    engineModel = serializers.StringRelatedField(source = 'engineModel.title')
    transmissionModel = serializers.StringRelatedField(source = 'transmissionModel.title')
    driveBridgeModel = serializers.StringRelatedField(source = 'driveBridgeModel.title')
    controlledBridgeModel = serializers.StringRelatedField(source = 'controlledBridgeModel.title')

    class Meta:
        model = Machine
        fields = [
            'machineNumber', 'machineModel', 'engineModel', 'engineNumder',
            'transmissionModel', 'transmissionNumber', 'driveBridgeModel',
            'driveBidgeNumder', 'controlledBridgeModel', 'controlledBridgeNumber'
        ]

# Сериализаторы для авторизованных пользователей

class MachineSerializer(serializers.ModelSerializer):
    machineModel = serializers.StringRelatedField(source='machineModel.title')
    engineModel = serializers.StringRelatedField(source='engineModel.title')
    transmissionModel = serializers.StringRelatedField(source='transmissionModel.title')
    driveBridgeModel = serializers.StringRelatedField(source='driveBridgeModel.title')
    controlledBridgeModel = serializers.StringRelatedField(source='controlledBridgeModel.title')
    client = serializers.StringRelatedField(source='client.clientUser')
    serviceCompany = serializers.StringRelatedField(source='serviceCompany.serviceUser')
    
    class Meta:
        model = Machine
        fields = '__all__'

#Сериализатор "ТО"

class MaintenanceSerializer(serializers.ModelSerializer):
    maintType = serializers.StringRelatedField(source='maintType.title')
    machine = serializers.StringRelatedField(source='machine.machineNumber')
    serviceCompany = serializers.StringRelatedField(source='serviceCompany.serviceUser')

    class Meta:
        model = Maintenance
        fields = '__all__'

# Сериализатор "Рекламация"

class ReclamationSerializer(serializers.ModelSerializer):
    refusalPoint = serializers.StringRelatedField(source='refusalPoint.title')
    recoveryMethod = serializers.StringRelatedField(source='recoveryMethod.title')
    machine = serializers.StringRelatedField(source='machine.machineNumber')
    serviceCompany = serializers.StringRelatedField(source='serviceCompany.serviceUser')

    class Meta:
        model = Reclamation
        fields = '__all__'



# Сериализатор для Сервисной Компании
class ServiceCompanySerializer(serializers.ModelSerializer):  
    class Meta:
        model = ServiceCompany
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']