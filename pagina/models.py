from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.forms import PasswordInput
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.conf import settings
from numpy import delete

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100, primary_key=True)
    celular = models.IntegerField()
    password = models.CharField(max_length=100, null=False)
    def _str_(self):
        return self.celular
    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"

class Tienda(models.Model):
    nombre = models.CharField(primary_key=True,max_length=100)
    direccion = models.CharField(max_length=100)
    celular = models.IntegerField(null=True)
    imagen = models.ImageField(upload_to = 'pagina/imagenes/', null = True)
    class Meta:
        verbose_name = "tienda"
        verbose_name_plural = "tiendas"

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=2000, null=True)
    valor = models.IntegerField()
    cantidad = models.IntegerField()
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, null=True, blank = True)
    imagen = models.ImageField(upload_to = 'pagina/imagenes/', null = True)

class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null = False, blank = True)
    contenido = models.CharField(max_length=500)
    fecha = models.CharField(max_length=12, null=False)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)




'''
   
    class Compra
    class 
'''