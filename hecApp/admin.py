from django.contrib import admin

# Register your models here.
from .models.rol import Rol
from.models.usuario import Usuario

admin.site.register(Rol)
admin.site.register(Usuario)