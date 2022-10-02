from django.urls import path

from measurement.views import *

urlpatterns = [
    path('sensors/', SensorsList.as_view()),
    path('sensors/<int:pk>/', UpdateSensor.as_view()),
    path('measurements/', MeasurementsList.as_view()),
    path('sensors/detail/<int:pk>/', SensorDetailView.as_view()),
]
