from django import forms
from juegosApp.models import Juego
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    pass 

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = '__all__'
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={
                'type': 'date', 
                'class': 'form-control fecha-publicacion', 
                'id': 'id_fecha_publicacion',  
            }),
        }    