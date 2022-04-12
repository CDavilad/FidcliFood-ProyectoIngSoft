from django.db.models import query
from pagina.models import Usuario
import sqlite3

def verificarPrevioRegistro(criterio, tipo = 'usuario'):
    query = False
    if tipo == 'usuario':
        query = Usuario.objects.filter(celular=criterio).exists()
    return query

