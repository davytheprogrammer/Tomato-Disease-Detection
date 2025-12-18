from django.contrib import admin
from .models import Prediction


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ['image_name', 'prediction', 'confidence', 'timestamp']
    list_filter = ['prediction', 'timestamp']
    search_fields = ['image_name', 'prediction']
