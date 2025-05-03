from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, \
    CreateAPIView
from .models import Sensor, Measurement
from .serializers import (
    SensorListSerializer,
    SensorDetailSerializer,
    MeasurementCreateSerializer
)


class SensorListCreateView(ListCreateAPIView):
    """
    Обработчик для создания датчика и получения списка датчиков.
    Использует разные сериализаторы для GET и POST запросов.
    """
    queryset = Sensor.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SensorListSerializer
        return SensorDetailSerializer


class SensorRetrieveUpdateView(RetrieveUpdateAPIView):
    """
    Обработчик для получения детальной информации о датчике
    и его обновления (частичного или полного).
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    lookup_field = 'id'


class MeasurementCreateView(CreateAPIView):
    """
    Обработчик для добавления нового измерения температуры.
    Поддерживает загрузку изображений (опционально).
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer