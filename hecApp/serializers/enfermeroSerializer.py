from string import printable
from rest_framework import serializers
from hecApp.models.enfermero import Enfermero

class EnfermeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermero
        fields = ['id', 'area', 'auxiliar', 'usuario']