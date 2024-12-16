from django import forms
from .models import Usuario, User
from django.contrib.auth.forms import UserChangeForm

class UsuarioForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(), 
        label="Confirma la Contraseña"
    )
    class Meta:
        model = Usuario
        fields = ['username', 'Nombre_User', 'Apellido_User', 'email', 'direccion', 'tarjeta_asociada', 'Miembro', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
    username = forms.CharField(label="Usuario", max_length=100)
    Nombre_User = forms.CharField(label="Nombre")
    Apellido_User = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Email")
    direccion = forms.CharField(label="Dirección", max_length=600)
    tarjeta_asociada = forms.IntegerField(label="Número de tarjeta")
    Miembro = forms.ChoiceField(
        choices=Usuario.MIEMBRO,
        label="Miembro activo",
        widget=forms.Select,
        required=False
    )
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Las contraseñas no coinciden.")
        return cleaned_data

class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['Nombre_User', 'Apellido_User', 'email', 'direccion', 'tarjeta_asociada', 'Miembro']
        username = forms.CharField(label="Usuario", max_length=100)
        Nombre_User = forms.CharField(label="Nombre")
        Apellido_User = forms.CharField(label="Apellido")
        email = forms.EmailField(label="Correo electrónico")
        direccion = forms.CharField(label="Dirección", max_length=600)
        tarjeta_asociada = forms.IntegerField(label="Ingrese número de tarjeta")
        Miembro = forms.BooleanField(label="Miembro", required=False)


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email'] 