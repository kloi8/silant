from rest_framework import serializers
from .models import *
from .models import Machine, Maintenance, Reclamation

# Сериализатор для неавторизованных пользователей
# Ограниченный просмотр полей из "Машина" (1-10)
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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']

class ClientSerializer(serializers.ModelSerializer):
    clientUser = UserSerializer()

    class Meta:
        model = Client
        fields = ['id', 'clientUser']

class ServiceSerializer(serializers.ModelSerializer):
    serviceUser = UserSerializer()

    class Meta:
        model = Serviсe
        fields = ['id', 'serviceUser']

class ManagerSerializer(serializers.ModelSerializer):
    managerUser = UserSerializer()

    class Meta:
        model = Manager
        fields = ['id', 'managerUser']
        

# Сериализатор для Справочников
class ServiceCompanySerializer(serializers.ModelSerializer):  
    class Meta:
        model = ServiceCompany
        fields = '__all__'

class EngineModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineModel
        fields = '__all__'

class EquipmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentModel
        fields = '__all__'

class DriveBridgeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriveBridgeModel
        fields = '__all__'

class ControlledBridgeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlledBridgeModel
        fields = '__all__'

class MaintenanceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceType
        fields = '__all__'

class RefusalPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefusalPoint
        fields = '__all__'

class RecoveryMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecoveryMethod
        fields = '__all__'


# Сериализаторы для авторизованных пользователей

class MachineSerializer(serializers.ModelSerializer):
    machineModel = EquipmentModelSerializer()  # сериализатор для модели машины
    engineModel = EngineModelSerializer()  # сериализатор для модели двигателя
    transmissionModel = EquipmentModelSerializer()
    driveBridgeModel = DriveBridgeModelSerializer()
    controlledBridgeModel = ControlledBridgeModelSerializer()
    client = ClientSerializer()  # сериализатор для клиента
    serviceCompany = ServiceSerializer()  # сериализатор для сервисной компании

    class Meta:
        model = Machine
        fields = '__all__'




# class MaintenanceCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Maintenance
#         fields = '__all__'

#     def create(self, validated_data):
#         user = self.context['request'].user
#         try:
#             service_company = ServiceCompany.objects.get(serviceCompanyUser=user)
#         except ServiceCompany.DoesNotExist:
#             return Maintenance.objects.create(**validated_data)
#         validated_data['serviceCompany'] = service_company
#         return Maintenance.objects.create(**validated_data)



class MaintenanceSerializer(serializers.ModelSerializer):
    maintType = MaintenanceTypeSerializer()  #  сериализатор для типа ТО
    machine = MachineSerializer()  # сериализатор для машины
    serviceCompany = ServiceSerializer()  # сервисная компания

    class Meta:
        model = Maintenance
        fields = '__all__'


class ReclamationSerializer(serializers.ModelSerializer):
    refusalPoint = RefusalPointSerializer()  # сериализатор для точки отказа
    recoveryMethod = RecoveryMethodSerializer()  # сериализатор для метода восстановления
    machine = MachineSerializer()  # сериализатор для машины
    serviceCompany = ServiceSerializer()  # сервисная компания

    class Meta:
        model = Reclamation
        fields = '__all__'



# class ReclamationCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reclamation
#         fields = '__all__'

    # def create(self, validated_data):
    #     user = self.context['request'].user
    #     try:
    #         service_company = ServiceCompany.objects.get(serviceCompanyUser=user)
    #     except ServiceCompany.DoesNotExist:
    #         return Reclamation.objects.create(**validated_data)
    #     validated_data['serviceCompany'] = service_company
    #     return Reclamation.objects.create(**validated_data)





