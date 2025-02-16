from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    
    password1 = forms.CharField(
    label='Contraseña',
    widget=forms.PasswordInput(
        attrs={
            'class': 'form-input',
            'pattern': '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$',
            'placeholder': 'Ingrese su contraseña',
            'title': 'Necesitas definir una contraseña segura',
            'required': True
        }
    )
)
    password2 = forms.CharField(
    label='Contraseña',
    widget=forms.PasswordInput(
        attrs={
            'class': 'form-input',
            'pattern': '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$',
            'placeholder': 'Repite su contrasena',
            'title': 'Necesitas definir una contraseña segura',
            'required': True
        }
    )
)

    
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']
        
        widgets = {
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'required': True,
                    'pattern': '^[a-zA-Z0-9]+@utez\.edu\.mx$',
                    'tittle': 'Debes ingresar un correo electronico valido de la UTEZ',   
                }
            ),
            'name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'required': True
                }
            ),
            'surname': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'required': True
                }
            ),
            'control_number': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'required': True,
                    'pattern':'^[0-9](5)[a-zA-Z](2)[0-9](3)$',
                    'tittle': 'Debes ingresar una matricula de la utez',
                    'maxlength': '20'
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'pattern': '^[0-9]+$',
                    'title': 'Ingresa solo números',
                    'max': '100',
                    'min': '1'
                }
            ),
            'tel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'pattern': '^\d{10}$',
                    'title': 'Ingresa solo números',
                    'maxlength': '15',
    }
),

        } 

class CustomUserLoginForm(AuthenticationForm):
    pass