from string import printable
from rest_framework import serializers
from hecApp.models.historia import Historia
from hecApp.models.paciente import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'eps', 'admision', 'familiar', 'usuario']
    
    def create(self, validated_data):
        print("Serializando Paciente")
        pacienteObj = Paciente.objects.create(**validated_data)
        historia = Historia.objects.create(paciente=pacienteObj)
        return pacienteObj