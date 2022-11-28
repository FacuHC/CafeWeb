from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist

from django.dispatch import receiver
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators  import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models.signals import post_save
from Cart.context_processor import total_total

from .models import Producto, Trabajadores, Avatar, order, comanda
from .forms import TrabajadoresFormulario, ordenarFormulario, ProductosFormulario, UserEditForm,  UserRegisterForm, avatarupload, ComandaFormulario
from django.contrib.auth.models import User

# Create your views here.


def inicio(request):
    

    return render(request, "inicio.html",)
 



#---------------PRODUCTOS------------#


def lista_producto(request):

    lista = Producto.objects.all()

    return render(request, "lista_producto.html", {"lista_productos": lista})



def form_productos(request):

    if request.method == 'POST':
        formulario_producto = ProductosFormulario(request.POST)
        if formulario_producto.is_valid():
            data = formulario_producto.cleaned_data
            listadeproducto = Producto(nombre=data["nombre"], descripcion=data["descripcion"], precio=data["precio"])         
            listadeproducto.save()
            
            
        
    else:
        formulario_producto = ProductosFormulario()
    
    return render(request, "form_productos.html", {"formulario_producto": formulario_producto})


        

#---------------ORDENES------------#

@staff_member_required(login_url="Login")
def lista_order(request):

    lista = order.objects.all()


    return render(request, "lista_order.html", {"lista_order": lista})


def ordenarForm(request):
   
    if request.method == 'POST':
        formulario_ordenes = ordenarFormulario(request.POST)
        print(formulario_ordenes)
        if formulario_ordenes.is_valid():
            data = formulario_ordenes.cleaned_data
            lista_order = order(nombre_cliente=data["nombre_cliente"], apellido_cliente=data["apellido_cliente"],email_cliente=data["email_cliente"])          
            
            lista_order.save()
        
    else:
        formulario_ordenes = ordenarFormulario()
    
    return render(request, "form_ordens.html", {"formulario_ordenes": formulario_ordenes})



#-----------comanda-----------#

def list_comanda(request):

    lista = comanda.objects.all()


    return render(request, "list_comanda.html", {"list_comanda": lista})

def form_comanda(request):

    if request.method == 'POST':
        formulario_producto = ComandaFormulario(request.POST)
        if formulario_producto.is_valid():
            data = formulario_producto.cleaned_data
            listadeproducto = comanda(nombre_cliente=data["nombre_cliente"], mesa=data["mesa"], items_cliente=data["items_cliente"], precio_total=data["precio_total"])         
            listadeproducto.save()
            return redirect("list,comanda")
        
    else:
        formulario_producto = ComandaFormulario()
    
    return render(request, "form_comanda.html", {"formulario_producto": formulario_producto})

def eliminar_comanda(request, id):
    
    if request.method == "POST":

        producto = comanda.objects.get(id=id)
        producto.delete()
        lista = comanda.objects.all()

        return render(request, "list_comanda.html", {"list_comanda": lista}) 



#---------------TRABAJADORES------------#

@login_required
def lista_trabajadores(request):

    listaDeTrabajadores = Trabajadores.objects.all()

    return render(request, "lista_trabajadores.html", {"lista_trabajadores": listaDeTrabajadores})



@login_required
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


#---------------BUSCADORES------------#

#----------B-ORDENES-----------#
def busqueda_order(request):


    return render(request, "busqueda_order.html")


def buscar_order(request):
    
   Buscar_nombre_cliente = request.GET["nombre_cliente"]

   Order = order.objects.get(nombre_cliente = Buscar_nombre_cliente)

   return render(request, "resultado_busqueda_order.html", {"Order": Order})

   

#----------B-TRABAJADORES-----------#

def busqueda_trabajador(request):
    return render(request, "busqueda_trabajador.html")


def buscar_trabajador(request):
    
   Buscar_nombre_trabajador = request.GET["nombre"]

   trabajador = Trabajadores.objects.get(nombre = Buscar_nombre_trabajador)

   return render(request, "resultado_busqueda_trabajador.html", {"trabajador": trabajador})

#----------B-PRODUCTOS-----------#


def busqueda_producto(request):
    return render(request, "busqueda_producto.html")


def buscar_producto(request):
    
    if request.GET["nombre"]:
         Buscar_nombre_producto = request.GET["nombre"]
         producto = Producto.objects.get(nombre = Buscar_nombre_producto)
         
       
         return render(request, "resultado_busqueda_producto.html", {"producto": producto})
    
    else:
        
        respuesta = "No hay informaicon para esa busqueda"

        return render(request, "busqueda_producto.html", {"respuesta": respuesta})



#----------ELIMINAR-----------#


def eliminar_producto(request, id):
    
    if request.method == "POST":

        producto = Producto.objects.get(id=id)
        producto.delete()
        lista = Producto.objects.all()

        return render(request, "lista_producto.html", {"lista_productos": lista}) 


def eliminar_order(request, id):
    
    if request.method == "POST":

        orden1 = order.objects.get(id=id)
        orden1.delete()
        lista = order.objects.all()

        return render(request, "lista_order.html", {"lista_order": lista}) 


def eliminar_trabajador(request, id):
    
    if request.method == "POST":

        trabajador = Trabajadores.objects.get(id=id)
        trabajador.delete()
        lista = Trabajadores.objects.all()

        return render(request, "lista_trabajadores.html", {"lista_trabajadores": lista}) 




#----------EDICION-----------#


def editar_prducto(request, id):

    producto = Producto.objects.get(id=id)

    if request.method == 'POST':
        formulario_producto = ProductosFormulario(request.POST)
        if formulario_producto.is_valid():
      
            data = formulario_producto.cleaned_data
      
            producto.nombre=data["nombre"]
            producto.descripcion=data["descripcion"]
            producto.precio=data["precio"]
            producto.imagen=data["imagen"]

            producto.save()

            return HttpResponseRedirect("/producto/")
            
        
    else:

        formulario_producto = ProductosFormulario(initial={
            "nombre":producto.nombre,
            "descripcion":producto.descripcion,
            "precio":producto.precio,
            "imagen":producto.imagen
        })
    
    return render(request, "editar_producto.html", {"formulario_producto": formulario_producto, "id": producto.id})



def editar_trabajador(request, id):

    trabajador = Trabajadores.objects.get(id=id)

    if request.method == 'POST':
        formulario_workers = TrabajadoresFormulario(request.POST)
        if formulario_workers.is_valid():
      
            data = formulario_workers.cleaned_data
      
            trabajador.nombre=data["nombre"]
            trabajador.apellido=data["apellido"]
            trabajador.email=data["email"]    
      
            trabajador.save()

            return HttpResponseRedirect("/trabajadores/")
            
        
    else:

        formulario_workers = TrabajadoresFormulario(initial={
            "nombre":trabajador.nombre,
            "apellido":trabajador.apellido,
            "email":trabajador.email
        })
    
    return render(request, "editar_trabajador.html", {"formulario_workers": formulario_workers, "id": trabajador.id})




class ProductosDetail(DetailView):

    model = Producto
    template_name = "producto_detail.html"
    context_object_name =  "Producto"
    




def loginView(request):
   
    if request.method == "POST":
        form1 = AuthenticationForm(request, data=request.POST)
        if form1.is_valid():
        
            data = form1.cleaned_data
          
            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username = usuario, password = psw) 
           
            if user:

                login(request, user)
                
                return render(request, "inicio.html", {"mensaje": f'Bienvendio {usuario}'})

            else:
            
             return render(request, "inicio.html", {"mensaje": f'Error datos incorrectos'})
       
        return render(request, "inicio.html", {"mensaje": f'Error, formulario invalido'})
        
    else:
        form1 = AuthenticationForm()
    
    return render(request, "login.html", {"form1": form1})

def register(request):


    if request.method == 'POST':
      
        form1 = UserRegisterForm(request.POST)
       
        if form1.is_valid():
      
            username = form1.cleaned_data["username"]

            form1.save()

            return render(request, "inicio.html", {"mensaje": f"Usuario{username} creado con existo"})
      
        else:

            return render(request, "inicio.html", {"mensaje": f"Error en la crecion"})

        
    else:

        form1 = UserRegisterForm()
    
        return render(request, "registro.html", {"form1": form1})



def editar_perfil(request):
    
    usuario = request.user

    if request.method == 'POST':
        form1 = UserEditForm(request.POST)
        if form1.is_valid():
      
            data = form1.cleaned_data
      
            usuario.first_name=data["first_name"]
            usuario.last_name=data["last_name"]
            usuario.email=data["email"]    
            # usuario.set_avatar(data["avatar"])
            usuario.set_password(data["password1"])
      
            usuario.save()

            return render(request, "editar_perfil.html", {"mensaje": f"Datos actualizados"})

        # return render(request,"editar_perfil.html", {"mensaje": f"Contraseñas no coninciden"} )

    else:

        form1 = UserEditForm(instance=request.user)
    
    return render(request, "editar_perfil.html", {"form1": form1})

@login_required
def changeAvatar(request):
     
     
    usuario = request.user

    if request.method == 'POST':
        form1 = avatarupload(request.POST)
        if form1.is_valid():
      
            data = form1.cleaned_data
      
            usuario.imagen=data["imagen"]
          
            usuario.save()

            return render(request, "avatarUL.html", {"mensaje": f"foto actualizados"})


    else:

        form1 = avatarupload(instance=request.user)
    
    return render(request, "avatarUL.html", {"form1": form1})



##############################TIENDA##############################

@login_required
def store(request):
    
    
    productos = Producto.objects.all()

    return render(request, "store.html", {"productos":productos})


##############################CONFI##############################


def confi(request):


    return render(request, "confi.html")



def placeholder(request):

     
    return render(request, "inicio.html", {"mensaje_no_pagina": f"NO HAY PAGINA AUN"})


def more_info(request):


    return render(request,"more_info.html")