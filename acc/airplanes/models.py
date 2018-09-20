from django.db import models
from django.utils.translation import ugettext_lazy as _


class Airplane(models.Model):
    id = models.PositiveIntegerField(primary_key=True, unique=True)
    fuel_tank = models.PositiveIntegerField(_('fuel tank'))
    consumption = models.FloatField(_('consumption'))

    def __str__(self):
        return self.id
