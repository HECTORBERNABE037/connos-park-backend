from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Aviso
from .serializers import AvisoSerializer

class AvisoViewSet(viewsets.ModelViewSet):
    queryset = Aviso.objects.all()
    serializer_class = AvisoSerializer
    permission_classes = [IsAuthenticated] # Cualquier usuario logueado puede verlos

    #solo admins publican
    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]