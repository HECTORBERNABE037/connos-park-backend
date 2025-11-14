from django.contrib import admin
from .models import Contrato

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'cajon', 'fecha_inicio', 'activo', 'monto_mensual', 'fecha_creacion']
    search_fields = ['cliente__nombre', 'cajon__numero']
    list_filter = ['activo', 'fecha_inicio']
