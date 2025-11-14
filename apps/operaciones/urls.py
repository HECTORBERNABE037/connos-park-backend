from rest_framework.routers import DefaultRouter
from .views import CajonViewSet

router = DefaultRouter()
router.register(r'cajones', CajonViewSet, basename='cajon')

urlpatterns = router.urls
