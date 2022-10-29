
from django import forms


class ordenarFormulario(forms.Form):
  
    nombre_cliente = forms.CharField(max_length=50)    
    apellido_cliente = forms.CharField(max_length=50)    
    email_cliente = forms.EmailField()
    items_cliente = forms.CharField(max_length=100)
    precio_total = forms.IntegerField()
