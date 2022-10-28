from django.http import HttpResponse
from django.shortcuts import render

from CafeApp.models import Producto

# Create your views here.


def inicio(request):

    return render(request, "inicio.html")
   


def lista_producto(request):

    #lista = Producto.objects.all()

    return render(request, "lista_producto.html")
