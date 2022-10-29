from django.http import HttpResponse
from django.shortcuts import redirect, render

from CafeApp.models import Producto, order
from .forms import ordenarFormulario

# Create your views here.


def inicio(request):

    return render(request, "inicio.html")
   


def lista_producto(request):

    lista = Producto.objects.all()

    return render(request, "lista_producto.html", {"lista_productos": lista})



def form_productos(request):

    if request.method == "POST":

        lista_producto = Producto(nombre=request.POST["nombre"], descripcion=request.POST["descripcion"],precio=request.POST["precio"] )
        lista_producto.save()

    

    return render(request, "form_productos.html")



def lista_order(request):

    lista = order.objects.all()

    return render(request, "lista_order.html", {"lista_order": lista})


def form_orders(request):
   
    if request.method == "POST":
        formulario_ordenes = ordenarFormulario(request.POST)
        if formulario_ordenes.is_valid():
            data = formulario_ordenes.cleaned_data
            lista_order = order(nombre=data["nombre_cliente"], apellido=data["apellido_cliente"] )          
            lista_order.save()
        
    else:
        formulario_ordenes = ordenarFormulario()
    
    return render(request, "form_ordens.html", {"formulario_ordenes": formulario_ordenes})

#email_cliente =data["email_cliente "],items_cliente =data["items_cliente "],precio_total =data["precio_total "]