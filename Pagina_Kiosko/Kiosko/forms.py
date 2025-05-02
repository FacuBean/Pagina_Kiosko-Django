from django import forms
from django.contrib.auth.models import User

from .models import Producto, Venta, Cliente

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'precio', 'categoria', 'stock']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['producto', 'cantidad','cliente']
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), empty_label="Seleccione un producto")
    cliente = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="Seleccione un cliente")

    
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']
