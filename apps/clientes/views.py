from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Cliente, Vehiculo, Documento
from .serializers import ClienteSerializer, VehiculoSerializer, DocumentoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

    #para el buscador
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'correo', 'telefono'] # Campos donde buscará

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [IsAuthenticated]

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    permission_classes = [IsAuthenticated]
