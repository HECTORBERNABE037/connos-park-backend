from django.contrib import admin
from .models import Pago

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ['contrato', 'monto', 'fecha_pago', 'periodo_inicio', 'periodo_fin', 'fecha_registro']
    search_fields = ['contrato__cliente__nombre']
    list_filter = ['fecha_pago']
