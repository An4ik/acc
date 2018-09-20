from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import Airplane
from .serializers import AirplaneSerializer


class AirplaneViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    permission_classes = (AllowAny,)
