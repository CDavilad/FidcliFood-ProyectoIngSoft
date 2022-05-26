from django.contrib import admin

from .models import Usuario
from .models import Producto
from .models import Tienda
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Tienda)