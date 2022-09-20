from django.db import models
from django.utils.translation import gettext_lazy as _

class Rol(models.Model):
    class TipoUsuario(models.TextChoices):
        PACIENTE  = 'PA', _('Paciente')
        FAMILIAR  = 'FA', _('Familiar')
        AUXILIAR  = 'AUX', _('Auxiliar')
        MEDICO    = 'MD', _('Medico')
        ENFERMERO = 'ENF', _('Enfermero')
    
    tipo_usuario = models.CharField(primary_key=True, max_length=3, choices=TipoUsuario.choices)
    permisos = models.IntegerField(default=0)