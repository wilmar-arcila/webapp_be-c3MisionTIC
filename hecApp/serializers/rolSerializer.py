from rest_framework import serializers
from hecApp.models.rol import Rol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['tipo_usuario', 'permisos']