from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'imagen']
        
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del producto'
                }),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Precio del producto (MXN)'
                }),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'URL de la imagen'
                })
        }
        
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio del producto (MXN)',
            'imagen': 'URL de la imagen'
        }
        
        error_messages = {
            'nombre': {
                'required': 'Este campo es obligatorio'
            },
            'precio': {
                'required': 'Este campo es obligatorio',
                'invalid': 'Por favor, ingresa un precio válido'
            },
            'imagen': {
                'required': 'Este campo es obligatorio'
            }
        }