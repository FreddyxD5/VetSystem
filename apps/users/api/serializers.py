from rest_framework import serializers
from apps.user.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ('modified_at','eliminated_at', )