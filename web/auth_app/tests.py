from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.test import TestCase, override_settings
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APITestCase
# Create your tests here.
from django.conf import settings
from rest_framework import status
from django.core import mail
import re

from main.services import UserService

User = get_user_model()


class AuthApiTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        print('setUpTestData')
        data = {
            'email': 'art05xxx@rambler.ru',
            'password': make_password('string1985'),
        }
        cls.user = User.objects.create(**data)
        cls.user.emailaddress_set.create(email=cls.user.email, primary=True, verified=True)

    def test_sign_in(self):
        url = reverse_lazy('auth_app:api_login')

        data = {
            'email': self.user.email,
            'password': 'string1985',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_sign_in_bad_request(self):
        url = reverse_lazy('auth_app:api_login')
        data = {
            'email': 'oemr.m.aa@mail.ru',
            'password': 'string1985',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)
        self.assertEqual(response.data, {'email': ['Entered email or password is incorrect']})

    def test_sign_is_not_active(self):
        self.user.is_active = False
        self.user.save()

        url = reverse_lazy('auth_app:api_login')
        data = {
            'email': self.user.email,
            'password': 'string1985',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)
        self.assertEqual(response.data, {'email': ['Your account is not active. Please contact Your administrator']})

    def test_sign_is_not_verified(self):
        email_address = self.user.emailaddress_set.get()
        email_address.verified = False
        email_address.save()
        url = reverse_lazy('auth_app:api_login')
        data = {
            'email': self.user.email,
            'password': 'string1985',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)
        print(response.data)
        self.assertEqual(response.data, {'email': ['Email not verified']})

    def test_sigh_up(self):
        url = reverse_lazy('auth_app:api_sign_up')
        data = {
            'first_name': 'Hero',
            'last_name': 'HHH',
            'email': 'oemr.m.aa@mail.ru',
            'password1': 'string1985',
            'password2': 'string1986',
            'gender': 'male',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)
        self.assertEqual(response.json(), {'password2': ["The two password fields didn't match."]})

        data['password2'] = 'string1985'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        user = UserService.get_user('oemr.m.aa@mail.ru')
        self.assertTrue(user.is_active)

    def test_logout(self):
        url = reverse_lazy('auth_app:api_login')
        data = {
            'email': self.user.email,
            'password': 'string1985',

        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.client.cookies.get('jwt-auth'))
        url = reverse_lazy('auth_app:logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(self.client.cookies.get('jwt-auth'))
        url = reverse_lazy('actions:like_dislike')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
