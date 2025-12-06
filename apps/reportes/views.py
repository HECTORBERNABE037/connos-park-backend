
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.usuarios.permissions import CanGenerateReports

class ReporteGeneralView(APIView):
    permission_classes = [IsAuthenticated,CanGenerateReports]

    def get(self, request):
        # Ejemplo de respuesta, puedes quitar esto y hacer lógica real
        data = {
            "reporte": "Aquí mostrarías tu primer reporte, ejemplo: pagos, ocupación, etc.",
            "status": "Pendiente de implementar lógica real"
        }
        return Response(data)
