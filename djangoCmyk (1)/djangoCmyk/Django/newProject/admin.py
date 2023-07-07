from django.contrib import admin
# Register your models here.
from .models import tipoUsuario, Usuario, despacho, pedido, producto

admin.site.register(tipoUsuario)
admin.site.register(Usuario) 
admin.site.register(producto) 
admin.site.register(despacho) 
admin.site.register(pedido) 
