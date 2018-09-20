from math import log
from decimal import Decimal

CAPACITY_VALUE = 200


def calculate_fuel_tank(id):
    return id * CAPACITY_VALUE


def calculate_consumption(id):
    return Decimal(log(id * 0.8))
