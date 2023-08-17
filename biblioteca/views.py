from django.shortcuts import render
from biblioteca.models import Libros, Empleados,Clientes
from django.http import HttpResponse
from biblioteca.forms import Users_form, cliente_form, libros_form

# Create your views here.

def inicio(request):
    return render(request, "padre.html")


def registrar_empleados(request):
    if request.method == "POST":
        mi_formulario = Users_form(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            usuario = Empleados(usuario=datos['usuario'], clave=datos['clave'])
            usuario.save()
            return render(request, "formulario_registro.html")
    return render(request, "formulario_registro.html")

def registrar_clientes(request):
    if request.method == "POST":
        mi_formulario_cliente = cliente_form(request.POST)
        if mi_formulario_cliente.is_valid():
            datos_cliente = mi_formulario_cliente.cleaned_data
            cliente = Clientes(nombre=datos_cliente['nombre'], email=datos_cliente['email'], direccion=datos_cliente['direccion'])
            cliente.save()
            return render(request, "form_registro_clientes.html")
    return render(request, "form_registro_clientes.html")

def alta_libros(request):
    if request.method == "POST":
        mi_formulario_libros = libros_form(request.POST)
        if mi_formulario_libros.is_valid():
            datos_libros = mi_formulario_libros.cleaned_data
            libros = Libros(nombre=datos_libros['nombre'], Editorial=datos_libros['Editorial'], año_publicacion=datos_libros['año_publicacion'])
            libros.save()
            return render(request, "form_registro_libros.html")
    return render(request, "form_registro_libros.html")

def buscar_libros(request):
    return render(request, "buscar_libros.html")


def buscar(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']
        librerias = Libros.objects.filter(nombre__icontains = nombre)
        return render(request, "resultado_busqueda.html", {"librerias":librerias})
    else:
        return HttpResponse("campo vacio")

