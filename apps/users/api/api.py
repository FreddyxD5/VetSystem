from rest_framework.viewsets import GenericViewSet
from apps.users.models import Usuario

class UsuarioViewSet(GenericViewSet):
    model = Usuario
    serializer_class = UsuarioSerializer