from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestUserDetailTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('airplane-calculate-consumptions')

    def test_calculate_consumptions_url(self):
        self.assertEqual(self.url, '/api/v1/airplanes/calculate_consumptions/')

    def test_calculate_consumptions(self):
        payload = [
            {
                "id": 15,
                "passengers": 54
            },
            {
                "id": 6,
                "passengers": 54
            },
            {
                "id": 7,
                "passengers": 56
            }
        ]
        response = self.client.post(self.url, payload, format='json')

        # TODO iterate through the response data and compare with data coming from managers.create_instance function
        self.assertEqual(response.status_code, status.HTTP_200_OK)
