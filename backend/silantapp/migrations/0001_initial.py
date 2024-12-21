# Generated by Django 5.1.4 on 2024-12-20 16:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlledBridgeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Название')),
                ('description', models.CharField(max_length=1024, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель управляемого моста',
                'verbose_name_plural': 'Модели управляемого моста',
            },
        ),
        migrations.CreateModel(
            name='DriveBridgeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Название')),
                ('description', models.CharField(max_length=1024, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель ведущего мооста',
                'verbose_name_plural': 'Модели ведущего моста',
            },
        ),
        migrations.CreateModel(
            name='EngineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Название')),
                ('description', models.CharField(max_length=1024, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель двигателя',
                'verbose_name_plural': 'Модели двигателя',
            },
        ),
        migrations.CreateModel(
            name='EquipmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Название')),
                ('description', models.CharField(max_length=1024, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель техники',
                'verbose_name_plural': 'Модели техники',
            },
        ),
        migrations.CreateModel(
            name='MaintenanceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Название')),
                ('description', models.CharField(max_length=1024, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Вид ТО',
                'verbose_name_plural': 'Виды ТО',
            },
        ),
        migrations.CreateModel(
            name='RecoveryMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Название')),
                ('description', models.CharField(max_length=1024, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Способ восстановления',
                'verbose_name_plural': 'Способы восстановления',
            },
        ),
        migrations.CreateModel(
            name='RefusalPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Название')),
                ('description', models.CharField(max_length=1024, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Узел отказа',
                'verbose_name_plural': 'Узлы отказа',
            },
        ),
        migrations.CreateModel(
            name='ServiceCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Название')),
                ('description', models.CharField(max_length=256, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Сервисная компания',
                'verbose_name_plural': 'Сервисные компании',
            },
        ),
        migrations.CreateModel(
            name='TransmissionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Название')),
                ('description', models.CharField(max_length=1024, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель трансмиссии',
                'verbose_name_plural': 'Модели трансмиссий',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('managerUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Менеджер',
                'verbose_name_plural': 'Менеджеры',
            },
        ),
        migrations.CreateModel(
            name='Serviсe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviсeUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Сервисная компания',
                'verbose_name_plural': 'Сервисные компании',
            },
        ),
        migrations.CreateModel(
            name='Reclamation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refusalDate', models.DateField(verbose_name='Дата отказа')),
                ('reclamationDevelopment', models.IntegerField(verbose_name='Наработка м/час')),
                ('refusalDescription', models.CharField(max_length=2048, verbose_name='Описание отказа')),
                ('spareParts', models.CharField(max_length=2048, verbose_name='Используемые зап.части')),
                ('recoveryDate', models.DateField(verbose_name='Дата восстановления')),
                ('machineDowntime', models.IntegerField(editable=False, verbose_name='Время простоя техники')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantapp.equipmentmodel', verbose_name='Машина')),
                ('recoveryMethod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantapp.recoverymethod', verbose_name='Способ восстановления')),
                ('refusalPoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantapp.refusalpoint', verbose_name='Узел отказа')),
                ('serviceCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantapp.serviсe', verbose_name='Сервисная компания')),
            ],
            options={
                'verbose_name': 'Рекламация',
                'verbose_name_plural': 'Рекламация',
            },
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintDate', models.DateField(verbose_name='Дата проведения ТО')),
                ('maintDevelopment', models.IntegerField(verbose_name='Наработка м/час')),
                ('workOrderNumder', models.CharField(max_length=64, verbose_name='№ заказ-наряда')),
                ('workOrderDate', models.DateField(verbose_name='Дата заказ-наряда')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantapp.equipmentmodel', verbose_name='Машина')),
                ('maintType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantapp.maintenancetype', verbose_name='Вид ТО')),
                ('maintOrganization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantapp.servicecompany', verbose_name='Организация, проводившая ТО')),
                ('serviceCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantapp.serviсe', verbose_name='#Сервисная компания')),
            ],
            options={
                'verbose_name': 'ТО',
                'verbose_name_plural': 'ТО',
            },
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machineNumber', models.CharField(max_length=64, unique=True, verbose_name='Зав. № машины')),
                ('engineNumder', models.CharField(max_length=32, unique=True, verbose_name='Зав.№ двигателя')),
                ('transmissionNumber', models.CharField(max_length=64, unique=True, verbose_name='Зав. № трансмиссии')),
                ('driveBidgeNumder', models.CharField(max_length=64, unique=True, verbose_name='Зав. № ведущего моста')),
                ('controlledBridgeNumber', models.CharField(max_length=64, verbose_name='Зав. № управляемого моста')),
                ('contract', models.CharField(max_length=32, verbose_name='Договор поставки №, дата')),
                ('shipmentDate', models.DateField(verbose_name='Дата отгрузки')),
                ('consignee', models.CharField(max_length=128, verbose_name='Грузополучатель')),
                ('deliveryAdress', models.CharField(max_length=128, verbose_name='Адрес поставки')),
                ('equipment', models.TextField(verbose_name='Комплектация')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantapp.client', verbose_name='Клиент')),
                ('controlledBridgeModel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantapp.controlledbridgemodel', verbose_name='Модель управляемого моста')),
                ('driveBridgeModel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantapp.drivebridgemodel', verbose_name='Модель ведущего моста')),
                ('engineModel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantapp.enginemodel', verbose_name='Модель двигателя')),
                ('machineModel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantapp.equipmentmodel', verbose_name='Модель техники')),
                ('serviceCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantapp.serviсe', verbose_name='Сервисная компания')),
                ('transmissionModel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantapp.transmissionmodel', verbose_name='Модель трансмиссии')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
            },
        ),
    ]
