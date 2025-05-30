from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from api.models import Post

class CreatePostTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='SecurePass123')
        self.client = APIClient()
        self.url = '/api/posts/create/'
        self.token_url = '/api/token-auth/'
        self.valid_data = {
            "title": "Test Post",
            "content": "This is a test blog post.",
            "category": "Tech"
        }

    def authenticate(self):
        response = self.client.post(
            self.token_url,
            data={"username": "testuser", "password": "SecurePass123"},
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

    def test_create_post_authenticated(self):
        self.authenticate()
        response = self.client.post(self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.first().author.username, "testuser")
        print("create post unit testing pass!!")

