from django.db import models

from hecApp.models.usuario import Usuario

class Enfermero(models.Model):
    id       = models.BigAutoField(primary_key=True)
    area     = models.CharField(max_length=30)
    auxiliar = models.BooleanField()
    usuario  = models.ForeignKey(Usuario, on_delete=models.CASCADE)