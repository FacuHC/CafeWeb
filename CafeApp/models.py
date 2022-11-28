from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Producto(models.Model):

    nombre = models.CharField(max_length=50)    
    descripcion = models.CharField(max_length=50)    
    precio  = models.IntegerField() 
    imagen = models.ImageField(upload_to="items/",null=True, blank=True)
    
    def __str__(self):

        return f"{self.nombre} - {self.precio}"


class Trabajadores(models.Model):
  
    nombre = models.CharField(max_length=50)    
    apellido = models.CharField(max_length=50)    
    email = models.EmailField()

    def __str__(self):

        return f"{self.nombre} - {self.apellido} - {self.email}"



class order(models.Model):

    nombre_cliente = models.CharField(max_length=50)    
    apellido_cliente = models.CharField(max_length=50)    
    email_cliente = models.EmailField()
    items_cliente = models.CharField(max_length=100)
    precio_total = models.IntegerField()

    def __str__(self):

        return f"{self.nombre_cliente} - {self.apellido_cliente} - {self.email_cliente} - {self.precio_total}"

class comanda(models.Model):

    nombre_cliente = models.CharField(max_length=50)    
    mesa = models.IntegerField()
    items_cliente = models.CharField(max_length=100)
    precio_total = models.IntegerField()

    def __str__(self):

        return f"{self.nombre_cliente} - {self.items_cliente} - {self.precio_total}"



class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)


class cliente(models.Model):

    profile_pic = models.ImageField(null = True, blank = True)
