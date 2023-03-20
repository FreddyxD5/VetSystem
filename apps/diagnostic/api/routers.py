from rest_framework.routers import DefaultRouter
from apps.diagnostic.api.api import DiagnosticViewSet

router = DefaultRouter()
router.register('', DiagnosticViewSet, basename='diagnostic')

urlpatterns = router.urls