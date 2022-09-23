import imp
from pydoc import importfile
from django.db import models

from hecApp.models.paciente import Paciente

class Historia(models.Model):
    id               = models.BigAutoField(primary_key=True)
    paciente         = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    oximetria        = models.JSONField(null=True)
    f_respiratoria   = models.JSONField(null=True)
    f_cardiaca       = models.JSONField(null=True)
    temperatura      = models.JSONField(null=True)
    presion_arterial = models.JSONField(null=True)
    glicemias        = models.JSONField(null=True)
    diagnostico      = models.TextField(null=True)
    cuidados         = models.TextField(null=True)