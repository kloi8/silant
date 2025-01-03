from rest_framework import permissions

from .models import *

# #Разрешения для Машин
# class MachinePermissions(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if not request.user.is_authenticated: #Что делать с неавторизованными
#             return request.method == 'GET'
#         user = request.user
#         if user.is_authenticated: #Настройка контроля доступа
#             if hasattr(user, 'сlient'): #значение не нужно, только проверка
#                 return request.method == 'GET'
#             elif hasattr(user, 'serviсe'):
#                 return request.method == 'GET'
#             elif hasattr(user, 'manager'):
#                 return request.method in ['GET', 'POST']
#             return False

# #Разрешения для ТО
# class MaintenancePermissions(permissions.BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         if user.is_authenticated:
#             if hasattr(user, 'client'):
#                 return request.method == 'GET'
#             elif hasattr(user, 'serviсe'):
#                 return request.method in ['GET', 'POST']
#             elif hasattr(user, 'manager'):
#                 return request.method in ['GET', 'POST']           
#             return False

# #Разрешения для рекламации
# class ReclamationPermissions(permissions.BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         if user.is_authenticated:
#             if hasattr(user, 'client'):
#                 return request.method == 'GET'
#             elif hasattr(user, 'serviсe'):
#                 return request.method in ['GET', 'POST']
#             elif hasattr(user, 'manager'):
#                 return request.method in ['GET', 'POST']        
#             return False

# #Разрешения для списков
# class ListPermissions(permissions.BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         if user.is_authenticated:
#             if hasattr(user, 'client'): 
#                 return request.method == 'GET'
#             elif hasattr (user,'serviсe'):
#                 return request.method in ['GET']
#             elif hasattr (user,'manager'):
#                 return request.method in ['GET', 'POST', 'PUT', 'DELETE']
#             return False
        




# __________________________________________________________________
# __________________________________________________________________
# __________________________________________________________________
# __________________________________________________________________


# Базовый класс разрешений
class BasePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        # Проверка на аутентификацию
        if not request.user.is_authenticated:
            return request.method == 'GET'

        user = request.user
        # Проверка прав в зависимости от роли пользователя
        if hasattr(user, 'client'):
            return self.check_client_permissions(request)
        elif hasattr(user, 'service'):
            return self.check_service_permissions(request)
        elif hasattr(user, 'manager'):
            return self.check_manager_permissions(request)

        # Если роль не определена
        return False
    
# Разрешение для клиентов
    def check_client_permissions(self, request):
        return request.method == 'GET'

# Разрешение для серв.компаний
    def check_service_permissions(self, request):
        return request.method in ['GET', 'POST']

# разрешение для менеджеров
    def check_manager_permissions(self, request):
        return request.method in ['GET', 'POST', 'PUT', 'DELETE']

# Проверить права
    def has_object_permission(self, request, view, obj):
        return True

#Разрешения для Машин
class MachinePermissions(BasePermissions):
    def has_object_permission(self, request, view, obj):
        user = request.user #Проверка доступа
        # Клиенты могут видеть только свои машины
        if hasattr(user, 'client'): #значение не нужно, только проверка
            return obj.client == user.client
        # Сервисные компании могут видеть машины, которые они обслуживают
        elif hasattr(user, 'service'):
            return obj.serviceCompany == user.service
        # Менеджеры имеют полный доступ
        elif hasattr(user, 'manager'):
            return True
        return False

#Разрешения для ТО
class MaintenancePermissions(BasePermissions):
    def has_object_permission(self, request, view, obj):
        user = request.user
        # Клиенты могут видеть только ТО своих машин
        if hasattr(user, 'client'):
            return obj.machine.client == user.client
        # Серв.компании могут видеть ТО машин, которые они обслуживают
        elif hasattr(user, 'service'):
            return obj.serviceCompany == user.service
        # Менеджеры имеют полный доступ
        elif hasattr(user, 'manager'):
            return True
        return False


#Разрешения для рекламации
class ReclamationPermissions(BasePermissions):
    def has_object_permission(self, request, view, obj):
        user = request.user
        # Клиенты могут видеть только рекламации своих машин
        if hasattr(user, 'client'):
            return obj.machine.client == user.client
        # Серв.компании могут видеть рекламации машин, которые обслуживают
        elif hasattr(user, 'service'):
            return obj.serviceCompany == user.service
        # Менеджеры имеют полный доступ
        elif hasattr(user, 'manager'):
            return True
        return False


# Разрешения для справочников
class ListPermissions(BasePermissions):
    # Клиенты могут только просматривать справочники
    def check_client_permissions(self, request):
        return request.method == 'GET'
    
# Сервисные компании могут только просматривать справочники
    def check_service_permissions(self, request):
        return request.method == 'GET'

# Менеджеры могут выполнять любые действия
    def check_manager_permissions(self, request):
        return request.method in ['GET', 'POST', 'PUT', 'DELETE']
