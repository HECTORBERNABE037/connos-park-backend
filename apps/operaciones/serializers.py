from rest_framework import serializers
from .models import Cajon

class CajonSerializer(serializers.ModelSerializer):
    # ELIMINAMOS def validate_numero(...) por completo.
    
    class Meta:
        model = Cajon
        fields = '__all__'