from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Cajon
from .serializers import CajonSerializer

class CajonViewSet(viewsets.ModelViewSet):
    queryset = Cajon.objects.all()
    serializer_class = CajonSerializer
    permission_classes = [IsAuthenticated]
