from django.contrib import admin

from measurement.models import Sensor, Measurement


@admin.register(Measurement)
class Measurement_admin(admin.ModelAdmin):
    list_display = ['id', 'sensor', 'temperature', 'created_at', ]

class MeasurementInLine(admin.TabularInline):
    model = Measurement
    extra = 3


@admin.register(Sensor)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', ]
    inlines = [MeasurementInLine, ]
