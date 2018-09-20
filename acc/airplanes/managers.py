from math import log
from decimal import Decimal
from django.db import models


class AirplaneQuerySet(models.QuerySet):
    def get_queryset(self):
        return self.get_queryset()


class AirplaneManager(models.Manager):
    CAPACITY_VALUE = 200

    def get_queryset(self):
        return AirplaneQuerySet(self.model, using=self._db)

    def create_instance(self, id, passengers):
        return self.model(
            id=id,
            fuel_tank=id * self.CAPACITY_VALUE,
            consumption=Decimal(log(id * 0.8)),
            passengers=passengers
        )

    def create_and_get_all(self, data):
        """
        :param data: list of id and passengers numbers
        :return: QuerySet instances

        Divide objects into three categories:
        1) existed: don't need any action
        2) updated: need to update
        3) created: need to create using bulk_create method (one query to DB)
        """

        # TODO: realize as described in documentation
        instances = [self.create_instance(item.get('id'), item.get('passengers', 0)) for item in data]
        return instances
