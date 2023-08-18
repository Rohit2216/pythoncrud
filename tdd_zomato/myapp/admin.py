from django.contrib import admin


from django.test import TestCase, Client
from django.urls import reverse
from myapp.models import Dish

class AdminTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_login_url = reverse('admin:login')
        self.dish_change_url = reverse('admin:myapp_dish_change', args=[1])  # Adjust the URL based on your app name and model

    def test_admin_login(self):
        response = self.client.get(self.admin_login_url)
        self.assertEqual(response.status_code, 200)

    def test_dish_change_page(self):
        self.client.login(username='your_username', password='your_password')
        response = self.client.get(self.dish_change_url)
        self.assertEqual(response.status_code, 200)

# Register your models here.
