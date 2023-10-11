from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.db.models import ForeignKey

class CustomUserManager(BaseUserManager):
    def create_user(self, nombre_usuario, email_usuario, password=None, **extra_fields):
        if not email_usuario:
            raise ValueError('El campo Email es requerido')
        email_usuario = self.normalize_email(email_usuario)
        user = self.model(nombre_usuario=nombre_usuario, email_usuario=email_usuario, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre_usuario, email_usuario, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(nombre_usuario, email_usuario, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    usuario_nombre = models.CharField(max_length=50)
    usuario_apellido = models.CharField(max_length=50)
    usuario_telefono = models.CharField(max_length=15)
    nombre_usuario = models.CharField(max_length=50, unique=True)
    email_usuario = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'nombre_usuario'
    REQUIRED_FIELDS = ['email_usuario']

    def __str__(self):
        return self.nombre_usuario

class dispositivos(models.Model):
    marca_dispositivos = models.CharField(max_length=255)
    modelo_dispositivos = models.CharField(max_length=255)
    fecha_dispositivos = models.DateField()
    propietario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='dispositivos')

    def __str__(self):
        return f"{self.marca_dispositivos} {self.modelo_dispositivos}"
