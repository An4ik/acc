from rest_framework import serializers
from .models import Airplane


class AirplaneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airplane
        fields = ('id', 'passengers', 'total_consumption', 'available_flying_time')

