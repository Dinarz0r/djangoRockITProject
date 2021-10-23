from django.contrib.auth.models import User
from django.test import TestCase, Client

class TestPages(TestCase):
    """Тестирование приложения"""

    @classmethod
    def setUpTestData(cls):
        cls.USERNAME = 'testusername'
        cls.PASSWORD = 'Qq12345678!'
        cls.user = User.objects.create_user(username=cls.USERNAME, email='USER_EMAIL@test.ru', password=cls.PASSWORD)

    def test_getting_a_token_access(self):
        """Тест получение токена при верном вводе логина и пароля"""
        form = {'username': self.USERNAME, 'password': self.PASSWORD}
        response = self.client.post('/api/token/jwt/create/', form)
        self.token = response.json().get('access')
        self.assertEqual(response.status_code, 200)

    def test_getting_a_token_non_access(self):
        """Тест получение токена при неверном вводе пароля"""
        form = {'username': self.USERNAME, 'password': 'NeverniyParol'}
        response = self.client.post('/api/token/jwt/create/', form)

        self.assertNotEqual(response.status_code, 200)
