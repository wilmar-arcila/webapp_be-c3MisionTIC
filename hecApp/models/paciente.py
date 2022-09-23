import imp
from pydoc import importfile
from django.db import models

from hecApp.models.familiar import Familiar
from hecApp.models.usuario import Usuario

class Paciente(models.Model):
    id        = models.BigAutoField(primary_key=True)
    usuario   = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    familiar  = models.ForeignKey(Familiar, on_delete=models.DO_NOTHING)
    eps       = models.CharField(max_length=20)
    admision  = models.DateField()