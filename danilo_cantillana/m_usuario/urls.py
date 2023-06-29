from django.urls import path
from .views import *

urlpatterns = [
    path('entrar/',entrar,name='entrar'),
    path('registrar/',registro, name='registro'),
    path('salir/',cerrar_sesion, name='cerrar_sesion'),
]