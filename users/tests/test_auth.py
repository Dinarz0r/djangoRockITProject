from django.contrib.auth import get_user_model
from django.utils import timezone
from faker import Faker
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from posts.models import Post

User = get_user_model()
fake = Faker()


class TestPages(APITestCase):
    """Тестирование приложения"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.USERNAME = 'testusername'
        cls.PASSWORD = 'Qq12345678!'
        cls.user = User.objects.create(username=cls.USERNAME, password=cls.PASSWORD)

        posts = []
        for idx in range(5):
            posts.append(Post(
                author=cls.user,
                name=fake.name(),
                content=fake.paragraph(nb_sentences=5),
                published_at=timezone.now()
            ))

        if posts:
            Post.objects.bulk_create(posts)

    def setUp(self):
        tokens = RefreshToken.for_user(self.user)
        self.token_refresh = str(tokens)
        self.token_access = str(tokens.access_token)

    def test_request(self):
        """
        Проверка получения поста для авторизованного пользователя
        """
        post = Post.objects.filter(pk=1).first()
        bearer = f'Bearer {self.token_access}'
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=bearer)
        response = client.get(f'/api/publications/posts/{post.hash}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(post.name, response.data['name'])

    def test_getting_a_token_non_access(self):
        """Тест получение токена при неверном вводе пароля"""
        form = {'username': self.USERNAME, 'password': 'NeverniyParol'}
        response = self.client.post('/api/token/jwt/create/', form)

        self.assertNotEqual(response.status_code, 200)
