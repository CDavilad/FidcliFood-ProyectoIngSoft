from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from pagina import autenticacion
from pagina import models
import sqlite3
from PIL import Image

# Create your views here.

login_check = False

def home(request):
    global login_check
    if login_check:
        return render(request, 'inicio.html')
    
    if request.method == 'POST':
        try:
            detalleUsuario = models.Usuario.objects.get(correo = request.POST['correo'], password = request.POST['password'])
            print("Usuario=", detalleUsuario)
            request.session['correo'] = detalleUsuario.correo
            request.session['nombre'] = detalleUsuario.nombre
            login_check = True
            return render(request, 'inicio.html')
        except models.Usuario.DoesNotExist as e:
            messages.info(request, "Correo o contraseña inválido")
    return render(request, 'index.html')

def logout(request):
    global login_check
    login_check = False
    return home(request)

def registro(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        celular = request.POST['celular']
        correo = request.POST['correo']
        password = request.POST['password']

        print (nombre, celular, correo, password)
        
        if len(password) <= 8:
            messages.info(request, 'la contraseña debe contener por lo menos 8 caracteres')
        
        elif autenticacion.verificarPrevioRegistro(celular):
            messages.info(request, 'celular ya registrado')
        
        else:
            agregar = models.Usuario(nombre = nombre, celular = celular, correo = correo, password = password)
            agregar.save()
            return render(request, 'home.html')

    return render (request, 'registro.html')


def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')

def inicioApps(request):
    searchTerm = request.GET.get('searchProducto')
    return render(request, 'inicio.html', {'searchTerm':searchTerm})

def perfil(request):
    return HttpResponse('<h1>This is your profile</h1>')




