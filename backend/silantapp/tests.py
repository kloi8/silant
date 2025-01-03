from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Client, Service, Manager

# class UserLoginTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create_user(username='testuser', password='testpassword')
#         self.client_user = Client.objects.create(clientUser=self.user)
#         self.service_user = Service.objects.create(serviceUser=self.user)
#         self.manager_user = Manager.objects.create(managerUser=self.user)

#     def test_login_success(self):
#         url = reverse('user-login')
#         data = {
#             'username': 'testuser',
#             'password': 'testpassword'
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['message'], 'Login successful')
#         self.assertIn('role', response.data)

#     def test_login_failure(self):
#         url = reverse('user-login')
#         data = {
#             'username': 'testuser',
#             'password': 'wrongpassword'
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(response.data['message'], 'Кажется вы ввели неверный логин или пароль. Если у вас нет логина и пароля и вы являетесь клиентом, отправьте сообщение на почту "corporation@mail.ru".')


class MachineTests(APITestCase):

# создание пользователя и токена
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

# создание новой машины
    def test_create_machine(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {'machineNumber': '123', 'machineModel': 'Excavator'}
        response = self.client.post('/machines/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# Получение списка машин
    def test_get_machines(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get('/machines/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)