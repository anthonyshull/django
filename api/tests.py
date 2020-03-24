from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_api_key.models import APIKey

from .models import Engineer


class EngineersTest(APITestCase):
    def test_create_engineer(self):
        """
        Ensure we can create a new engineer.
        """
        name = 'Guido van Rossum'
        rank = 10
        url = reverse('engineers-list')
        data = {
            'name': name,
            'rank': rank,
        }
        api_key, key = APIKey.objects.create_key(name="tests")
        response = self.client.post(url, data, format='json', headers={'X-Api-Key': key})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Engineer.objects.count(), 1)
        self.assertEqual(Engineer.objects.get().name, name)
