from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Cliente, Vehiculo, Documento
from .serializers import ClienteSerializer, VehiculoSerializer, DocumentoSerializer
from .permissions import CanEditClientData

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated,CanEditClientData]#encargado no puede modificar datos del cliente

    #para el buscador
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'correo', 'telefono'] # Campos donde buscará

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [IsAuthenticated,CanEditClientData]#encargado no puede modificar datos del vehiculo

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    permission_classes = [IsAuthenticated,CanEditClientData]#encargado no puede modificar datos del contrato
