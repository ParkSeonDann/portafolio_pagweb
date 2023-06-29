from django.contrib import admin
from m_venta.models import *
# Register your models here.
admin.site.register(Venta)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)
admin.site.register(ProductoVenta)