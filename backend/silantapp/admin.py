from django.contrib import admin
from .models import *

# Юзеры
admin.site.register(Client)
admin.site.register(Serviсe)
admin.site.register(Manager)
# Основные сущности
admin.site.register(Machine)
admin.site.register(Maintenance)
admin.site.register(Reclamation)
# Справочники
admin.site.register(EquipmentModel)
admin.site.register(EngineModel)
admin.site.register(TransmissionModel)
admin.site.register(DriveBridgeModel)
admin.site.register(ControlledBridgeModel)
admin.site.register(MaintenanceType)
admin.site.register(ServiceCompany)
admin.site.register(RefusalPoint)
admin.site.register(RecoveryMethod)

# Mary - пользователь Mary9876
# 
# Kirill - менеджер Kiril9876
# 
# Jully - сервисная комп Jull9876
# Avelie - Aveli9876