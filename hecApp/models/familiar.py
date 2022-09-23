from django.db import models

from hecApp.models.usuario import Usuario

class Familiar(models.Model):
    id         = models.BigAutoField(primary_key=True)
    parentezco = models.CharField(max_length=30)
    usuario    = models.ForeignKey(Usuario, on_delete=models.CASCADE)