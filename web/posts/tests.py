from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.hashers import make_password


User = get_user_model()


class PostApiTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        print('setUpTestData')
        data = {
            'email': 'test22@test.com',
            'password': make_password('tester26'),
        }
        cls.user = User.objects.create(**data, is_active=True)
        cls.user.emailaddress_set.create(email=cls.user.email, primary=True, verified=True)

    def setUp(self):
        url = reverse_lazy('auth_app:api_login')
        data = {
            'email': self.user.email,
            'password': 'tester26',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_create_post(self):
        url = reverse_lazy('posts:post-list')
        data = {
            'title': 'Sport',
            'content': 'Test content',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        print(response.data)

        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        print(response.data)

    def test_create_post_forbidden(self):
        url = reverse_lazy('auth_app:logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        url = reverse_lazy('posts:post-list')
        data = {
            'title': 'Sport',
            'content': 'Test content',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        print("Create article forbidden", response.data)
