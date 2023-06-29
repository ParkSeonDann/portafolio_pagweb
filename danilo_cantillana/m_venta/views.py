from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from m_producto.models import Producto
from .models import *
from django.db.models import Sum
from sweetify import success, warning, info, error

# Create your views here.
@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    print(producto)
    carrito = Carrito.objects.filter(user=request.user).first()
    print(carrito)

    if producto.cantidad == 0:
        return redirect('productos_agotados')

    if carrito:
        item_carrito = ItemCarrito.objects.filter(carrito=carrito, producto=producto).first()
        if item_carrito:
            item_carrito.cantidad += 1
            item_carrito.save()
        else:
            item_carrito = ItemCarrito(carrito=carrito, producto=producto, cantidad=1)
            item_carrito.save()
    else:
        carrito = Carrito(user=request.user)
        carrito.save()
        item_carrito = ItemCarrito(carrito=carrito, producto=producto, cantidad=1)
        item_carrito.save()

    producto.cantidad -= 1
    producto.save()

    success(request,'Producto agregado a tu carrito :3')
    return redirect('ver_prod')

@login_required
def mostrar_carrito(request):
    carrito = Carrito.objects.filter(user=request.user).first()

    if not carrito:
        carrito = Carrito(user=request.user)
        carrito.save()

    items = ItemCarrito.objects.filter(carrito=carrito)
    total_cant = items.aggregate(total=Sum(F('producto__precio') * F('cantidad')))['total'] if items else 0

    context = {
        'carrito': carrito,
        'items': items,
        'total_cant': total_cant
    }

    return render(request, 'carrito.html', context)


@login_required
def aumentar_cantidad(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    item.cantidad += 1
    item.save()
    return redirect('ver_carrito')

@login_required
def disminuir_cantidad(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    if item.cantidad > 1:
        item.cantidad -= 1
        item.save()
    return redirect('ver_carrito')

@login_required
def eliminar_producto(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    item.delete()
    return redirect('ver_carrito')

@login_required
def limpiar_carrito(request):
    carrito = Carrito.objects.filter(user=request.user).first()
    if carrito:
        items = ItemCarrito.objects.filter(carrito=carrito)
        items.delete()
    return redirect('ver_carrito')

def generar_comprobante(request, carrito_id):
    carrito = get_object_or_404(Carrito, id=carrito_id)
    items = ItemCarrito.objects.filter(carrito=carrito)
    total = 0
    for item in items:
        total += item.producto.precio * item.cantidad

    context = {
        'carrito': carrito,
        'items': items,
        'total': total,
    }

    return render(request, 'pay.html', context)

# def pagar_total(request):
#     carrito = Carrito.objects.filter(user=request.user).first()
#     total_cant = carrito.itemcarrito_set.aggregate(total=Sum(F('producto__precio') * F('cantidad')))['total'] or 0

#     venta = Venta(total_cant=total_cant, user=request.user)
#     venta.save()
#     print(venta)

#     carrito.itemcarrito_set.all().delete()

#     success(request, 'Pago realizado con éxito.')

#     return redirect('ver_prod')

def pagar_total(request):
    carrito = Carrito.objects.filter(user=request.user).first()
    total_cant = carrito.itemcarrito_set.aggregate(total=Sum(F('producto__precio') * F('cantidad')))['total'] or 0

    venta = Venta(total_cant=total_cant, user=request.user)
    venta.save()

    for item in carrito.itemcarrito_set.all():
        producto_venta = ProductoVenta(venta=venta, producto=item.producto, cantidad=item.cantidad)
        producto_venta.save()

    carrito.itemcarrito_set.all().delete()

    success(request, 'Pago realizado con éxito.')

    return redirect('ver_prod')

def historial_ventas(request):
    ventas = Venta.objects.filter(user=request.user).order_by('-fecha_venta')
    context = {
        'ventas': []
    }

    for venta in ventas:
        productos_venta = ProductoVenta.objects.filter(venta=venta)
        productos = []
        for producto_venta in productos_venta:
            producto = producto_venta.producto
            cantidad = producto_venta.cantidad
            total_producto = producto.precio * cantidad
            productos.append((producto, cantidad, total_producto))

        venta_info = {
            'venta': venta,
            'productos': productos,
            'total_producto': total_producto
        }
        context['ventas'].append(venta_info)

    return render(request, 'historial_ventas.html', context)


