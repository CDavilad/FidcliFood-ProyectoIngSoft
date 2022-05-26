"""FidcliFood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pagina import views as paginaViews

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', paginaViews.home),
    path('home/', paginaViews.home, name = 'inicio'),
    path('inicioApp/', paginaViews.inicioApps, name = 'inicioApp'),
    path('about/', paginaViews.about, name = 'about'),
    path('registro/', paginaViews.registro, name = 'registro'),
    path('cerrar_sesion/', paginaViews.logout, name = 'cerrar_sesion'),
    path('perfil/', paginaViews.perfil, name = 'perfil'),
    path('tienda/<str:nombretienda>/', paginaViews.tienda, name='tienda'),
    path('editarPerfil/', paginaViews.EditarPerfil, name='editarPerfil'),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
