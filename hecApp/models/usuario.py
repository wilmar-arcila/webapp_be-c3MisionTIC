from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

from hecApp.models.rol import Rol

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    id        = models.BigAutoField(primary_key=True)
    rol       = models.ForeignKey(Rol, related_name='_rol', to_field='tipo_usuario', on_delete=models.CASCADE)
    password  = models.CharField('Password', max_length = 256)
    nombre    = models.CharField('Nombre', max_length = 30)
    apellido  = models.CharField('Apellido', max_length = 30)
    celular   = models.CharField('Celular', max_length = 30)
    direccion = models.CharField('Direccion', max_length = 256)
    email     = models.EmailField('Email', max_length = 100, unique=True)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK7vgTdIYwpkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
        objects = UserManager()
    
    USERNAME_FIELD = 'email'