from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from sweetify import success, warning
from .models import Producto

# Create your views here.
def mostrar_prods(request):
    productos = Producto.objects.all()
    contexto = {
        'productos': productos
    }
    return render(request,'productos.html', contexto)