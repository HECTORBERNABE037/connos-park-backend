from django.contrib import admin
from .models import Cajon

@admin.register(Cajon)
class CajonAdmin(admin.ModelAdmin):
    list_display = ['numero', 'estado', 'descripcion']
    search_fields = ['numero', 'descripcion']
    list_filter = ['estado']
