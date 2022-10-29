from django.contrib import admin

from CafeApp.models import Producto, Trabajadores, order

admin.site.register(Producto)

admin.site.register(Trabajadores)

admin.site.register(order)

# Register your models here.
