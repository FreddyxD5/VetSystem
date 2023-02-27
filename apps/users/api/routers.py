from rest_framework.routers import DefaultRouter
from apps.users.api.api import UsuarioViewSet

router.register(r'usuarios', UsuarioViewSet, basename='usuarios')

urlpatterns = router.urls 