# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from .models import Sensor
from .serializers import SensorSerializer


@api_view(['GET'])
def info_sensor(request):
    sensors = Sensor.objects.all()
    ser = SensorSerializer(sensors, many=True)
    # data = {
    #     'name_sensor': 'SENSOR_1',
    #     'info': 'bedroom'
    # }
    return Response(ser.data)

class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
