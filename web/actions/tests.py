from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APITestCase
from django.contrib.auth.hashers import make_password
from rest_framework import status

from posts.choices import PostStatus
from posts.models import Post

User = get_user_model()


class LikeApiTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        print('setUpTestData')
        data = {
            'email': 'art05xxx@rambler.ru',
            'password': make_password('string1985'),
        }
        cls.user = User.objects.create(**data)
        cls.user.emailaddress_set.create(email=cls.user.email, primary=True, verified=True)

        data = {
            'title': 'Sport',
            'content': 'Test content',
            'status': PostStatus.ACTIVE,
        }
        cls.post = Post.objects.create(**data)

    def setUp(self):
        self.url = reverse_lazy('actions:like_dislike')
        url = reverse_lazy('auth_app:api_login')
        data = {
            'email': self.user.email,
            'password': 'string1985',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_make_like(self):
        data = {
            'vote': 1,
            'post': self.post.id,
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        self.assertEqual(response.data, {'like_count': 1, 'dislike_count': 0, 'status': 1})
        print(response.data)

    def test_inactive_post_like(self):
        self.post.status = PostStatus.INACTIVE
        self.post.save()

        data = {
            'vote': 1,
            'post': self.post.id,
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)
        # print(response.data)
        self.assertEqual(response.data, {'post': [f'Invalid pk "{self.post.id}" - object does not exist.']})

    def test_double_dislike(self):
        data = {
            'vote': -1,
            'post': self.post.id,
        }
        response = self.client.post(self.url, data, format='json')
        print(response.data)
        self.assertEqual(response.data, {'like_count': 0, 'dislike_count': 1, 'status': -1})
        data = {
            'vote': -1,
            'post': self.post.id,
        }
        response = self.client.post(self.url, data, format='json')
        print(response.data)
        self.assertEqual(response.data, {'like_count': 0, 'dislike_count': 0, 'status': -1})

    def test_like_after_dislike(self):
        data = {
            'vote': -1,
            'post': self.post.id,
        }
        response = self.client.post(self.url, data, format='json')
        print(response.data)
        self.assertEqual(response.data, {'like_count': 0, 'dislike_count': 1, 'status': -1})
        data = {
            'vote': 1,
            'post': self.post.id,
        }
        response = self.client.post(self.url, data, format='json')
        print(response.data)
        self.assertEqual(response.data, {'like_count': 1, 'dislike_count': 0, 'status': 1})
