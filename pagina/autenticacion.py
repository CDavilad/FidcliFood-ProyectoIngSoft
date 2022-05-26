from django.db.models import query
from pagina.models import Usuario
import sqlite3

def verificarPrevioRegistro(criterio, tipo = 'usuario'):
    query = False
    if tipo == 'usuario':
        query = Usuario.objects.filter(celular=criterio).exists()
    return query

def consultaUsuario(id):
    es_usuario = Usuario.objects.filter(celular = id).exists()
    if es_usuario:
        user = Usuario.objects.get(celular = id)
        info = {}
        info["nombre"] = user.nombre
        info["celular"] = user.celular
        info["correo"] = user.correo
    print(info)
    return info   

def consultaUsuarioCorreo(id):
    es_usuario = Usuario.objects.filter(correo = id).exists()
    if es_usuario:
        user = Usuario.objects.get(correo = id)
        info = {}
        info["nombre"] = user.nombre
        info["celular"] = user.celular
        info["correo"] = user.correo
    print(info)
    return info   

def actualizarUsuario(id, nombre, celular):
    target = Usuario.objects.get(celular = id)
    target.nombre = nombre
    target.celular = celular
    target.save(update_fields=['nombre','celular'])