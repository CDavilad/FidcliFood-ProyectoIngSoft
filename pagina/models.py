from tabnanny import verbose
from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100, primary_key=True)
    celular = models.IntegerField()
    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"

class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    valor = models.IntegerField()
    cantidad = models.IntegerField()

'''
    class Tienda
    class Compra
    class 
'''