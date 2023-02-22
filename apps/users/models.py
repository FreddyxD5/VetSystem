from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionMixin
)

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateField('Fecha de Creacion', auto_now_add =True, auto_now=False)
    modified_at = models.DateField('Fecha de modificacion', auto_now=True, auto_now_add=False)
    eliminated_at = models.DateField('Fecha de eliminacion', auto_now=True, auto_now_add=False)    

    class Meta:
        abstract = True
    

class UsuarioManager(BaseUserManager):
    def _create_user(self, username, email, nombres, apellidos, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            nombres = nombres,
            apellidos = apellidos,
            is_staff= is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, nombres,apellidos, password=None, is_staff, is_superuser, **extra_fields):
        return self._create_user(username, email, nombres,apellidos, password=None, False, False, **extra_fields)
    
    def create_superuser(self, username, email, nombres,apellidos, password=None, is_staff, is_superuser, **extra_fields):
        return self._create_user(self, username, email, nombres,apellidos, password=None, True, True, **extra_fields)



class Usuario(AbstractBaseUser, PermissionMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField('Correo Electronico', max_length=255, unique=True)
    nombres = models.CharField('Nombres' ,max_length=255, blank=True, null=True)
    apellidos = models.CharField('Apellidos' ,max_length=255, blank=True, null=True)
    numero_documento = models.CharField('Numero de Documento', max_length=20, null=True)
    telefono = models.CharField('Telefono', max_length=20, null=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateField('Fecha de Creacion', auto_now_add =True, auto_now=False)
    modified_at = models.DateField('Fecha de modificacion', auto_now=True, auto_now_add=False)
    eliminated_at = models.DateField('Fecha de eliminacion', auto_now=True, auto_now_add=False)    
    codigo_verificacion = models.CharField('Codigo de verificación', max_length=255, null=True,unique=True)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos']

    def __str__(self):
        return f" Usuario {self.username}"
    
    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"
    
    def save(self,  *args, **kwargs):
        self.codigo_verificacion = f"{self.numero_documento} {self.id}"
        self.codigo_verificacion = make_password(self.codigo_verificacion)
        super(Usuario, self).save(*args,**kwargs)
