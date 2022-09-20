from rest_framework import serializers
from hecApp.models.usuario import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellido', 'celular', 'direccion', 'email', 'password', 'rol']