from decimal import Decimal
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import AirplaneManager


class Airplane(models.Model):
    PASSENGER_FUEL_CONSUMPTION = 0.002

    id = models.PositiveIntegerField(primary_key=True, unique=True)
    fuel_tank = models.PositiveIntegerField(_('fuel tank'))
    consumption = models.DecimalField(_('consumption'), max_digits=6, decimal_places=2)

    passengers = models.IntegerField(_('passengers'), default=0)

    class Meta:
        app_label = 'airplanes'

    @property
    def total_consumption(self):
        return self.consumption + Decimal(self.passengers * self.PASSENGER_FUEL_CONSUMPTION)

    @property
    def available_flying_time(self):
        return self.fuel_tank / self.total_consumption

    objects = AirplaneManager()
