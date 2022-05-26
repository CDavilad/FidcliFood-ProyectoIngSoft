from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from pagina import autenticacion
from pagina import models
import pagina.autenticacion as user
import sqlite3
from PIL import Image

# Create your views here.

login_check = False
usuario = None

def home(request):
    productos = models.Producto.objects.filter(tienda = "McDonalds")
    print(productos)
    global login_check
    global usuario
    if login_check:
        correo = request.POST['correo']
        info_usuario = user.consultaUsuarioCorreo(correo)
        usuario = info_usuario
        return (request, 'inicio.html', {'info_usuario':info_usuario})
    
    if request.method == 'POST':
        try:
            detalleUsuario = models.Usuario.objects.get(correo = request.POST['correo'], password = request.POST['password'])
            print("Usuario=", detalleUsuario)
            request.session['correo'] = detalleUsuario.correo
            request.session['password'] = detalleUsuario.password
            login_check = True
            usuario = detalleUsuario
            print("celular = ", usuario.celular)
            return inicioApps(request)
        except models.Usuario.DoesNotExist:
            messages.info(request, "Correo o contraseña inválido")
    return render(request, 'index.html')

def logout(request):
    global login_check
    global usuario
    usuario = None
    login_check = False
    return render(request, 'saltocerrar.html')

def saltoRegistro(request):
    return render(request, 'saltoregistro.html')

def registro(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        celular = request.POST['celular']
        correo = request.POST['correo']
        password = request.POST['password']

        print (nombre, celular, correo, password)
        
        if len(password) < 8:
            messages.info(request, 'la contraseña debe contener por lo menos 8 caracteres')
        
        elif autenticacion.verificarPrevioRegistro(celular):
            messages.info(request, 'celular ya registrado')
        
        else:
            agregar = models.Usuario(nombre = nombre, celular = celular, correo = correo, password = password)
            agregar.save()
            global usuario 
            usuario = user.consultaUsuario(celular)
            return saltoRegistro(request)

    return render (request, 'registro.html')


def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')

def inicioApps(request):
    global usuario
    tiendas = models.Tienda.objects.all()
    correo = usuario.correo
    info_usuario = user.consultaUsuarioCorreo(correo)
    return render(request,'inicio.html', {'tiendas' : tiendas, 'info_usuario':info_usuario})

def perfil(request):
    global usuario
    info_usuario = user.consultaUsuario(usuario.celular)
    return render(request, "perfil.html", {"info_usuario": info_usuario})

def tienda(request, nombretienda):
    productos = models.Producto.objects.filter(tienda = nombretienda)
    return render(request, 'tienda.html', {'productos':productos,'tienda':nombretienda})

def SaltoEditar(request, codigo):
    return render(request, 'saltoeditarperfil.html', {"codigo":codigo})

def EditarPerfil(request):
    codigo = usuario.celular
    info_usuario = user.consultaUsuario(codigo)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        celular = request.POST['celular']
        user.actualizarUsuario(codigo,nombre,celular)
        return SaltoEditar(request, codigo)
    return render(request, 'editarPerfil.html',{"info_usuario": info_usuario})




