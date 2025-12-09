from rest_framework import serializers
from .models import Cajon

class CajonSerializer(serializers.ModelSerializer):
    ocupado = serializers.ReadOnlyField()#regresa los datos de solo lectura al front
    
    class Meta:
        model = Cajon
        fields = '__all__'