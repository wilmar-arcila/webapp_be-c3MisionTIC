from string import printable
from rest_framework import serializers
from hecApp.models.historia import Historia

class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia
        #fields = ['__all__']