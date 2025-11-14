from django.contrib import admin
from .models import Cliente, Vehiculo, Documento

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'correo', 'activo', 'fecha_registro']
    search_fields = ['nombre', 'correo']
    list_filter = ['activo']

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ['placa', 'marca', 'modelo', 'color', 'año', 'cliente']
    search_fields = ['placa', 'marca', 'modelo']
    list_filter = ['marca', 'color']

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'tipo', 'archivo', 'fecha_subida']
    list_filter = ['tipo', 'fecha_subida']
