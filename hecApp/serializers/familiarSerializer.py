from string import printable
from rest_framework import serializers
from hecApp.models.familiar import Familiar

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = ['id', 'parentezco', 'usuario']