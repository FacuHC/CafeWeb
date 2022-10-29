from django.db import models
# Create your models here.


class Producto(models.Model):

    nombre = models.CharField(max_length=50)    
    descripcion = models.CharField(max_length=50)    
    precio  = models.IntegerField()


class Trabajadores(models.Model):
  
    nombre = models.CharField(max_length=50)    
    apellido = models.CharField(max_length=50)    
    email = models.EmailField()


class order(models.Model):

    nombre_cliente = models.CharField(max_length=50)    
    apellido_cliente = models.CharField(max_length=50)    
    email_cliente = models.EmailField()
    items_cliente = models.CharField(max_length=100)
    precio_total = models.IntegerField()
