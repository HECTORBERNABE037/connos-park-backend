from rest_framework import serializers
from .models import Pago

class PagoSerializer(serializers.ModelSerializer):
    def validate_monto(self, value):
        if value <= 0:
            raise serializers.ValidationError("El monto debe ser positivo y mayor a cero.")
        return value

    class Meta:
        model = Pago
        fields = '__all__'
