from django.contrib import admin

from CafeApp.models import Producto, Trabajadores, order,Avatar

admin.site.register(Producto)

admin.site.register(Trabajadores)

admin.site.register(order)

admin.site.register(Avatar)


# Register your models here.
