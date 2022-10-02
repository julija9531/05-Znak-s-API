from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


#TODO 1. Создать датчик. Указываются название и описание датчика.
# 4. Получить список датчиков. Выдается список с краткой информацией по датчикам: ID, название и описание
class SensorsList(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


#TODO 2. Изменить датчик. Указываются название и/или описание.
class UpdateSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

#TODO 3. Добавить измерение. Указываются ID датчика и температура.
class MeasurementsList(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

#TODO 5. Получить информацию по конкретному датчику. Выдается полная информация по датчику:
# ID, название, описание и список всех измерений с температурой и временем.
class SensorDetailView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


