from django.db import models

# Create your models here.

class dispositivos(models.Model):
    marca_dispositivos = models.CharField(max_length=255)
    modelo_dispositivos = models.CharField(max_length=255)
    fecha_dispositivos = models.DateField()

class usuarios(models.Model):
    usuario_nombre = models.CharField(max_length=50)
    usuario_apellido = models.CharField(max_length=50)
    usuario_telefono = models.CharField(max_length=15)
    nombre_usuario = models.CharField(max_length=50)
    email_usuario = models.EmailField()
    password = models.CharField(max_length=50)