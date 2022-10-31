"""CafeWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from .views import TrabajadoresForm, buscar_order, busqueda_order, ordenarForm, form_productos, inicio, lista_order, lista_producto, lista_trabajadores
from django.urls import path

urlpatterns = [
    path('', inicio, name="inicio"),    #incio
    path('producto', lista_producto , name = "producto"), #Lista con todos los productos
    path("ordenarFormulario", ordenarForm, name = "ordenar"), #Hacer pedidos
    path("form_producto", form_productos, name="form_productos"), #Agregar productos
    path("lista_order", lista_order,name="lista_order" ), # Lista con todas las pedidos
    path("trabajadores",lista_trabajadores,name="trabajadores"), # Lista de los empleados
    path("TrabajadoresFormulario",TrabajadoresForm,name="TrabajadoresFormulario"), #Agregar empleados
    path("Busqueda_order",busqueda_order, name="busqueda_order"), #Buscar una pedido
    path("buscar_order",buscar_order, name="buscar_order"), 
]
