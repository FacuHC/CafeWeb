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

from .views import (register,loginView, editar_trabajador, editar_prducto, 
 eliminar_trabajador, eliminar_order, eliminar_producto, TrabajadoresForm, buscar_order, 
 buscar_producto, buscar_trabajador, busqueda_order, busqueda_producto, busqueda_trabajador, ordenarForm, 
 form_productos, inicio, lista_order, lista_producto, lista_trabajadores, editar_perfil, ProductosDetail, changeAvatar, store)

from django.contrib.auth.views import LogoutView

from django.urls import path

urlpatterns = [
    path('', inicio, name="inicio"),    #incio
    path("store",store,name="store"), #store
    path('producto/', lista_producto , name = "producto"), #Lista con todos los productos
    path("ordenarFormulario/", ordenarForm, name = "ordenar"), #Hacer pedidos
    path("form_producto/", form_productos, name="form_productos"), #Agregar productos
    path("lista_order/", lista_order,name="lista_order" ), # Lista con todas las pedidos
    path("trabajadores/",lista_trabajadores,name="trabajadores"), # Lista de los empleados
    path("TrabajadoresFormulario/",TrabajadoresForm,name="TrabajadoresFormulario"), #Agregar empleados
    path("Busqueda_order/",busqueda_order, name="busqueda_order"), #Buscar una pedido
    path("buscar_order/",buscar_order, name="buscar_order"), 
    path("busqueda_trabajador/",busqueda_trabajador, name="busqueda_trabajador"), #Buscar una trabajador
    path("buscar_trabajador/",buscar_trabajador, name="buscar_trabajador"),
    path("busqueda_producto/",busqueda_producto, name="busqueda_producto"), #Buscar una producto
    path("buscar_producto/",buscar_producto, name="buscar_producto"),
    path("eliminar_producto/<int:id>",eliminar_producto, name="eliminar_producto"),
    path("EliminarOrden/<int:id>",eliminar_order, name="EliminarOrden"),
    path("eliminar_trabajador/<int:id>",eliminar_trabajador, name="eliminar_trabajador"),
    path("editar_prducto/<int:id>",editar_prducto, name="editar_prducto"),
    path("editar_trabajador/<int:id>",editar_trabajador, name="editar_trabajador"),
    path("Login",loginView, name="Login"),
    path("Registrar",register, name="Registrar"),
    path("Logout",LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path("EditarPerfil",editar_perfil, name="EditarPerfil"),
    path("DetallesProductos/<pk>",ProductosDetail.as_view(), name="DetallesProductos"),
    path("changeAvatar",changeAvatar, name="changeAvatar")
   




    # path("CreaProducto/",ProductoCreate.as_view(), name="CreaProducto"),
    # path("ProductoList",ProductoList.as_view(), name="ProductoList"),
    # path("ActualizaProductos/<pk>",ProductosUpdate.as_view(), name="ActualizaProductos"),
    # path("EliminaProducto/<pk>",ProductosDelete.as_view(), name="EliminaProducto"),



    
    
   


]
