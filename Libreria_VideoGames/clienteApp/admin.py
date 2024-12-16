from django.contrib import admin
from clienteApp.models import Usuario
# Register your models here.
class InformacionAdminUser(admin.ModelAdmin):
    list_display = ['Nombre_User', 'Apellido_User', 'email', 'direccion', 'tarjeta_asociada', 'Miembro']

admin.site.register(Usuario, InformacionAdminUser)