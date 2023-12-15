from django.contrib import admin

from .models import Categoria, Producto, PedidoPersonalizado, EstadoCarrito, Proveedor

from .carrito import Carrito

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(PedidoPersonalizado)
admin.site.register(Carrito)
admin.site.register(EstadoCarrito)
admin.site.register(Proveedor)

