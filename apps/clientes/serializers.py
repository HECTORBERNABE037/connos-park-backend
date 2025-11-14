from rest_framework import serializers
from .models import Cliente, Vehiculo, Documento
import re
from rest_framework.validators import UniqueValidator

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    vehiculos = VehiculoSerializer(many=True, read_only=True)
    documentos = DocumentoSerializer(many=True, read_only=True)
    correo = serializers.EmailField(
        validators=[UniqueValidator(queryset=Cliente.objects.all(), message="Este correo ya está registrado.")]
    )

    def validate_direccion(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("La dirección debe tener al menos 10 caracteres.")
        if value.lower().startswith("calle") == False: # Ejemplo de formato, ajusta como necesites
            raise serializers.ValidationError("La dirección debe iniciar con 'Calle' o incluir un formato similar.")
        return value

    def validate_telefono(self, value):
        telefono_limpio = re.sub(r'\D', '', value)
        if not (len(telefono_limpio) == 10 or (len(telefono_limpio) == 12 and telefono_limpio.startswith('52'))):
            raise serializers.ValidationError(
                'El teléfono debe contener 10 dígitos (lada + número) o 12 dígitos con código de país +52.'
            )
        return value
    
    def validate_nombre(self, value):
        if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+$', value):
            raise serializers.ValidationError('El nombre solo puede contener letras y espacios.')
        return value

    class Meta:
        model = Cliente
        fields = [
            'id', 'nombre', 'telefono', 'direccion', 'correo', 'activo',
            'fecha_registro', 'fecha_modificacion', 'vehiculos', 'documentos',
        ]
        read_only_fields = ['fecha_registro', 'fecha_modificacion', 'vehiculos', 'documentos']
