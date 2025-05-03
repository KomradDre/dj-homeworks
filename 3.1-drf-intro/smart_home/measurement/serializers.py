from rest_framework import serializers
from .models import Sensor, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'image']
        read_only_fields = ['created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(
        many=True,
        read_only=True,
        source='measurements.all'
    )

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


class SensorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'image']
        extra_kwargs = {
            'image': {'required': False, 'allow_null': True}
        }