from rest_framework import serializers
from .models import Cajon

class CajonSerializer(serializers.ModelSerializer):

    def validate_numero(self, value):
        if value <= 0:
            raise serializers.ValidationError("El número del cajón debe ser mayor que cero.")
        return value
    
    class Meta:
        model = Cajon
        fields = '__all__'
