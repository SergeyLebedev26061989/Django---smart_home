from rest_framework import serializers

# TODO: опишите необходимые сериализаторы

# class Sensor_serializer(serializers.Serializer):
#     temperature = serializers.FloatField()
#     date_of_measurement = serializers.DateTimeField()
from measurement.models import Sensor, Measurement
#
#
# class SensorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sensor
#         fields = ['name', 'description']
#
#
# class MeasurementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Measurement
#         fields = ['id', 'temperature', 'date_of_measurement']
