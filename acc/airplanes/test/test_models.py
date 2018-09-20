from django.test import TestCase

from ..models import Airplane
from .. import utils


class TestAirplane(TestCase):

    def setUp(self):
        self.valid_data = {
            'id': 21,
            'passengers': 231,
        }

    def test_create_instance(self):
        instance = Airplane.objects.create_instance(**self.valid_data)

        self.assertEqual(instance.id, self.valid_data['id'])
        self.assertEqual(instance.fuel_tank, utils.calculate_fuel_tank(self.valid_data['id']))
        self.assertEqual(instance.consumption, utils.calculate_consumption(self.valid_data['id']))
