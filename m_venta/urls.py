from django.urls import path
from .views import *
from m_producto.views import mostrar_prods

urlpatterns = [
    path('productos/<int:producto_id>/', agregar_al_carrito, name='vista_carrito'),
    path('carrito/', mostrar_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:item_id>/', aumentar_cantidad, name='aumentar_cantidad'),
    path('carrito/disminuir/<int:item_id>/', disminuir_cantidad, name='disminuir_cantidad'),
    path('carrito/eliminar/<int:item_id>/', eliminar_producto, name='eliminar_producto'),
    path('carrito/limpiar/', limpiar_carrito, name='limpiar_carrito'),
    path('comprobante/<int:carrito_id>/', generar_comprobante, name='generar_comprobante'),
    path('pagar/', pagar_total, name='pagar_total'),
    path('historial/', historial_ventas, name='historial_ventas'),
]