from rest_framework import serializers
from .models import Aviso

class AvisoSerializer(serializers.ModelSerializer):
    # Formateamos la fecha y hora para que el front no batalle tanto
    fecha_formato = serializers.SerializerMethodField()
    hora_formato = serializers.SerializerMethodField()

    class Meta:
        model = Aviso
        fields = ['id', 'mensaje', 'fecha_creacion', 'fecha_formato', 'hora_formato']

    def get_fecha_formato(self, obj):
        # Ej: "26 de septiembre"
        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        fecha_local = obj.fecha_creacion # Django maneja la zona horaria si USE_TZ=True
        return f"{fecha_local.day} de {meses[fecha_local.month - 1]}"

    def get_hora_formato(self, obj):
        # Ej: "9:10 pm"
        return obj.fecha_creacion.strftime("%I:%M %p").lower()