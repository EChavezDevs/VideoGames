from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django import forms


# Create your models here.

class Usuario(AbstractUser):
    MIEMBRO = [
        ('SI', 'Si'),
        ('NO', 'No')
    ]
    username = models.CharField(max_length=150, unique=True)
    
    Nombre_User = models.CharField(max_length=150)
    Apellido_User = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    direccion = models.CharField(max_length=255)
    tarjeta_asociada = models.IntegerField()
    Miembro = models.CharField(max_length=3, choices=MIEMBRO)

    django_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    groups = models.ManyToManyField('auth.Group', related_name='usuario_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='usuario_set', blank=True)

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return self.username
    
class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['Nombre_User', 'Apellido_User', 'email', 'direccion', 'tarjeta_asociada', 'Miembro']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']    