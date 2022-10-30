from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Producto, order, Trabajadores
from .forms import TrabajadoresFormulario, ordenarFormulario

# Create your views here.


def inicio(request):

    return render(request, "inicio.html")
   
#---------------PRODUCTOS------------


def lista_producto(request):

    lista = Producto.objects.all()

    return render(request, "lista_producto.html", {"lista_productos": lista})



def form_productos(request):

    if request.method == "POST":

        lista_producto = Producto(nombre=request.POST["nombre"], descripcion=request.POST["descripcion"],precio=request.POST["precio"] )
        lista_producto.save()

    

    return render(request, "form_productos.html")

#---------------ORDENES------------


def lista_order(request):

    lista = order.objects.all()


    return render(request, "lista_order.html", {"lista_order": lista})


def ordenarForm(request):
   
    if request.method == 'POST':
        formulario_ordenes = ordenarFormulario(request.POST)
        print(formulario_ordenes)
        if formulario_ordenes.is_valid():
            data = formulario_ordenes.cleaned_data
            lista_order = order(nombre_cliente=data["nombre_cliente"], apellido_cliente=data["apellido_cliente"],email_cliente=data["email_cliente"],items_cliente =data["items_cliente"],precio_total =data["precio_total"])          
            lista_order.save()
            return redirect("lista_order")
        
    else:
        formulario_ordenes = ordenarFormulario()
    
    return render(request, "form_ordens.html", {"formulario_ordenes": formulario_ordenes})


#---------------TRABAJADORES------------


def lista_trabajadores(request):

    listaDeTrabajadores = Trabajadores.objects.all()

    return render(request, "lista_trabajadores.html", {"lista_trabajadores": listaDeTrabajadores})




def TrabajadoresForm(request):
   
    if request.method == "POST":
        formulario_workers = TrabajadoresFormulario(request.POST)
        if formulario_workers.is_valid():
            data = formulario_workers.cleaned_data
            listaDeTrabajadores = Trabajadores(nombre = data["nombre"], apellido = data["apellido"],email = data["email"])
            listaDeTrabajadores.save()
        
    else:
        formulario_workers = TrabajadoresFormulario()
    
    return render(request, "form_workers.html", {"formulario_workers": formulario_workers})