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
    def calculation(self, request, pk=None):
        """
        1. do calculation of consumption
        2. store in database
        3. serialize queryset
        4. return data
        """

        data = filter(lambda x: x.get('id') and isinstance(x['id'], int), request.data)
        query_set = Airplane.objects.bulk_create(data)
        serializer = AirplaneSerializer(data=query_set, many=True)
        serializer.is_valid()
        return Response(data=serializer.data)

