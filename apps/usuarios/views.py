from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Usuario, Rol
from .serializers import UsuarioSerializer, RolSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [IsAuthenticated]

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Vista de Login personalizada que usa nuestro serializer modificado
    """
    serializer_class = CustomTokenObtainPairSerializer
