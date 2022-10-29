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
from unicodedata import name
from .views import form_orders, form_productos, inicio, lista_order, lista_producto
from django.urls import path

urlpatterns = [
    path('', inicio, name="inicio"),
    path('producto', lista_producto , name = "producto"),
    path("ordenar", form_orders , name = "ordenar"),
    path("form_producto", form_productos, name="form_productos"),
    path("lista_order", lista_order,name="lista_order" ),
]
