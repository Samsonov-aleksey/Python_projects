from django.test import TestCase, Client
from .forms import FormWeather
from django.urls import reverse
# Create your tests here.


class UnitTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_weather_info_get(self):
        response = self.client.get(reverse('weather_info'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weather/index.html')

    def test_form_is_valid(self):
        form_data = {'city': 'Moscow'}
        form = FormWeather(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_is_not_valid(self):
        form_data = {'city': 111}
        form = FormWeather(data=form_data)
        self.assertFalse(form.is_valid())







