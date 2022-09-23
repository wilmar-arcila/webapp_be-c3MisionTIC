from string import printable
from rest_framework import serializers
from hecApp.models.enfermero import Enfermero
from hecApp.models.usuario import Usuario

class EnfermeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermero
        fields = ['id', 'area', 'auxiliar', 'usuario']