from django.contrib import admin

from CafeApp.models import Producto, Trabajadores,Avatar,order,comanda

admin.site.register(Producto)

admin.site.register(Trabajadores)

# admin.site.register(order)

admin.site.register(Avatar)

admin.site.register(order)

admin.site.register(comanda)
# Register your models here.
