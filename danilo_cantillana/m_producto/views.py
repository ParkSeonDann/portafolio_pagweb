from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from sweetify import success, warning
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def mostrar_prods(request):
    productos = Producto.objects.all()
    contexto = {
        'productos': productos
    }
    return render(request,'productos.html', contexto)


def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'admin/listar.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'admin/crear.html', {'form': form})


def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'admin/editar.html', {'form': form, 'producto': producto})

def delete_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('listar_productos')