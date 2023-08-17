from django.test import TestCase

from .models import Task
# Create your tests here.
from django.urls import reverse


class TaskModelTest(TestCase):
    def test_task_model_exists(self):
         tasks=Task.objects.count()

         self.assertEqual(tasks,0)

    def test_model_has_string_representation(self):
        task=Task.objects.create(title='first test')
        self.assertEqual(str(task),task.title)  

class IndexPageTest(TestCase):

    def setUp(self):
        self.task= Task.objects.create(title='First task')


    def test_index_page_returns_correct_response(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'task/index.html')

    def test_index_page_has_tasks(self):
        # task= Task.objects.create(title='First task')

        response= self.client.get('/')

        self.assertContains(response,self.task.title)


class DetailPageTest(TestCase):

    def setUp(self):
        self.task= Task.objects.create(title='First task', description="the description")
        self.task2= Task.objects.create(title='second task', description="the description")


    def test_detail_page_returns_correct_response(self):
        response=self.client.get(f'/{self.task.id}/')
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'task/detail.html')

    def test_detail_page_returns_correct_content(self):
        response=self.client.get(f'/{self.task.id}/')    

        self.assertContains(response,self.task.title)
        self.assertContains(response,self.task.description)
        self.assertNotContains(response, self.task2.title)


# from django.test import TestCase

class WeatherTestCase(TestCase):
    def setUp(self):
        self.weather_data = {
            'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
            'New York': {'temperature': 20, 'weather': 'Sunny'},
            'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
            'Seattle': {'temperature': 10, 'weather': 'Rainy'},
            'Austin': {'temperature': 32, 'weather': 'Hot'},
        }

    def test_valid_city_weather(self):
        for city, data in self.weather_data.items():
            response = self.client.get(reverse('get_weather', args=[city]))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), data)

    def test_invalid_city_weather(self):
        response = self.client.get(reverse('get_weather', args=['NonExistentCity']))
        self.assertEqual(response.status_code, 404)


    def test_add_weather_data(self):
        data = {
            'city': 'Chicago',
            'temperature': 18,
            'weather': 'Cloudy',
        }
        response = self.client.post(reverse('add_weather'), data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

        # Fetch updated weather data from the response
        added_weather = response.json()

        # Check if the added_weather is not None
        self.assertIsNotNone(added_weather)

        # Check specific attributes of the added_weather
        self.assertEqual(added_weather['temperature'], 18)
        self.assertEqual(added_weather['weather'], 'Cloudy')


    def test_valid_city_weather(self):
        for city, data in self.weather_data.items():
            response = self.client.get(reverse('get_weather', args=[city]))
            self.assertEqual(response.status_code, 200)
            
            # Check if the response data matches the updated data
            updated_data = self.weather_data.get(city)
            self.assertEqual(response.json(), updated_data)   




    def test_delete_city_weather(self):
        for city in self.weather_data:  # Only iterate through cities
            response = self.client.get(reverse('get_weather', args=[city]))
            self.assertEqual(response.status_code, 200)


      