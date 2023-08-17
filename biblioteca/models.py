from django.db import models

# Create your models here.

class Libros(models.Model):
    nombre = models.CharField(max_length=100)
    Editorial = models.CharField(max_length=100)
    año_publicacion = models.IntegerField()

class Empleados(models.Model):
    usuario = models.CharField(max_length=40)
    clave = models.IntegerField()

class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    