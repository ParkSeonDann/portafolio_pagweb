from django.urls import path
from .views import *

urlpatterns = [
    path('productos/', mostrar_prods, name='ver_prod'),
    path('listar/', listar_productos, name='listar_productos'),
    path('crear/', crear_producto, name='crear_producto'),
    path('editar/<int:producto_id>/', editar_producto, name='editar_producto'),
    path('eliminar/<int:producto_id>/', delete_producto, name='delete_producto'),
]