from rest_framework.test import APITestCase
from humanoids.models import Humanoid
import json

class AvailableCountries(APITestCase):

    def setUp(self):
        Humanoid.objects.create(name='Mario', email='a@email.com', country='Iowa')
        Humanoid.objects.create(name='Mario', email='b@email.com', country='Utah')
        Humanoid.objects.create(name='Mario', email='c@email.com', country='Alabama')
        Humanoid.objects.create(name='Mario', email='d@email.com', country='Alabama')
        Humanoid.objects.create(name='Mario', email='e@email.com', country='Utah')
        Humanoid.objects.create(name='Mario', email='f@email.com', country='Alabama')
        Humanoid.objects.create(name='Mario', email='g@email.com', country='Illinois')

    def test_available_countries(self):
        response = self.client.get('/api/countries')
        result_countries = json.loads(response.content)
        self.assertEqual(result_countries, ['Alabama', 'Illinois', 'Iowa', 'Utah'])