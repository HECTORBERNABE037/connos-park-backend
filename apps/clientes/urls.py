from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, VehiculoViewSet, DocumentoViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'vehiculos', VehiculoViewSet, basename='vehiculo')
router.register(r'documentos', DocumentoViewSet, basename='documento')

urlpatterns = router.urls
