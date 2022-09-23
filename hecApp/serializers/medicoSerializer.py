from string import printable
from rest_framework import serializers
from hecApp.models.medico import Medico
from hecApp.models.usuario import Usuario

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id', 'especialidad', 'usuario']

    def create(self, validated_data):
        print("create medico")
        print(validated_data)
        return super().create(validated_data)