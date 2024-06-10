from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import FormularioEntrar, FormularioRegistro
from sweetify import success, warning, info, error

def entrar(request):
    if request.method == 'GET':
        contexto = {
            'titulo': 'Bienvenido',
            'formulario':FormularioEntrar()
        }
        return render(request,'entrar.html',contexto)
    if request.method == 'POST':
        datos_usuario = FormularioEntrar(data=request.POST)
        es_valido = datos_usuario.is_valid()
        if es_valido:
            username = datos_usuario.cleaned_data['usuario']
            password = datos_usuario.cleaned_data['contrasenia']
            usuario = authenticate(username=username,password=password)
            if usuario is not None:
                login(request, usuario)
                success(request, f'Bienvenido {usuario.username}')
                return redirect('principal')
        contexto = {
            'titulo': 'Bienvenido',
            'formulario': datos_usuario
        }
        warning(request,'Usuario y contraseña incorrectos')
        return render(request,'entrar.html',contexto)
    

def registro(request):
    if request.method == 'GET':
        contexto = {
            'formulario': FormularioRegistro()
        }
        return render(request, 'registro.html', contexto)
    elif request.method == 'POST':
        formulario_usuario = FormularioRegistro(request.POST)
        es_valido = formulario_usuario.is_valid()
        if es_valido:
            formulario_usuario.save()
            success(request,'Gracias por unirte!')
            return redirect('entrar')
        contexto = {
            'formulario': formulario_usuario
        }
        warning(request, 'Completa bien los campos por favor :/')
        return render(request, 'registro.html', contexto)
        
def cerrar_sesion(request):
    if request.user.is_authenticated:
        logout(request)
        success(request,'Nos vemos!')
    return redirect('principal')