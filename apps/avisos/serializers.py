from rest_framework import serializers
from django.utils.timezone import localtime 
from .models import Aviso

class AvisoSerializer(serializers.ModelSerializer):
    fecha_formato = serializers.SerializerMethodField()
    hora_formato = serializers.SerializerMethodField()

    class Meta:
        model = Aviso
        fields = ['id', 'mensaje', 'fecha_creacion', 'fecha_formato', 'hora_formato']

    def get_fecha_formato(self, obj):
        # Convertimos la fecha UTC a la hora local configurada (Mexico_City)
        fecha_local = localtime(obj.fecha_creacion)
        
        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        return f"{fecha_local.day} de {meses[fecha_local.month - 1]}"

    def get_hora_formato(self, obj):
        # Convertimos a local antes de formatear la hora
        fecha_local = localtime(obj.fecha_creacion)
        return fecha_local.strftime("%I:%M %p").lower()