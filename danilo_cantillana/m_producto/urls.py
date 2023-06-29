from django.urls import path
from .views import *

urlpatterns = [
    path('productos/', mostrar_prods, name='ver_prod')
]