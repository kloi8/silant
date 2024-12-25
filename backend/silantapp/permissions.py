from rest_framework import permissions

from .models import *

#Разрешения для Машин
class MachinePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authentificated: #Что делать с неавторизованными
            return request.method == 'GET'
        user = request.user
        if user.is_authentificated: #Настройка контроля доступа
            if hasattr(user, 'сlient'): #значение не нужно, только проверка
                return request.method == 'GET'
            elif hasattr(user, 'serviсe'):
                return request.method == 'GET'
            elif hasattr(user, 'manager'):
                return request.method in ['GET', 'POST']
            return False

#Разрешения для ТО
class MaintenancePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authentificated:
            if hasattr(user, 'client'):
                return request.method == 'GET'
            elif hasattr(user, 'serviсe'):
                return request.method in ['GET', 'POST']
            elif hasattr(user, 'manager'):
                return request.method in ['GET', 'POST']           
            return False

#Разрешения для рекламации
class ReclamationPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authentificated:
            if hasattr(user, 'client'):
                return request.method == 'GET'
            elif hasattr(user, 'serviсe'):
                return request.method in ['GET', 'POST']
            elif hasattr(user, 'manager'):
                return request.method in ['GET', 'POST']        
            return False

#Разрешения для списков (чтобы редактировали менеджеры)
class ListPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authentificated:
            if hasattr(user, 'client'): 
                return request.method == 'GET'
            elif hasattr (user,'serviсe'):
                return request.method in ['GET']
            elif hasattr (user,'manager'):
                return request.method in ['GET', 'POST', 'PUT', 'DELETE']
            return False