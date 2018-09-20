from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Airplane
from .serializers import AirplaneSerializer


class AirplaneViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    permission_classes = (AllowAny,)

    @action(methods=['post'], detail=False)
    def calculate_consumptions(self, request, pk=None):
        """
        Accepts airplane id and passengers number, filtering it and stores (create, update, get) in DB
        Calculate fuel consumption (per/minute) for every airplane and return them in increasing order
        by flying time, so the last item is an airplane which has maximum minutes able to fly,
        """

        data = filter(lambda x: x.get('id') and isinstance(x['id'], int), request.data)
        query_set = Airplane.objects.create_and_get_all(data)
        serializer = AirplaneSerializer(data=query_set, many=True)
        serializer.is_valid()
        data = sorted(serializer.data, key=lambda x: x.get('id'))
        return Response(data=data)

