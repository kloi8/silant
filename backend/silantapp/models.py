from django.db import models
from django.contrib.auth.models import User

#ПОЛЬЗОВАТЕЛИ

#Клиент
class Client(models.Model):
    clientUser = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.clientUser}'
    
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

#Сервисная компания-пользователь
class Serviсe(models.Model):
    serviсeUser = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.serviсeUser}'

    class Meta:
        verbose_name = 'Сервисная компания(пользователь)'
        verbose_name_plural = 'Сервисные компании(пользователи)'

#Менеджер 
class Manager(models.Model):
    managerUser = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.managerUser}'
    
    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'


#СПРАВОЧНИКИ

#Класс Модель техники
class EquipmentModel(models.Model):
    title = models.CharField('Название', max_length=64, unique=True)
    description = models.CharField('Описание', max_length=1024)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Модель техники'
        verbose_name_plural = 'Модели техники'

#Класс Модель двигателя
class EngineModel(models.Model):
    title = models.CharField('Название', max_length=64, unique=True)
    description = models.CharField('Описание', max_length=1024)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Модель двигателя'
        verbose_name_plural = 'Модели двигателя'

#Класс Модель трансмиссии
class TransmissionModel(models.Model):
    title = models.CharField('Название', max_length=64, unique=True)
    description = models.CharField('Описание', max_length=1024)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Модель трансмиссии'
        verbose_name_plural = 'Модели трансмиссий'


#Класс Модель ведущего места
class DriveBridgeModel(models.Model):
    title = models.CharField('Название', max_length=64, unique=True)
    description = models.CharField('Описание', max_length=1024)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Модель ведущего мооста'
        verbose_name_plural = 'Модели ведущего моста'

#Класс Модель управляемого моста
class ControlledBridgeModel(models.Model):
    title = models.CharField('Название', max_length=64, unique=True)
    description = models.CharField('Описание', max_length=1024)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Модель управляемого моста'
        verbose_name_plural = 'Модели управляемого моста'




#Класс вид ТО
class MaintenanceType(models.Model):
    title = models.CharField('Название', max_length=64, unique=True)
    description = models.CharField('Описание', max_length=1024)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Вид ТО'
        verbose_name_plural = 'Виды ТО'

#Класс сервисная компания
class ServiceCompany(models.Model):
    title = models.CharField('Название', max_length=64, unique=True)
    description = models.CharField('Описание', max_length=256)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Сервисная компания'
        verbose_name_plural = 'Сервисные компании'

#Класс Узел отказа
class RefusalPoint(models.Model):
    title = models.CharField('Название', max_length=64, unique=True)
    description = models.CharField('Описание', max_length=1024)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Узел отказа'
        verbose_name_plural = 'Узлы отказа'

#Класс способ восстановления
class RecoveryMethod(models.Model):
    title = models.CharField('Название', max_length=64, unique=True)
    description = models.CharField('Описание', max_length=1024)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Способ восстановления'
        verbose_name_plural = 'Способы восстановления'



#ОСНОВНЫЕ СУЩНОСТИ

#Класс Машина
class Machine(models.Model):
    machineNumber = models.CharField(verbose_name='Зав. № машины', max_length=64, unique=True) #Зав. № машины
    machineModel = models.ForeignKey(EquipmentModel, verbose_name='Модель техники', on_delete=models.CASCADE) #Модель техники
    engineModel = models.ForeignKey(EngineModel, verbose_name='Модель двигателя', on_delete=models.CASCADE) #Модель двигателя
    engineNumder = models.CharField(verbose_name='Зав.№ двигателя', max_length=32, unique=True) #Зав. № двигателя
    transmissionModel = models.ForeignKey(TransmissionModel, verbose_name='Модель трансмиссии', on_delete=models.CASCADE) #Модель трансмиссии
    transmissionNumber = models.CharField(verbose_name='Зав. № трансмиссии', max_length=64,unique=True) #Зав. № трансмиссии
    driveBridgeModel = models.ForeignKey(DriveBridgeModel, verbose_name='Модель ведущего моста', on_delete=models.CASCADE) #Модель ведущего моста
    driveBidgeNumder = models.CharField(verbose_name='Зав. № ведущего моста', max_length=64,unique=True) #Зав. № ведущего моста
    controlledBridgeModel = models.ForeignKey(ControlledBridgeModel, verbose_name='Модель управляемого моста', on_delete=models.CASCADE) #Модель управляемого моста
    controlledBridgeNumber = models.CharField(verbose_name='Зав. № управляемого моста', max_length=64,) #Зав. № управляемого моста
    contract = models.CharField(verbose_name='Договор поставки №, дата', max_length=32,) #договор поставки №, дата
    shipmentDate = models.DateField(verbose_name='Дата отгрузки') #Дата отгрузки
    consignee = models.CharField(verbose_name='Грузополучатель', max_length=128,) #грузополучатель
    deliveryAdress = models.CharField(verbose_name='Адрес поставки', max_length=128,) #адрес поставки
    equipment = models.TextField(verbose_name='Комплектация') #комплектация
    client = models.ForeignKey(Client, verbose_name='Клиент', on_delete=models.CASCADE) #Клиент
    serviceCompany = models.ForeignKey(Serviсe, verbose_name='Сервисная компания', on_delete=models.CASCADE) #Сервисная компания

    def __str__(self):
        return f'Серийный номер машины: {self.machineNumber}, модель: {self.machineModel}, клиент: {self.client}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

#Класс ТО
class Maintenance(models.Model):
    maintType = models.ForeignKey(MaintenanceType, verbose_name='Вид ТО', on_delete=models.CASCADE) #Вид ТО
    maintDate = models.DateField(verbose_name='Дата проведения ТО') #Дата проведения ТО
    maintDevelopment = models.IntegerField(verbose_name='Наработка м/час') #наработка, м/час
    workOrderNumder = models.CharField(verbose_name='№ заказ-наряда', max_length=64) # № заказ-наряда
    workOrderDate = models.DateField(verbose_name='Дата заказ-наряда') # Дата заказ-наряда
    maintOrganization= models.ForeignKey(ServiceCompany, verbose_name='Организация, проводившая ТО', on_delete=models.CASCADE) #организация, проводившая ТО
    machine = models.ForeignKey(EquipmentModel, verbose_name='Машина', on_delete=models.CASCADE) #Машина
    serviceCompany = models.ForeignKey(Serviсe, verbose_name='#Сервисная компания', on_delete=models.CASCADE) #Сервисная компания


    def __str__(self):
        return f'Машина: {self.machine}, Вид ТО: {self.maintType}, Сервисная компания: {self.serviceCompany}'

    class Meta:
        verbose_name = 'ТО'
        verbose_name_plural = 'ТО'

#Класс Рекламация
class Reclamation(models.Model):
    refusalDate = models.DateField(verbose_name='Дата отказа') #Дата отказа
    reclamationDevelopment = models.IntegerField(verbose_name='Наработка м/час') #наработка м/ч
    refusalPoint = models.ForeignKey(RefusalPoint, verbose_name='Узел отказа', on_delete=models.CASCADE) #Узел отказа
    refusalDescription = models.CharField(verbose_name='Описание отказа', max_length=2048) #Описание отказа
    recoveryMethod = models.ForeignKey(RecoveryMethod, verbose_name='Способ восстановления', on_delete=models.CASCADE) #Способ восстановления
    spareParts = models.CharField(verbose_name='Используемые зап.части', max_length=2048) #используемые зап.части
    recoveryDate = models.DateField(verbose_name='Дата восстановления') #Дата восстановления
    machineDowntime = models.IntegerField(verbose_name='Время простоя техники', editable=False) #время простоя техники
    machine = models.ForeignKey(EquipmentModel, verbose_name='Машина', on_delete=models.CASCADE) #Машина
    serviceCompany = models.ForeignKey(Serviсe, verbose_name='Сервисная компания', on_delete=models.CASCADE) #Сервисная компания


    def save(self, *args, **kwargs):
        self.machineDowntime = (self.recoveryDate - self.refusalDate).days
        super(Reclamation, self).save(*args, **kwargs)

    def __str__(self):
        return f'Машина: {self.machine}, дата поломки: {self.refusalDate}, время простоя: {self.machineDowntime}'
    
    class Meta:
        verbose_name = 'Рекламация'
        verbose_name_plural = 'Рекламация'

