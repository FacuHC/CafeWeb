from django import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings 
from .views import tienda, agregar_producto, eliminar_producto, restar_producto , limpiar_carrito

urlpatterns = [
    path('Tienda',tienda,name ="Tienda"),
    path("agregar/<int:producto_id>",agregar_producto,name="Add"), 
    path("eliminar/<int:producto_id>",eliminar_producto,name="Del"), 
    path("restar/<int:producto_id>",restar_producto,name="Sub"), 
    path("limpiar",limpiar_carrito,name="CLS"), 
    

    # static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
]
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)