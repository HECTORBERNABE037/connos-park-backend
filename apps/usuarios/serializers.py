from rest_framework import serializers
from .models import Usuario, Rol
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id', 'nombre', 'descripcion']

class UsuarioSerializer(serializers.ModelSerializer):
    rol = RolSerializer(read_only=True)
    rol_id = serializers.PrimaryKeyRelatedField(
        queryset=Rol.objects.all(),
        source='rol', write_only=True
    )

    class Meta:
        model = Usuario
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'rol', 'rol_id', 'telefono', 'activo', 'is_superuser', 'is_staff'
        ]
        read_only_fields = ['id', 'is_superuser', 'is_staff']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Personaliza la respuesta del Login para incluir datos del usuario
    además de los tokens de acceso y refresco.
    """
    def validate(self, attrs):
        # 1. Generar la data estándar (access y refresh tokens)
        data = super().validate(attrs)

        # 2. Agregar datos personalizados del usuario al diccionario de respuesta
        # 'self.user' es el usuario que se acaba de autenticar correctamente
        data['user'] = {
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            # Validamos si tiene rol para evitar errores si es None
            'rol': self.user.rol.id if self.user.rol else None,
            'rol_nombre': self.user.rol.nombre if self.user.rol else 'Sin Asignar',
        }

        return data
