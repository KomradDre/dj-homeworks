from django.contrib import admin
from .models import Sensor, Measurement

class MeasurementInline(admin.TabularInline):
    """Встроенное отображение измерений для датчика"""
    model = Measurement
    extra = 1  # Количество пустых форм для добавления
    fields = ('temperature', 'created_at', 'image_preview')
    readonly_fields = ('created_at', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return admin.utils.mark_safe(f'<img src="{obj.image.url}" width="100" />')
        return "Нет изображения"
    image_preview.short_description = "Превью"

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    """Административный интерфейс для датчиков"""
    list_display = ('id', 'name', 'description', 'measurement_count')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    inlines = [MeasurementInline]

    def measurement_count(self, obj):
        return obj.measurements.count()
    measurement_count.short_description = "Кол-во измерений"

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    """Административный интерфейс для измерений"""
    list_display = ('id', 'sensor', 'temperature', 'created_at', 'image_preview')
    list_filter = ('sensor', 'created_at')
    readonly_fields = ('created_at', 'image_preview')
    date_hierarchy = 'created_at'

    def image_preview(self, obj):
        if obj.image:
            return admin.utils.mark_safe(f'<img src="{obj.image.url}" width="100" />')
        return "Нет изображения"
    image_preview.short_description = "Превью"