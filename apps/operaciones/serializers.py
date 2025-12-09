from rest_framework import serializers
from .models import Cajon

class CajonSerializer(serializers.ModelSerializer):
    ocupado = serializers.ReadOnlyField()
    
    class Meta:
        model = Cajon
        fields = '__all__'