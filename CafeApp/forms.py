
from django import forms
from .models import Producto, Avatar, comanda
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

class ordenarFormulario(forms.Form):
  
    nombre_cliente = forms.CharField(max_length=50)    
    apellido_cliente = forms.CharField(max_length=50)    
    email_cliente = forms.EmailField()
    


class TrabajadoresFormulario(forms.Form):
  
    nombre = forms.CharField(max_length=50)    
    apellido = forms.CharField(max_length=50)    
    email = forms.EmailField()


class ComandaFormulario(forms.ModelForm):
    
    class Meta:
        model = comanda 
        fields = ("__all__")


class ProductosFormulario(forms.ModelForm):
    
    class Meta:
        model = Producto 
        fields = ("__all__")


class UserEditForm(UserChangeForm):
    
    password = forms.CharField(
        help_text = "",
        widget=forms.HiddenInput(), required=False

    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label=" RepetirContraseña", widget=forms.PasswordInput, required=False)


    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]


    def clean_password(self):

       password2 = self.cleaned_data["password2"]
       if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden!")
       return password2 


class UserRegisterForm(UserCreationForm):

    class Meta:

        model = User 
        fields = ("username","last_name", "first_name","email")


class avatarupload(forms.ModelForm):
 
    class Meta:
        model = Avatar 
        fields = ("__all__")
