from django.contrib.models.auth import authenticate
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet
from apps.users.models import Usuario

class UsuarioViewSet(GenericViewSet):
    model = Usuario
    serializer_class = UsuarioSerializer


def login(self, request):
    if request.method =="POST":
        data = request.data
        try:
            Usuario.objects.filter(username = data['username'])
        except:
            return Response({'error':'Usuario no existe'},
                            status = status.HTTP_400_BAD_REQUEST)
    
        user = authenticate(username = data['username'], password = data['password'])
        if user:
            #Generar Token
            return Response({'message':"se ha iniciado session"},
                        status=status.HTTP_200_OK)
        return Response({'error':'La contraseña es incorrecta.'},
                        status = status.HTTP_400_BAD_REQUEST)

