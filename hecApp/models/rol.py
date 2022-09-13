from django.db import models
from django.utils.translation import gettext_lazy as _

class Rol(models.Model):
    class TipoUsuario(models.TextChoices):
        PACIENTE = 'PA', _('Paciente')
        FAMILIAR = 'FA', _('Familiar')
        AUXILIAR = 'AUX', _('Auxiliar')
        MEDICO = 'MD', _('Medico')
        ENFERMERO = 'ENF', _('Enfermero')
    
    id = models.AutoField(primary_key=True)
    tipo_usuario = TipoUsuario.choices
    permisos = models.IntegerField(default=0)